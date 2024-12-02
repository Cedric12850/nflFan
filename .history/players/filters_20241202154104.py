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
    poste = django_filters.ChoiceFilter(
        queryset=Player_position.objects.all(),  # Assurez-vous d'avoir un modèle Position dans votre projet
        field_name='poste',  # Le nom du champ dans votre modèle Player
        to_field_name='abrev',  # Vous filtrez par l'abréviation du poste
        label='Poste',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    team = django_filters.CharFilter(
        field_name='team__name', 
        lookup_expr='icontains', 
        label='Team Name', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by team name'})
    )

    