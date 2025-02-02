from django.contrib import admin

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.

class WeekAdmin(admin.ModelAdmin):
    search_fields = ('week_number', 'season__name')  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('team_local', 'team_visitor', 'week',  'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('-played_at',)
    date_hierarchy = 'played_at'
    autocomplete_fields = ['week']
    # Pagination (afficher 16 éléments par page)
    list_per_page = 16

    # Spécifiez l'ordre des champs dans le formulaire
    fields = ['week','played_at',  'team_local', 'team_visitor', 'score_local', 'score_visitor']

class SuperbowlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'winner', 'teamOne', 'teamTwo', 'stadium', 'town')  # Colonnes affichées
    list_filter = ('year', 'winner', 'town')  # Filtres par année, gagnant, ville
    search_fields = ('name', 'stadium', 'winner__name')  # Recherche par nom, stade, gagnant
    ordering = ('-year',)  # Tri décroissant par année

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)
    ordering = ('start_date',)
    date_hierarchy = 'start_date'

    # Personnalisation de l'affichage de l'objet dans le formulaire d'administration
    def __str__(self):
        return f"Saison {self.name} ({self.start_date} - {self.end_date})"

admin.site.register(PlayGame, PlayGameAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Superbowls, SuperbowlsAdmin)
admin.site.register(Season, SeasonAdmin)