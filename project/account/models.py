from django.db import models
from django.contrib.auth.models import User
from project.settings_custom import DEFAULT_PICTURE, DEFAULT_PICTURE_URL, PROFILE_PICTURES_LOCATION
from account.utils import resize_image


class Profile(models.Model):
    """ Trieda, ktorá je rozšírením pre účet používateľa """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default=DEFAULT_PICTURE, upload_to=PROFILE_PICTURES_LOCATION)
    info = models.TextField(default="No info was provided", blank=True, null=True)
    
    def __str__(self):
        return f"Profile for { self.user.username }"
        
    def save(self, *args, **kwargs):
        resize_image(self.picture)
        super().save(*args, **kwargs)





