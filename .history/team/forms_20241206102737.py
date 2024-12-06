from django import forms

from .fields import TeamChoiceField
from .models import Teams

class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = [
            'name',
            'town',
            'stadium',
            'division',
            'owner',
            'founded',
            'thumbnail',
            'colorOne',
            'colorTwo'
        ]
        widgets = {'founded': forms.SelectDateWidget(years=range(1920, 2024))}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            # Remplacer les champs qui font référence à Teams
            if isinstance(self.fields[field_name], forms.ModelChoiceField) and self.fields[field_name].queryset.model == Teams:
                self.fields[field_name] = TeamChoiceField(queryset=Teams.objects.all())