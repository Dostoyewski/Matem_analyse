from django.db import models
import datetime

TYPE = (
    (0, "Practice"),
    (1, "Lecture"),
    (2, "Info")
)


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
    # Тип объявления
    type = models.IntegerField(choices=TYPE, default=2)
    # Документ, приложенный к посту
    doc = models.FileField(default=None, blank=True)
