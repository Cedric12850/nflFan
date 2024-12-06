from django import forms
from .models import Teams

class TeamGroupedSelect(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        # Grouper les équipes par division
        divisions = {}
        for team in Teams.objects.select_related('division').order_by('division__name', 'name'):
            divisions.setdefault(team.division.name, []).append((team.id, team.name))

        return [
            (division, teams) for division, teams in divisions.items()
        ]
