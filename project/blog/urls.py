from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('welcome/', views.welcome, name='blog-welcome'),
    path('post/new/', views.post_new, name='blog-post-new'),
    path('post/<int:post_id>/', views.post_view, name='blog-post-view'),
]