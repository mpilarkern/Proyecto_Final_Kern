from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarForm

def signup_view(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  
           url_exitosa = reverse('home')
           return redirect(url_exitosa)
   else: 
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/sign_up.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('home')
               return redirect(url_exitosa)
   else: 
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )

class LogoutView(LogoutView):
   template_name = 'perfiles/logout.html'

class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('home')
   template_name = 'perfiles/profile_form.html'

   def get_object(self, queryset=None):
       return self.request.user

def add_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES) 

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('home')
            return redirect(url_exitosa)
    else:  
        formulario = AvatarForm()
    return render(
        request=request,
        template_name="perfiles/avatar_form.html",
        context={'form': formulario},
    )
