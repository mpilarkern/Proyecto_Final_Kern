from django.urls import path
from perfiles.views import signup_view, login_view, LogoutView, MyProfileUpdateView
urlpatterns = [
    path('sign-up/', signup_view, name='sign_up'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('edit-profile/', MyProfileUpdateView.as_view(), name="edit_profile"),
]