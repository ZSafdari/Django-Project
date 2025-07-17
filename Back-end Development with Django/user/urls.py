from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.SignUpView.as_view()),
    path('profile', views.UpdateProfileView.as_view()),
    path('login', views.LoginView.as_view()),
    path('list', views.UsersListView.as_view())
]
      