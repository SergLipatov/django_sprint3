from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Location(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
    )
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
    )
    description = models.TextField('Описание')
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField('Текст')

    pub_date = models.DateTimeField()

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField('Опубликовано', default=True)







