from django import forms
import django_filters
from players.models import PLayers, Player_position

class PLayersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains', 
        label='Player Name', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'})
    )
    poste = django_filters.ChoiceFilter(
        choices=[(poste.abrev, poste.name) for poste in Player_position.objects.all()],
        field_name='poste__abrev',  # Utilisation de l'abréviation dans le modèle PLayers
        label='Poste',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    team = django_filters.CharFilter(
        field_name='team__name', 
        lookup_expr='icontains', 
        label='Team Name', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by team name'})
    )
    number = django_filters.NumberFilter(
        field_name= 'number',
        lookup_expr=
    )

    class Meta:
        model = PLayers
        fields = ['name', 'poste', 'team']