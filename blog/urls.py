from django.urls import path
from blog.views import search_articles, ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
urlpatterns = [
    path('search-articles/', search_articles, name='search_articles'),
    path('articles/', ArticleListView.as_view(), name='articles_list'),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="read_article"),
    path('new-article/', ArticleCreateView.as_view(), name='new_article'),
    path('edit-article/<int:pk>/', ArticleUpdateView.as_view(), name='edit_article'),
    path('delete-article/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
]