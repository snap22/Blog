from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    """ Formulár pre vytvorenie novéo užívateľa, ktorý dedí z django formulára pre užívateľa"""

    email = forms.EmailField()

    class Meta:
        """ Vnorená trieda pre konfiguráciu """

        model = User
        fields = ["username","email","password1","password2"]