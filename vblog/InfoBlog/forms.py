from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок поста')
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':150, 'rows':20}))
    is_published = forms.BooleanField(label='Публикация', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')