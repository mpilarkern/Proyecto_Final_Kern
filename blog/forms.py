from PIL import Image
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=64, required=True)
    subtitle = forms.CharField(max_length=256, required=False)
    body = forms.CharField(required=True)
    
    
