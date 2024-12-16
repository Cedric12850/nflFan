from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nom d’utilisateur'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adresse email'}),
        }
        labels = {
            'username': "Nom d'utilisateur",
            'email': "Adresse email",
            'password1': "Mot de passe",
            'password2': "Confirmer le mot de passe",
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