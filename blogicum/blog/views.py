"""
Модуль views.py приложения blog.

Cодержит определения представлений (views),
которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
"""


from django.shortcuts import render



def index(request):
    """Отображает страницу блога."""
    template = 'blog/index.html'
    reversed_posts = list(posts)
    reversed_posts.reverse()
    context = {'posts': reversed_posts}
    return render(request, template, context)


def post_detail(request, id):
    """Отображает детальную страницу поста по id.

    Parameters:
    request (HttpRequest): Объект запроса.

    id (int): индетификатор поста.

    Returns:
    HttpResponse: HTTP-ответ с отрендеренным шаблоном.
    """
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Отображает посты по категориям (пока заготовка).

    Parameters:
    request (HttpRequest): Объект запроса.

    category_slug (str): Наименование категории.

    Returns:
    HttpResponse: HTTP-ответ с отрендеренным шаблоном.
    """
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
