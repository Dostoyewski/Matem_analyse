from django.db import models
from django.utils import timezone
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
    title = models.CharField(max_length=200, blank=True)
    # Полный текст поста
    text = models.CharField(max_length=1000, blank=True)
    # Дата публикации
    published = models.DateTimeField(default=timezone.now)
    # Тип объявления
    type = models.IntegerField(choices=TYPE, default=2)
    # Документ, приложенный к посту
    doc = models.FileField(default=None, blank=True)
    # Порядок публикации
    order_id = models.IntegerField(default=0)

    def __str__(self):
        return "статья " + '"' + str(self.title) + '"'
