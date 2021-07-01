from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'post_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
