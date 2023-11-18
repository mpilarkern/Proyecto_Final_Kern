from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Article
from blog.forms import ArticleForm

def list_articles(request):
    contexto = {'articles': Article.objects.all()}
    http_response = render(
        request=request,
        template_name='blog/articles_list.html',
        context=contexto,
    )
    return http_response

def post_article(request):
    if request.method == "POST":
 
        formulario = ArticleForm(request.POST) 
 
        if formulario.is_valid():
                  data=formulario.cleaned_data
                  title=data["title"]
                  subtitle=data['subtitle']
                  body=data['body']
                  author=data['author']
                  date=data['date']
                  article = Article(title=title, subtitle=subtitle, body=body, author=author, date=date)
                  article.save()
                  url_exitosa = reverse('articles_list')  
                  return redirect(url_exitosa)
    else:
        formulario = ArticleForm()
    
    http_response = render(
        request=request,
        template_name='blog/new_article.html',
        context={'formulario': formulario}
    )
    return http_response