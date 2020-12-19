from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('welcome/', views.welcome, name='blog-welcome'),
]