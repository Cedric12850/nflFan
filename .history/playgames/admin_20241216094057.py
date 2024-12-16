from django import forms
from django.contrib import admin

from playgames.models import PlayGame, Season, Superbowls, Week
# Register your models here.

class PlayGameForm(forms.ModelForm):
     # Champ virtuel pour sélectionner une saison
    season = forms.ModelChoiceField(
        queryset=Season.objects.all(),
        required=False,
        label="Saison",
        widget=forms.Select(attrs={"id": "id_season"})
    )

    class Meta:
        model = PlayGame
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Préremplir la liste des semaines en fonction de l'objet actuel ou vide
        if 'season' in self.data:  # Si la saison est sélectionnée dans le formulaire
            try:
                season_id = int(self.data.get('season'))
                self.fields['week'].queryset = Week.objects.filter(season_id=season_id)
            except (ValueError, TypeError):
                self.fields['week'].queryset = Week.objects.none()
        elif self.instance.pk:  # Si l'objet existe déjà (édition)
            self.fields['week'].queryset = Week.objects.filter(season=self.instance.week.season)
        else:  # Nouvel objet
            self.fields['week'].queryset = Week.objects.none()

class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin/js/playgame_admin.js',)

    form = PlayGameForm
    list_display = ('team_local', 'team_visitor', 'week', 'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('-played_at',)
    date_hierarchy = 'played_at'
    list_per_page = 16

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'week':
            if request.POST.get('season'):
                kwargs["queryset"] = Week.objects.filter(season_id=request.POST.get('season'))
            else:
                kwargs["queryset"] = Week.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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