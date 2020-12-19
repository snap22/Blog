from django.contrib import admin
from .models import Post


# Register your models here.

# Registrácia modelu aby ho bolo vidno v /admin 
admin.site.register(Post)