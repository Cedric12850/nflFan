from django.contrib import admin

from playgames.models import PlayGame, Superbowls, Week
# Register your models here.
class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'team_local', 'team_visitor', 'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('played_at',)
    date_hierarchy = 'played_at'
    autocomplete_fields = ('week', 'team_local', 'team_visitor')

class SuperbowlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'winner', 'teamOne', 'teamTwo', 'stadium', 'town')  # Colonnes affichées
    list_filter = ('year', 'winner', 'town')  # Filtres par année, gagnant, ville
    search_fields = ('name', 'stadium', 'winner__name')  # Recherche par nom, stade, gagnant
    ordering = ('-year',)  # Tri décroissant par année
    autocomplete_fields = ('winner', 'teamOne', 'teamTwo')  # Auto-complétion pour les équipes

class SeasonAdmin(admin.ModelAdmin):
    # Définir les champs à afficher dans la liste
    list_display = ('id', 'name', 'start_date', 'end_date')

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
ad