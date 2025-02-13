"""
Модуль views.py приложения blog.

Cодержит определения представлений (views),
которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
"""
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post


def index(request):
    """Отображает главную страницу блога с пятью последними публикациями."""
    current_time = timezone.now()
    latest_posts = (
        Post.objects.filter(
            pub_date__lte=current_time,
            is_published=True,
            category__is_published=True
        ).order_by('-pub_date')[:5]
    )
    context = {'post_list': latest_posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Отображает детальную страницу поста по id.

    Parameters:
    request (HttpRequest): Объект запроса.

    id (int): индетификатор поста.

    Returns:
    HttpResponse: HTTP-ответ с отрендеренным шаблоном.
    """
    current_time = timezone.now()
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображает публикации в указанной категории.

    Parameters:
    request (HttpRequest): Объект запроса.
    category_slug (str): Идентификатор категории.

    Returns:
    HttpResponse: HTTP-ответ с отрендеренным шаблоном или 404,
    если категория не опубликована.
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    current_time = timezone.now()
    posts_in_category = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': posts_in_category
    }
    return render(request, 'blog/category.html', context)
