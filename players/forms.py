from django import forms

from players.models import PLayers
from players.widgets import CustomWidgets
from team.models import Teams

class PlayerForm(forms.ModelForm):
    class Meta:
        model = PLayers
        fields = [
            'name',
            'firstName',
            'team',
            'poste',
            'number',
            'age',
            'thumbnail',
            'actif',
            'injury',
        ]
        widgets = {
            'name': CustomWidgets.text_input_with_placeholder("Nom du joueur"),
            'firstName': CustomWidgets.text_input_with_placeholder("Prénom du joueur"),
            'team': CustomWidgets.select_input,
            'poste': CustomWidgets.select_input,
            'number': CustomWidgets.number_input,
            'age': CustomWidgets.date_input,
            'thumbnail': CustomWidgets.file_input,
            'actif': CustomWidgets.checkbox_input,
            'injury': CustomWidgets.checkbox_input,
        }
        labels = {
            'name': 'Nom :',
            'firstName': 'Prénom :',
            'number': 'N',
            'poste': 'position :',
            'injury': 'blessé',
            'age': 'Date de naissance :',
            'thumbnail': 'Photo :',
        }


        