from django import forms
from django.contrib import admin

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.

# formulaire d'admin personnalisé pour PlayGame
class PlayGameAdminForm(forms.ModelForm):
    class Meta:
        model = PlayGame
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si une saison est sélectionnée, filtrer les semaines pour cette saison
        if 'season' in self.data:
            try:
                season_id = int(self.data.get('season'))
                self.fields['week'].queryset = Week.objects.filter(season_id=season_id)
            except (ValueError, TypeError):
                pass  # Si la saison n'est pas encore sélectionnée, la liste est vide
        elif self.instance.pk:
            # Si un objet est déjà créé, on filtre les semaines par la saison de cet objet
            self.fields['week'].queryset = self.instance.week.season.weeks.all()


class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    form = PlayGameAdminForm
    list_display = ('team_local', 'team_visitor', 'week', 'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('-played_at',)
    date_hierarchy = 'played_at'
    list_per_page = 16

    # Activer l'autocomplétion pour le champ 'week'
    autocomplete_fields = ['week']

    # Hook pour personnaliser le formulaire dans l'admin
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            # Si un objet est déjà sélectionné, ajuster la liste des semaines en fonction de la saison
            form.base_fields['week'].queryset = obj.week.season.weeks.all()
        return form


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