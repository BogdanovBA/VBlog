from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'get_html_photo', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'category', 'content', 'post_image', 'is_published', 'time_create', 'time_update', 'get_html_photo')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.post_image:
            return mark_safe(f"<img src='{object.post_image.url}' width=75>")

    get_html_photo.short_description = 'Image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)
    prepopulated_fields = {"slug": ("category_name",)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'ADMIN'
admin.site.site_header = 'admin-panel VBlog'
