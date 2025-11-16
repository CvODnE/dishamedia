from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
import json
from .models import News, Gallery
from .forms import NewsForm, GalleryForm

# Secret code for verification
SECRET_CODE = "schoolSC"

def home(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, "home.html", {'latest_news': latest_news})

def gallery(request):
    # Get all distinct categories for the filter
    categories = Gallery.CATEGORY_CHOICES
    
    # Get the selected category from the request
    category = request.GET.get('category', '')
    
    # Filter gallery items by category if specified
    gallery_items = Gallery.objects.all()
    if category:
        gallery_items = gallery_items.filter(category=category)
    
    # Order by creation date (newest first) and then by featured status
    gallery_items = gallery_items.order_by('-created_at', '-is_featured')
    
    # Pagination - 12 items per page
    page = request.GET.get('page', 1)
    paginator = Paginator(gallery_items, 12)
    
    try:
        gallery_page = paginator.page(page)
    except PageNotAnInteger:
        gallery_page = paginator.page(1)
    except EmptyPage:
        gallery_page = paginator.page(paginator.num_pages)
    
    context = {
        'gallery_items': gallery_page,
        'categories': categories,
        'selected_category': category,
    }
    
    return render(request, "gallery.html", context)

def news(request):
    all_news = News.objects.order_by('-created_at')
    return render(request, 'news.html', {'all_news': all_news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    related_news = News.objects.exclude(pk=pk).order_by('-created_at')[:3]
    return render(request, 'news_detail.html', {
        'news': news_item,
        'related_news': related_news
    })

def contact(request):
    return render(request, "contact.html")

@require_http_methods(["POST"])
@csrf_exempt
def verify_secret_code(request):
    data = json.loads(request.body)
    if data.get('code') == 'schoolSC':
        request.session['secret_code_verified'] = True
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def add_content(request):
    if not request.session.get('secret_code_verified', False):
        return redirect('home')
    # Clear the verification after use to require it again next time
    request.session['secret_code_verified'] = False
    return render(request, 'add.html')

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            messages.success(request, 'News added successfully!')
            return redirect('web:news')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

@login_required
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.uploaded_by = request.user
            gallery.save()
            messages.success(request, 'Gallery item added successfully!')
            return redirect('web:gallery')
    else:
        form = GalleryForm()
    return render(request, 'add_gallery.html', {'form': form})

@require_POST
def delete_news(request, pk):
    try:
        data = json.loads(request.body)
        if data.get('secret_code') != SECRET_CODE:
            return JsonResponse({'status': 'error', 'message': 'Invalid secret code'}, status=403)
        
        news_item = get_object_or_404(News, pk=pk)
        news_item.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@require_POST
def delete_gallery(request, pk):
    try:
        data = json.loads(request.body)
        if data.get('secret_code') != SECRET_CODE:
            return JsonResponse({'status': 'error', 'message': 'Invalid secret code'}, status=403)
        
        gallery_item = get_object_or_404(Gallery, pk=pk)
        gallery_item.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)