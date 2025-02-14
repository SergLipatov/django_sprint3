"""
Модуль admin.py приложения blog.

Этот модуль определяет классы администрирования для моделей
Category, Post и Location, которые используются для настройки
отображения и редактирования объектов этих моделей
в административной панели Django.
"""
from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Category, Post, Location


class BaseModelAdmin(admin.ModelAdmin):
    """Абстрактная базовая модель для общих полей."""

    list_editable = (
        'is_published',
    )

    class Meta:
        abstract = True  # Эта модель абстрактная.


class CategoryAdmin(BaseModelAdmin):
    """Управление админкой модели Category."""

    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )


class LocationAdmin(BaseModelAdmin):
    """Управление админкой модели Location."""

    list_display = (
        'name',
        'is_published',
        'created_at'
    )


class PostAdmin(BaseModelAdmin):
    """Управление админкой модели Post."""

    list_display = (
        'title',
        'category',
        'location',
        'pub_date',
        'is_published',
        'created_at'
    )


admin.site.empty_value_display = 'Не задано'
Group._meta.verbose_name = 'группа'
Group._meta.verbose_name_plural = 'Группы'
User._meta.verbose_name = 'пользователь'
User._meta.verbose_name_plural = 'Пользователи'

# Регистрация моделей в административной панели.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
