from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('webhook/', views.rasa_webhook, name='rasa_webhook'),
]