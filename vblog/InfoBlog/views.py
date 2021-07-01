from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, Http404
from InfoBlog.models import Posts, Category


def index(request):
    return render(request, 'InfoBlog/index.html')


def all_posts(request):
    posts = Posts.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'category_selected': 0,
    }
    return render(request, 'InfoBlog/posts_page.html', context=context)


def post_num(request, post_id):
    return HttpResponse(f"Оторбражение поста с id = {post_id}")


def show_category(request, cat_id):
    posts = Posts.objects.filter(category_id=cat_id)
    categories = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'categories': categories,
        'category_selected': cat_id,
    }
    return render(request, 'InfoBlog/posts_page.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def access_denied(request, exception):
    return HttpResponseNotAllowed('<h1>Доступ запрещен</h1>')