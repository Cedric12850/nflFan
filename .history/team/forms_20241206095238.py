from django import forms

from team.fields import TeamChoiceField

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

class TeamSelectFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remplacez les champs de type équipe par le champ personnalisé
        for field_name in self.fields:
            if isinstance(self.fields[field_name], forms.ModelChoiceField) and self.fields[field_name].queryset.model == Teams:
                self.fields[field_name] = TeamChoiceField(queryset=Teams.objects.all())

class PlayGameAdminForm(TeamSelectFormMixin):
    class Meta:
        model = PlayGame
        fields = '__all__'