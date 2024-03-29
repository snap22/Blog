"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('project/', include('project.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

handler400 = "blog.views.error_views.error_400"
handler403 = "blog.views.error_views.error_403"
handler404 = "blog.views.error_views.error_404"
handler500 = "blog.views.error_views.error_500"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls')),
    path("account/", include("account.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="account/password_reset/password_reset.html"), name="reset_password"),
    path("reset_password_done/", auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset/password_reset_done.html"), name="password_reset_done"),
    path("reset_password/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset/password_reset_complete.html"), name="password_reset_complete"),
    path("tinymce/", include('tinymce.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
