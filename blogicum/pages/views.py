"""
Модуль views.py приложения pages.

Cодержит определения представлений (views),
которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
"""


from django.shortcuts import render


def about(request):
    """Отображает страницу 'about'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Отображает страницу 'rules'."""
    template = 'pages/rules.html'
    return render(request, template)
