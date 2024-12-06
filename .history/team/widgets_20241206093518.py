from typing import Any, Sequence
from django.forms import Select
from django.forms.widgets import _OptAttrs


class TeamGroupedSelected(Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_