import django_filters
from players.models import PLayers

class PLayersFilter(django_filters.FilterSet):
    class Meta:
        model = PLayers
        fields = {
            'name': ['icontains'],
            'position': ['exact'],
            'number'
        }