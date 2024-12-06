

# Création du champs personnalisé pour les équipes par division
from django import forms


class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args)