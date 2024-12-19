from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.widgets import CustomWidgets

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe :",
        widget=CustomWidgets.password_input,
        help_text="Votre mot de passe doit contenir au moins 8 caractères et ne doit pas être entièrement numérique."
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe :",
        widget=CustomWidgets.password_input,
        help_text="Entrez à nouveau le même mot de passe pour confirmation."
    )
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            ]
        widgets = {
            'username': CustomWidgets.text_input_with_placeholder("Pseudo"),
            'first_name': CustomWidgets.text_input,
            'last_name': CustomWidgets.text_input,
            'email': CustomWidgets.text_input_with_placeholder("@"), 
        }
        labels = {
            'username': "Nom d'utilisateur :",
            'first_name': 'Nom :',
            'last_name': 'Prénom :',
            'email': "Adresse email :",
        }

    # Méthode pour s'assurer que l'email est obligatoire
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("L'adresse email est obligatoire.")
        return email

    # Validation des mots de passe
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les deux mots de passe ne correspondent pas.")
        return password2