"""
Настройки конфигурации приложения для Django.

Этот модуль содержит конфигурацию приложения Django,
которая используется для настройки основных параметров приложения,
таких как его имя и настройки сигнала.
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    """Конфигурация приложения 'Blog'."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = _('Блог')
