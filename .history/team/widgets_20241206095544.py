from django.forms import Select
from django.forms.widgets import _OptAttrs

from .models import Divisions, Teams

# Widget pour récupérer les équipes de chaques divisions
class TeamGroupedSelect(Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        divisions = {}
        for team in Teams.objects.select_related('division').order_by('division__name', 'name'):
            divisions.setdefault(team.division.name, []).append((team.id, team.name))

        return [
            (division, teams) for division, teams in divisions.items()
        ]

