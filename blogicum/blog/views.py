from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    if post_id not in post_id_list:
        raise Http404('Page not found (такого "post_id" не существует). Пост не найден')
    return render(request, 'blog/detail.html', {'post': post_id_list[post_id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
