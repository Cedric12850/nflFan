from typing import Any, Sequence
from django.forms import Select
from django.forms.widgets import _OptAttrs

from .models import Divisions, Teams


class TeamGroupedSelected(Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        divisions = {}
        for team in Teams.objects.select_related('division').all()
            divisions.setdefault(team)