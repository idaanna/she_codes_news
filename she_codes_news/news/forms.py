from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        # removed 'author'
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'datetime-local'
                }
            )
        }