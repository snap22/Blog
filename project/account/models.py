from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """ Trieda, ktorá je rozšírením pre účet používateľa """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default="default.png", upload_to="profile_pictures")
    

    def __str__(self):
        return f"Profile for { self.user.username }"


