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

class TeamGroupedSelect(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        divisions = {}
        for team in Teams.objects.select_related('division').order_by('division__name', 'name'):
            divisions.setdefault(team.division.name, []).append((team.id, team.name))
        
        return [
            (division, teams) for division, teams in divisions.items()
        ]

class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__(queryset=queryset, widget=TeamGroupedSelect, *args, **kwargs)

class TeamSelectFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assurez-vous que ce champ est bien modifié par le formulaire personnalisé
        for field_name in self.fields:
            if isinstance(self.fields[field_name], forms.ModelChoiceField) and self.fields[field_name].queryset.model == Teams:
                self.fields[field_name] = TeamChoiceField(queryset=Teams.objects.all())