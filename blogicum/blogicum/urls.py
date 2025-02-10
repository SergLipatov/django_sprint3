"""
Конфигурация маршрутизатора URL-запросов приложения blogicum.

Список `urlpatterns` направляет URL-адреса в представления.
Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/3.2/topics/http/urls/.
"""


from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages'))
]
