from django.urls import path
from perfiles.views import signup_view, login_view, LogoutView, MyProfileUpdateView, add_avatar
urlpatterns = [
    path('sign-up/', signup_view, name='sign_up'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('edit-profile/', MyProfileUpdateView.as_view(), name="edit_profile"),
    path('add-avatar/', add_avatar, name="add_avatar"),
]