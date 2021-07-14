from django.urls import path
from InfoBlog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('posts/', InfoBlogPosts.as_view(), name='posts'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('category/<slug:cat_slug>', PostsCategory.as_view(), name='category'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register')
]