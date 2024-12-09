from django.contrib import admin

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.
# Inline pour afficher les PlayGames sous Week dans l'admin
class PlayGameInline(admin.TabularInline):
    model = PlayGame
    extra = 0  # N'ajoute pas de nouvelles lignes vides
    fields = ('team_local', 'team_visitor', 'score_local', 'score_visitor', 'played_at')  # Champs à afficher
    readonly_fields = ('team_local', 'team_visitor', 'score_local', 'score_visitor', 'played_at')  # Champs en lecture seule

# Admin pour Week
class WeekAdmin(admin.ModelAdmin):
    list_display = ('week_number', 'season', 'is_playoff')
    search_fields = ('week_number', 'season__name')  # Recherche par numéro de semaine et nom de saison
    list_filter = ('season', 'is_playoff')  # Filtres pour la saison et les playoffs
    ordering = ('season', 'week_number')  # Tri par saison puis semaine
    inlines = [PlayGameInline]  # Inclure les PlayGames sous chaque semaine


# class WeekAdmin(admin.ModelAdmin):
#     search_fields = ('name',)  # Personnalisez si nécessaire

# class PlayGameAdmin(admin.ModelAdmin):
#     list_display = ('team_local', 'team_visitor','week',  'played_at', 'score_local', 'score_visitor')
#     list_filter = ('week__season', 'week', 'played_at')
#     search_fields = ('team_local__name', 'team_visitor__name')
#     ordering = ('played_at',)
#     date_hierarchy = 'played_at'
#     autocomplete_fields = ('week', 'team_local', 'team_visitor')
#     # Pagination (afficher 10 éléments par page)
#     list_per_page = 16 

class SuperbowlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'winner', 'teamOne', 'teamTwo', 'stadium', 'town')  # Colonnes affichées
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
admin.site.register(Season, SeasonAdmin)