from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Article

class ArticleListView(ListView):
     model = Article
     template_name = 'blog/articles_list.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
     model = Article
     fields = ('title', 'subtitle', 'body', 'picture')
     success_url = reverse_lazy('articles_list')

     def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
     model = Article
     fields = ('title', 'subtitle', 'body', 'picture')
     success_url = reverse_lazy('articles_list')     

class ArticleDetailView(DetailView):
    model = Article
    success_url = reverse_lazy('articles_list')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles_list')

