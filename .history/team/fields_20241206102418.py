# fields.py
from django import forms
from .models import Teams
from .widgets import TeamGroupedSelect

class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__(queryset=queryset, widget=TeamGroupedSelect, *args, **kwargs)
