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


class CategoryAdmin(admin.ModelAdmin):
    """Управление админкой модели Category."""

    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
    )


class LocationAdmin(admin.ModelAdmin):
    """Управление админкой модели Location."""

    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
    )


class PostAdmin(admin.ModelAdmin):
    """Управление админкой модели Post."""

    list_display = (
        'title',
        'is_published',
        'category',
        'location',
        'created_at',
        'pub_date'
    )
    list_editable = (
        'is_published',
    )


admin.site.empty_value_display = 'Не задано'
Group._meta.verbose_name = "группа"
Group._meta.verbose_name_plural = "Группы"
User._meta.verbose_name = "пользователь"
User._meta.verbose_name_plural = "Пользователи"

# Регистрация моделей в административной панели.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
