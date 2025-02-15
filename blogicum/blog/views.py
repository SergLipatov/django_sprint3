"""
Модуль views.py приложения blog.

Cодержит определения представлений (views),
которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
"""
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


NUMBER_OF_POST_ON_THE_MAIN_PAGE = 5


def get_published_posts_in_category(category):
    """Возвращает посты из категории или 404 если их нет."""
    posts = category.blog_post_related.published()
    if not posts.exists():
        raise Http404("Нет опубликованных постов в этой категории.")
    return posts


def index(request):
    """Отображает главную страницу блога с пятью последними публикациями."""
    latest_posts = Post.objects.published()[:NUMBER_OF_POST_ON_THE_MAIN_PAGE]
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
    post = get_object_or_404(Post.objects.published(), id=id)
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
    )
    posts_in_category = get_published_posts_in_category(category)

    context = {
        'category': category,
        'post_list': posts_in_category
    }
    return render(request, 'blog/category.html', context)
