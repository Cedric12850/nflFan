from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.

# Formulaire personnalisé pour le PlayGameAdmin
class PlayGameForm(forms.ModelForm):
    class Meta:
        model = PlayGame
        fields = '__all__'
    
    # Champs pour la saison et la semaine
    season = forms.ModelChoiceField(queryset=Season.objects.all(), required=True)
    week = forms.ModelChoiceField(queryset=Week.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si une saison est sélectionnée, filtrer les semaines disponibles
        if 'season' in self.data:
            season_id = self.data.get('season')
            if season_id:
                self.fields['week'].queryset = Week.objects.filter(season_id=season_id)
        elif self.instance.pk:  # Si l'objet PlayGame existe déjà, on met à jour les semaines en fonction de la saison
            self.fields['week'].queryset = Week.objects.filter(season=self.instance.week.season)

        # JavaScript pour mettre à jour les semaines en fonction de la saison
        self.fields['season'].widget.attrs.update({
            'onchange': 'updateWeeks(this.value);'
        })

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/core.js', 'admin/js/actions.js', 'js/admin/season_week_filter.js')

class WeekAdmin(admin.ModelAdmin):
    search_fields = ('week_number', 'season__name')
    list_filter = ('season',)
    list_display = ('week_number', 'season')

class PlayGameAdmin(admin.ModelAdmin):
    form = PlayGameForm
    list_display = ('team_local', 'team_visitor', 'week',  'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('-played_at',)
    date_hierarchy = 'played_at'
    # Pagination (afficher 16 éléments par page)
    list_per_page = 16 

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