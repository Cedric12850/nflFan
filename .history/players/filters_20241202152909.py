from django import forms
import django_filters
from players.models import PLayers

class PLayersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains', 
        label='Player Name', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'})
    )
    position = django_filters.ChoiceFilter(
        field_name='poste', 
        label='Poste', 
        choices=[
            ('QB', 'Quarterback'),
            ('WR', 'Wide Receiver'),
            ('RB', 'Running Back'),
            # Ajoutez d'autres positions si nécessaire
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    team = django_filters.CharFilter(
        field_name='team__name', 
        lookup_expr='icontains', 
        label='Team Name', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by team name'})
    )

    