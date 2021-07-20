from django.urls import path
from InfoBlog.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('posts/', cache_page(60)(InfoBlogPosts.as_view()), name='posts'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>', PostsCategory.as_view(), name='category'),
]