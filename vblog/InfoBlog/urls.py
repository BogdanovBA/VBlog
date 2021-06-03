from django.urls import path
from InfoBlog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('posts/', all_posts),
    path('posts/<slug:post>', num_post)
]