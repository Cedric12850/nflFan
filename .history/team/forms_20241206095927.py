from django import forms


from .models import PlayGame, Teams

class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = [
            'name',
            'town',
            'stadium',
            'division',
            'owner',
            'founded',
            'thumbnail',
            'colorOne',
            'colorTwo'
        ]
        widgets = {'founded': forms.SelectDateWidget(years=range(1920, 2024))}

# 1. Widget personnalisé
class TeamGroupedSelect(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        # Group teams by division
        divisions = {}
        for team in Teams.objects.select_related('division').order_by('division__name', 'name'):
            divisions.setdefault(team.division.name, []).append((team.id, team.name))
        
        return [
            (division, teams) for division, teams in divisions.items()
        ]

# 2. Champ personnalisé
class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__(queryset=queryset, widget=TeamGroupedSelect, *args, **kwargs)

# 3. Mixin pour les formulaires d'admin
class TeamSelectFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remplacez les champs de type équipe par le champ personnalisé
        for field_name in self.fields:
            if isinstance(self.fields[field_name], forms.ModelChoiceField) and self.fields[field_name].queryset.model == Team:
                self.fields[field_name] = TeamChoiceField(queryset=Teams.objects.all())