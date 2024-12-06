

# Création du champs personnalisé pour les équipes par division
from django import forms


class TeamChoiceField(forms.ModelChoiceField)