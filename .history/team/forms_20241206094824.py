from django import forms

from .models import Team

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
            if isinstance(self.fields[field_name], forms.ModelChoiceField) and self.fields[field_name].queryset.model == Team:
                self.fields[field_name] = TeamChoiceField(queryset=Team.objects.all())