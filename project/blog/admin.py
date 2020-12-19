from django.contrib import admin
from .models import Post

# Registrácia modelu aby ho bolo vidno v /admin 
admin.site.register(Post)