from django.shortcuts import render

def iniciar(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

def about(request):
    contexto = {}
    http_response = render(
        request,
        'about.html',
        contexto
    )
    return http_response


