from django.shortcuts import render

def list_articles(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='blog/articles_list.html',
        context=contexto,
    )
    return http_response