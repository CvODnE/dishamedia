from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('verify-secret-code/', views.verify_secret_code, name='verify_secret_code'),
    path('add/', login_required(views.add_content), name='add_content'),
    path('add/news/', login_required(views.add_news), name='add_news'),
    path('add/gallery/', login_required(views.add_gallery), name='add_gallery'),
    path('delete-news/<int:pk>/', views.delete_news, name='delete_news'),
    path('delete-gallery/<int:pk>/', views.delete_gallery, name='delete_gallery'),
]