from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']  # Ajoute les champs nécessaires

    # Personnalisez les labels ou les validations si nécessaire
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['email'].label = "Adresse email"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmer le mot de passe"
        self.fields['last_name'].label = "Nom"
        self.fields['first_name'].label = "Prénom"
