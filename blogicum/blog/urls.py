"""
Конфигурация маршрутизатора URL-запросов приложения blog.

Список `urlpatterns` направляет URL-адреса в представления.
Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/3.2/topics/http/urls/.
"""


from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts')
]
