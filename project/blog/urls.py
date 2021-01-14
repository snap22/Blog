from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='blog-welcome'),
    path('home/', views.home, name='blog-home'),
    path('browse/', views.browse_posts, name='blog-browse'),
    path('post/new/', views.post_new, name='blog-post-new'),
    path('post/<int:pk>/', views.post_view, name='blog-post-view'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='blog-post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-post-delete'),
    path('post/comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='blog-comment-edit'),
    path('post/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='blog-comment-delete'),
]