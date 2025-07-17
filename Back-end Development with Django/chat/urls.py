from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('conversation', views.ConversationView.as_view()),
    path('message', views.MessageView.as_view()),
    path('message/new', views.add_message)
]