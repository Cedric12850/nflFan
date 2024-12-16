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

    week = forms.ModelChoiceField(
        queryset=Week.objects.none(),  # Initialement vide
        required=False,
        widget=AutocompleteSelect(
            Week._meta.get_field('season').remote_field, admin.site,
        ),
    )

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/core.js', 'admin/js/actions.js')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajoutez un handler pour la saison afin de filtrer les semaines
        if self.instance and self.instance.week:
            self.fields['week'].queryset = Week.objects.filter(season=self.instance.week.season)

        # Filtrer les semaines selon la saison sélectionnée
        if 'season' in self.data:
            season_id = self.data.get('season')
            if season_id:
                self.fields['week'].queryset = Week.objects.filter(season_id=season_id)

class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
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