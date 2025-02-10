"""
Конфигурация маршрутизатора URL-запросов приложения pages.

Список `urlpatterns` направляет URL-адреса в представления.
Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/3.2/topics/http/urls/.
"""


from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules')
]
