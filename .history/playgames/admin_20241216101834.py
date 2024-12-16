from django import forms
from django.contrib import admin
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.

def get_weeks(request):
    season_id = request.GET.get('season')
    logger.info(f"Received season_id: {season_id}")
    
    if not season_id:
        return JsonResponse([], safe=False)

    weeks = Week.objects.filter(season_id=season_id).values('id', 'name')
    logger.info(f"Fetched weeks: {list(weeks)}")
    
    return JsonResponse(list(weeks), safe=False)

class PlayGameForm(forms.ModelForm):
    season = forms.ModelChoiceField(
        queryset=Season.objects.all(),
        required=False,
        label="Season",
        widget=forms.Select(attrs={"id": "id_season"}),  # Assurez l'ID correct pour JS
    )

    class Meta:
        model = PlayGame
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si une saison est sélectionnée, filtrez les weeks.
        if 'season' in self.data:
            try:
                season_id = int(self.data.get('season'))
                self.fields['week'].queryset = Week.objects.filter(season_id=season_id)
            except (ValueError, TypeError):
                self.fields['week'].queryset = Week.objects.none()
        elif self.instance.pk:
            # Remplissage si en mode édition
            self.fields['week'].queryset = Week.objects.filter(season=self.instance.week.season)
        else:
            # Aucune saison sélectionnée : pas de weeks disponibles
            self.fields['week'].queryset = Week.objects.none()

class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    form = PlayGameForm
    list_display = ('team_local', 'team_visitor', 'week', 'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('-played_at',)
    date_hierarchy = 'played_at'
    list_per_page = 16

    class Media:
        js = ('admin/js/playgame_admin.js',)  # Lien vers votre JS personnalisé

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('get_weeks/', get_weeks, name='get_weeks'),
        ]
        return custom_urls + urls

class SuperbowlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'winner', 'teamOne', 'teamTwo', 'stadium', 'town')  # Colonnes affichées
    list_filter = ('year', 'winner', 'town')  # Filtres par année, gagnant, ville
    search_fields = ('name', 'stadium', 'winner__name')  # Recherche par nom, stade, gagnant
    ordering = ('-year',)  # Tri décroissant par année

class SeasonAdmin(admin.ModelAdmin):
    # Définir les champs à afficher dans la liste
    list_display = ('name', 'start_date', 'end_date')

    # Ajouter des filtres pour faciliter la recherche par dates
    list_filter = ('start_date', 'end_date')

    # Ajouter une barre de recherche pour rechercher par nom
    search_fields = ('name',)

    # Permettre de trier les saisons par date de début
    ordering = ('start_date',)

    # Ajouter une hiérarchie de dates pour faciliter la navigation par période
    date_hierarchy = 'start_date'

    # Optionnel : Permet de limiter les choix dans les formulaires d'administration si nécessaire
    # autocomplete_fields = ('champ',)

    # Personnalisation de l'affichage de l'objet dans le formulaire d'administration
    def __str__(self):
        return f"Saison {self.name} ({self.start_date} - {self.end_date})"

admin.site.register(PlayGame, PlayGameAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Superbowls, SuperbowlsAdmin)
admin.site.register(Season, SeasonAdmin)