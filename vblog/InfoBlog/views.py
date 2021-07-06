from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, Http404
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


def show_category(request, cat_id):
    posts = Posts.objects.filter(category_id=cat_id)

    context = {
        'posts': posts,
        'category_selected': cat_id,
    }
    return render(request, 'InfoBlog/posts_page.html', context=context)



def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    context = {
        'post': post,
        'category_selected': post.category_id,
    }

    return render(request, 'InfoBlog/post.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def access_denied(request, exception):
    return HttpResponseNotAllowed('<h1>Доступ запрещен</h1>')