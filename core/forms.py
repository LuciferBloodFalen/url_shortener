from django import forms
from django.core.exceptions import ValidationError
from .models import UrlMapping


class UrlShortenForm(forms.Form):
    original_url = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'url-input',
            'placeholder': 'Enter your long URL here...',
            'required': True
        })
    )
    
    def clean_original_url(self):
        url = self.cleaned_data.get('original_url')
        if not url:
            raise ValidationError('Please enter a valid URL')
        
        if not (url.startswith('http://') or url.startswith('https://')):
            raise ValidationError('Please enter a valid URL (including http:// or https://)')
        
        return url