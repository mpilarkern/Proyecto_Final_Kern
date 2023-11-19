from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Article


def search_articles(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["search"]
        
        articles = Article.objects.filter(
            Q(title__icontains=busqueda) | Q(author__icontains=busqueda) 
        )

        contexto = {
             "articles": articles,
        }
        http_response = render(
            request=request,
            template_name='blog/articles_list.html',
            context=contexto,
        )
        return http_response

class ArticleListView(ListView):
     model = Article
     template_name = 'blog/articles_list.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
     model = Article
     fields = ('title', 'subtitle', 'body', 'author', 'date')
     success_url = reverse_lazy('articles_list')

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
     model = Article
     fields = ('title', 'subtitle', 'body', 'author', 'date')
     success_url = reverse_lazy('articles_list')

class ArticleDetailView(DetailView):
    model = Article
    success_url = reverse_lazy('articles_list')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles_list')

