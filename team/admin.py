from django.contrib import admin

from .models import Coachs, Conferences, Divisions, Superbowls, Teams

# Register your models here.
admin.site.register(Coachs)
admin.site.register(Divisions)
admin.site.register(Conferences)
admin.site.register(Superbowls)

class TeamsAdmin(admin.ModelAdmin):
    # Afficher des colonnes supplémentaires dans la liste des objets
    list_display = ('name', 'town', 'division', 'founded_year', 'colorOne', 'colorTwo')
    
    # Ajout d'un champ de recherche
    search_fields = ('name', 'town', 'stadium', 'division__name')
    
    # Ajout de filtres dans la barre latérale
    list_filter = ('division', 'founded', 'town')

    # Pagination (afficher 10 éléments par page)
    list_per_page = 8  
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'town', 'stadium', 'thumbnail')
        }),
        ('Historique', {
            'fields': ('founded', 'division')
        }),
        ('Couleurs de l\'équipe', {
            'fields': ('colorOne', 'colorTwo')
        }),
    )
    
    # Prévisualisation des images (si applicable)
    readonly_fields = ('thumbnail_preview',)

    def founded_year(self, obj):
        return obj.founded.year
    founded_year.short_description = "Année de fondation"

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" style="width: 50px; height: 50px;" />'
        return "Pas d'image"
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = "Aperçu du logo"

# Enregistrement du modèle et de l'admin personnalisé
admin.site.register(Teams, TeamsAdmin)
