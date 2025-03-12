from django.db import models


class Post(models.Model):
    """Создаю модель описывающую один пост
    Пост имеет поля:
    - text
    """

    text = models.TextField()

    def __str__(self):
        return self.text[:50]
