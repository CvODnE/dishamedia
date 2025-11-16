from django import forms
from .models import News, Gallery

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter news title',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; margin-bottom: 15px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter news description',
                'rows': 5,
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; resize: vertical; min-height: 150px;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*',
                'style': 'padding: 10px;'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 20px; height: 20px; margin-top: 5px;'
            })
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image', 'category', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image title',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*',
                'style': 'padding: 10px;'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 20px; height: 20px; margin-top: 5px;'
            })
        }
