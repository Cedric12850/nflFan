from django import forms

from players.models import PLayers

class PlayerForm(forms.ModelForm):
    class Meta:
        model = PLayers
        form = TeamSelectFormMixin
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
        widgets = {'age': forms.SelectDateWidget(years=range(1980, 2024))}
    