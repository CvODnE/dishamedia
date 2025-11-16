from django.shortcuts import render

# Create your views here.
def newsPage(request):
    return render(request,'testapp/index.html')