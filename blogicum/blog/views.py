from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def get_posts(qs):
    return qs.select_related('location', 'author', 'category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    return render(
        request, 'blog/index.html', {'post_list': get_posts(Post.objects)[:5]}
    )


def post_detail(request, post_id):
    return render(
        request, 'blog/detail.html',
        {'post': get_object_or_404(get_posts(Post.objects), pk=post_id)}
    )


def category_posts(request, category_slug):
    """Отображение публикаций категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_posts(category.posts)
    context = {'category': category,
               'post_list': posts.filter(category=category)}
    return render(request, 'blog/category.html', context)
