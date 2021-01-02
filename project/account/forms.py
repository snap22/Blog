from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class AccountCreationForm(UserCreationForm):
    """ Formulár pre vytvorenie novéo užívateľa, ktorý dedí z django formulára pre užívateľa"""

    email = forms.EmailField()

    class Meta:
        """ Vnorená trieda pre konfiguráciu """

        model = User
        fields = ["username","email","password1","password2"]


class AccountUpdateForm(forms.ModelForm):
    """ Formulár pre aktualizáciu údajov o uzívateľovi """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email"]




class ProfileUpdateForm(forms.ModelForm):
    """ Formulár pre aktualizáciu údajov o profile uzívateľa """

    class Meta:
        model = Profile
        fields = ["picture", "info"]
