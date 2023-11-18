from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    author = models.CharField(max_length=256)
    date = models.DateField(null=True)
