from django.urls import path
from blog.views import list_articles, post_article, search_articles

urlpatterns = [
    path('articles/', list_articles, name='articles_list'),
    path('new-article/', post_article, name='new_article'),
    path('search-articles/', search_articles, name='search_articles'),
]