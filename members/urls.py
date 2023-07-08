from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserUpdateView.as_view(),name='edit_profile'),
    path('password-success', views.password_success, name = 'password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view() , name = 'show_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view() , name = 'edit_profile_page'),
    path('create_profile/' , CreateProfilePageView.as_view() , name = 'create_profile'),
    
    
    
]
