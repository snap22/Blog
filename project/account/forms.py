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

    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"{username} is already in use.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"{email} is already in use.")
        return email

    class Meta:
        model = User
        fields = ["username","email"]




class ProfileUpdateForm(forms.ModelForm):
    """ Formulár pre aktualizáciu údajov o profile uzívateľa """

    class Meta:
        model = Profile
        fields = ["picture", "info"]
