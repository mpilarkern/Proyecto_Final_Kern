from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=256, blank=True)
    body = models.TextField()
    date = models.DateField(auto_now=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'
