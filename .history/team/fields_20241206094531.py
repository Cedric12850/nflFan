from django import forms

# Création du champs personnalisé pour les équipes par division
class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__(queryset=queryset, widget=TeamGroupesSelect, *args, **kwargs)