from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=False, verbose_name='Контент')
    post_image = models.ImageField(upload_to="images/%Y/%m/d/", verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']