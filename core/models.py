from django.db import models
import datetime


class Post(models.Model):
    """
    Post with info
    """
    # Название поста
    title = models.CharField(max_length=50, blank=True)
    # Полный текст поста
    text = models.CharField(max_length=1000, blank=True)
    # Дата публикации
    published = models.DateTimeField(default=datetime.datetime.now())
