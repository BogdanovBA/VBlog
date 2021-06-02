from django.urls import path
from InfoBlog.views import *

urlpatterns = [
    path('', index),
    path('home/', index),
    path('posts/', all_posts)
]