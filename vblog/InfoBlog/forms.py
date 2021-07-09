from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'post_image', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 120, 'rows': 15}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('Длина заголовка превышает 150 символов')
        return title