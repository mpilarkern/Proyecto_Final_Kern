from django.urls import path
from perfiles.views import signin_view, login_view, LogoutView
urlpatterns = [
    path('sign-in/', signin_view, name='sign_in'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
]