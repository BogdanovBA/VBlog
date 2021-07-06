from django.urls import path
from InfoBlog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('posts/', all_posts, name='posts'),
    path('posts/<int:post_id>', show_post, name='post'),
    path('category/<int:cat_id>', show_category, name='category'),
]