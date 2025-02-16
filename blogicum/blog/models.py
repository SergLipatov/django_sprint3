"""Модуль определения моделей баз данных для приложения.

Этот модуль содержит определения моделей базы данных,
используемых в этом приложении Django.
Каждая модель соответствует таблице в базе данных
и определяет структуру данных, их типы и связи между ними.
"""
from django.db import models
from django.contrib.auth import get_user_model

from .querysets import PostQuerySet

User = get_user_model()


class BaseModel(models.Model):
    """Абстрактная базовая модель для общих полей."""

    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True  # Эта модель абстрактная.


class Location(BaseModel):
    """Модель, представляющая географическое местоположение."""

    name = models.CharField(
        verbose_name='Название места',
        max_length=256,
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(BaseModel):
    """Модель для классификации контента в различные группы."""

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256
    )
    description = models.TextField(
        'Описание',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=64,
        unique=True,
        help_text='Идентификатор страницы для URL; '
                  'разрешены символы латиницы, цифры, '
                  'дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(BaseModel):
    """Модель, представляющая пост в блоге."""

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
                  'можно делать отложенные публикации.'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )
    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = '%(app_label)s_%(model_name)s_related'
