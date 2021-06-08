from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed


def index(request):
    return render(request, 'InfoBlog/index.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def access_denied(request, exception):
    return HttpResponseNotAllowed('<h1>Доступ запрещен</h1>')


def all_posts(request):
    return HttpResponse("<h1>All posts</h1>")


def num_post(request, post):
    return HttpResponse(f"<p>Current {post}</p>")
