"""Модуль определения моделей баз данных для приложения.

Этот модуль содержит определения моделей базы данных,
используемых в этом приложении Django.
Каждая модель соответствует таблице в базе данных
и определяет структуру данных, их типы и связи между ними.
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    """Абстрактная базовая модель для общих полей."""

    # Поле, указывающее, опубликовано ли местоположение:
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    # Временная метка создания записи:
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True  # Эта модель абстрактная.


class Location(BaseModel):
    """Модель, представляющая географическое местоположение."""

    # Название местоположения:
    name = models.CharField(
        verbose_name='Название места',
        max_length=256,
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    # Строковое представление объекта местоположения:
    def __str__(self):
        return self.name


class Category(BaseModel):
    """Модель для классификации контента в различные группы."""

    # Заголовок категории:
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256
    )
    # Детальное описание категории:
    description = models.TextField(
        'Описание',
    )
    # Уникальный идентификатор категории, используемый в URL:
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

    # Строковое представление объекта категории:
    def __str__(self):
        return self.title


class Post(BaseModel):
    """Модель, представляющая пост в блоге."""

    # Заголовок публикации:
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    # Пользователь, который является автором публикации:
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    # Основное содержание публикации:
    text = models.TextField(
        verbose_name='Текст',
    )
    # Дата и время публикации:
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
                  'можно делать отложенные публикации.'
    )
    # Местоположение, связанное с публикацией, может быть пустым:
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )
    # Категория, к которой отнесена публикация:
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
