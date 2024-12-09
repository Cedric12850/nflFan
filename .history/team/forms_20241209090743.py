from django import forms

from team.widgets import TeamGroupedSelect

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


class PlayGameForm(forms.ModelForm):
    team_local = TeamChoiceField(queryset=Teams.objects.all(), required=True)
    team_visitor = TeamChoiceField(queryset=Teams.objects.all(), required=True)

    class Meta:
        model = PlayGame
        fields = ['team_local', 'team_visitor', 'score_local', 'score_visitor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Appliquer le widget de sélection d'équipes groupées pour 'team_local' et 'team_visitor'
        self.fields['team_local'].widget = TeamGroupedSelect()
        self.fields['team_visitor'].widget = TeamGroupedSelect()

