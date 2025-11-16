from django.contrib import admin
from .models import News, Gallery
from django.utils.html import format_html

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    prepopulated_fields = {}
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category')
        }),
        ('Content', {
            'fields': ('image', 'description')
        }),
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'title', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_featured',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />'.format(obj.image.url))
        return "No Image"
    thumbnail_preview.short_description = 'Preview'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'is_featured')
        }),
        ('Image', {
            'fields': ('image', 'description')
        }),
    )
