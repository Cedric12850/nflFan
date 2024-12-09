from django.contrib import admin

from playgames.models import PlayGame
from team.forms import PlayGameForm

from .models import Coachs, Conferences, Divisions, Stadium, Superbowls, Teams

# Register your models here.
admin.site.register(Divisions)
admin.site.register(Conferences)
admin.site.register(Superbowls)

class TeamsAdmin(admin.ModelAdmin):
    # Afficher des colonnes supplémentaires dans la liste des objets
    list_display = ('name', 'town', 'division','owner', 'founded_year', 'stadium', 'colorOne', 'colorTwo')
    
    # Ajout d'un champ de recherche
    search_fields = ('name', 'town', 'stadium', 'division__name')
    
    # Ajout de filtres dans la barre latérale
    list_filter = ('division', )

    # Pagination (afficher 10 éléments par page)
    list_per_page = 8  
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'town', 'stadium', 'thumbnail')
        }),
        ('Historique', {
            'fields': ('owner', 'founded', 'division')
        }),
        ('Couleurs de l\'équipe', {
            'fields': ('colorOne', 'colorTwo')
        }),
    )
    
    # Prévisualisation des images (si applicable)
    readonly_fields = ('thumbnail_preview',)

    def founded_year(self, obj):
        return obj.founded.year
    

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" style="width: 50px; height: 50px;" />'
        return "Pas d'image"
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = "Aperçu du logo"

class CoachsAdmin(admin.ModelAdmin):
    # Afficher des colonnes supplémentaires dans la liste des objets
    list_display = ('name', 'firstName', 'team','poste', 'thumbnail', 'actif')
    
    # Ajout d'un champ de recherche
    search_fields = ('name', 'firstName', 'actif')
    
    # Ajout de filtres dans la barre latérale
    list_filter = ('actif', 'poste' )

    # Pagination (afficher 10 éléments par page)
    list_per_page = 8  
    
    
    # Prévisualisation des images (si applicable)
    readonly_fields = ('thumbnail_preview',)
    
    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" style="width: 50px; height: 50px;" />'
        return "Pas d'image"
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = "Aperçu du logo"

class StadiumAdmin(admin.ModelAdmin):
    list_display = ("name", "town", 'state', "capacity", 'creation_year', 'thumbnail', 'toiture')
    search_fields = ('toiture', 'town')
    list_filter = ('name', 'toiture')
    list_per_page = 10

    def creation_year(self, obj):
        return obj.creation.year
    creation_year.short_description = "Année de création"
    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" style="width: 50px; height: 50px;" />'
        return "Pas d'image"
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = "Aperçu du stade"

class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('team_local', 'score_local', 'team_visitor', 'score_visitor')
    search_fields = ('team_local','team_visitor')
    list_filter = ('team_local','team_visitor')
    list_per_page = 10
    form = PlayGameForm

# Enregistrement du modèle et de l'admin personnalisé
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Coachs,CoachsAdmin)
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(PlayGame, PlayGameAdmin)
