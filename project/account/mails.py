from django.core.mail import send_mail
from django.conf import settings


def send_welcome_email(username, email):
    subject = "Welcome to Blob!"
    text = f"Hello {username}, \n we would like to thank you for registering at our site!"

    send_mail(
                subject,
                text,
                settings.EMAIL_HOST_USER,   
                [email],    #prijimatelia
                fail_silently=False     #False => vyhodi exception ak sa nieco pokazi
            )