"""
Конфигурация маршрутизатора URL-запросов приложения blogicum.

Список `urlpatterns` направляет URL-адреса в представления.
Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/3.2/topics/http/urls/.
"""


from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    url(r'^admin/', admin.site.urls),
]
