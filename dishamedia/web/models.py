from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('announcements', 'Announcements'),
        ('events', 'Events'),
        ('achievements', 'Achievements'),
        ('academics', 'Academics'),
        ('others', 'Others'),
    ]
    
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='announcements'
    )
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('campus', 'Campus'),
        ('students', 'Students'),
        ('activities', 'Activities'),
        ('others', 'Others'),
    ]
    
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='events'
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Gallery Images'
        ordering = ['-created_at']

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"