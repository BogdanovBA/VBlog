from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, Http404

from InfoBlog.forms import *
from InfoBlog.models import Posts, Category


def index(request):
    return render(request, 'InfoBlog/index.html')


def all_posts(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts,
        'category_selected': 0,
    }
    return render(request, 'InfoBlog/posts_page.html', context=context)


def show_category(request, cat_slug):
    categories = Category.objects.all()
    cat = get_object_or_404(Category, slug = cat_slug)
    posts = Posts.objects.filter(category_id=cat.id)

    context = {
        'posts': posts,
        'categories': categories,
        'category_selected': cat_slug,
    }
    return render(request, 'InfoBlog/posts_page.html', context=context)



def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)

    context = {
        'post': post,
        'category_selected': post.category_id,
    }

    return render(request, 'InfoBlog/post.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = AddPostForm()
    return render(request, 'InfoBlog/add_post.html', {'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def access_denied(request, exception):
    return HttpResponseNotAllowed('<h1>Доступ запрещен</h1>')