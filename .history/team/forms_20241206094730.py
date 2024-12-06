from django import forms

from team.models import Teams

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

class TeamSelectFormMixin(forms.ModelForm):
    def __ini