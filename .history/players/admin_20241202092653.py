from django.contrib import admin

from players.models import PLayers, Player_position



class PlayersAdmin(admin.ModelAdmin):
    # Afficher des colonnes supplémentaires dans la liste des objets
    list_display = ('name', 'firstName','thumbnail', 'age','team', 'poste', 'actif', 'injury' )

    # Ajout d'un champ de recherche
    search_fields = ('name', 'firstName', 'team', 'poste')

    # Ajout de filtres dans la barre latérale
    list_filter = ('team', 'poste', 'actif', 'injury')

    # Pagination (afficher 10 éléments par page)
    list_per_page = 10  

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


class Player_positionAdmin(admin.ModelAdmin):
    # Afficher des colonnes supplémentaires dans la liste des objets
    list_display = ("name", "abrev")

    # Ajout d'un champ de recherche
    search_fields = ("name" "abrev")

    # Ajout de filtres dans la barre latérale
    list_filter = ('name', 'abrev')


# Enregistrement du modèle et de l'admin personnalisé
admin.site.register(PLayers, PlayersAdmin)
admin.site.register(Player_position, Player_positionAdmin)