from django import forms
from .widgets import TeamGroupedSelect

# Création du champs personnalisé pour les équipes par division
class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__(queryset=queryset, widget=TeamGroupedSelect, *args, **kwargs)