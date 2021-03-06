from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='account-register'),
    path("profile/", views.profile, name="account-profile"),
    path("profile/inspect/<int:pk>/", views.profile_inspect, name="account-profile-inspect"),
    path("profile/password/", views.change_password, name="account-password-change"),
    path("profile/delete/", views.delete_account, name="account-delete"),
]