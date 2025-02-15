"""
Этот модуль определяет дополнительный набор запросов для модели Post.

Содержит класс PostQuerySet, который расширяет базовую функциональность
QuerySet и предоставляет метод для фильтрации опубликованных постов.
"""
from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):
    """Дополнительный набор запросов для модели Post."""

    def published(self):
        """
        Возвращает опубликованные посты.

        Фильтрует записи по следующим условиям:
        - Дата публикации меньше или равна текущему времени.
        - Пост должен быть помечен как опубликованный.
        - Категория поста должна быть опубликована.

        Возвращает:
            QuerySet: Набор результатов, содержащий опубликованные посты.
        """
        current_time = timezone.now()
        return self.filter(
            pub_date__lte=current_time,
            is_published=True,
            category__is_published=True
        )
