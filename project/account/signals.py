from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Metóda ktorá po registrácii nového užívateľa vytvorí nový profil a priradí ho užívateľovi. """

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """ Metóda, ktorá uloží zmeny v profile """

    instance.profile.save()


@receiver(pre_save, sender=User)
def pre_save_profile(sender, instance, **kwargs):
    """ Metóda, ktorá vymaže nie predvolenú starú fotku pred uložením """

    # ak objekt sa len vytvara tak jeho ID je None
    if instance.id is None:
        return None

    old_picture = User.objects.get(id=instance.id).profile.picture
    if old_picture.name == "default.png":
        return None

    new_picture = instance.profile.picture
    if (old_picture.name != new_picture.name):
        old_picture.delete(save=False)
    