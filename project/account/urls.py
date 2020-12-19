from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('login/', views.login_view, name='account-login'),
    path('logout/', views.logout_view, name='account-logout'),
]