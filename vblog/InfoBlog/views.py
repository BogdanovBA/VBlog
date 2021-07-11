from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, Http404
from django.views.generic import ListView, DeleteView, CreateView

from InfoBlog.forms import *
from InfoBlog.models import Posts, Category


class InfoBlogPosts(ListView):
    model = Posts
    template_name = 'InfoBlog/posts_page.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_selected'] = 0
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True)


def index(request):
    return render(request, 'InfoBlog/index.html')


#def all_posts(request):
#    posts = Posts.objects.all()
#
#    context = {
#        'posts': posts,
#        'category_selected': 0,
#    }
#    return render(request, 'InfoBlog/posts_page.html', context=context)


class PostsCategory(ListView):
    model = Posts
    template_name = 'InfoBlog/posts_page.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Posts.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_selected'] = context['posts'][0].category_id
        return context

# def show_category(request, cat_slug):
#     categories = Category.objects.all()
#     cat = get_object_or_404(Category, slug = cat_slug)
#     posts = Posts.objects.filter(category_id=cat.id)
#
#     context = {
#         'posts': posts,
#         'categories': categories,
#         'category_selected': cat_slug,
#     }
#     return render(request, 'InfoBlog/posts_page.html', context=context)


class ShowPost(DeleteView):
    model = Posts
    template_name = 'InfoBlog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

# def show_post(request, post_slug):
#     post = get_object_or_404(Posts, slug=post_slug)
#
#     context = {
#         'post': post,
#         'category_selected': post.category_id,
#     }
#
#     return render(request, 'InfoBlog/post.html', context=context)


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'InfoBlog/add_post.html'


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     else:
#         form = AddPostForm()
#     return render(request, 'InfoBlog/add_post.html', {'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def access_denied(request, exception):
    return HttpResponseNotAllowed('<h1>Доступ запрещен</h1>')