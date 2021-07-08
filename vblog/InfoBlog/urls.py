from django.urls import path
from InfoBlog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('posts/', all_posts, name='posts'),
    path('posts/<slug:post_slug>', show_post, name='post'),
    path('add_post/', add_post, name='add_post'),
    path('category/<slug:cat_slug>', show_category, name='category'),
]