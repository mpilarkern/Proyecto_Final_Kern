from django.urls import path
from blog.views import list_articles

urlpatterns = [
    path('articles/', list_articles, name='articles_list'),
]