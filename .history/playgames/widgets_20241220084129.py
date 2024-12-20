from django import forms

class CustomWidgets:
    select_input = forms.Select(attrs={
        'class': 'form-select',
    })
    integer_input = forms.NumberInput(attrs={
        'class': 'form-control',
        'min': 0,
    })
    date_input = forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
    })

class TeamSelectWidget(forms.Select):
    template_name = "widgets/team_select_widget.html"

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value:  # Vérifier que la valeur existe
            try:
                # Récupérer l'équipe en fonction de l'identifiant
                team = self.choices.queryset.get(pk=value)
                if team and hasattr(team, 'thumbnail'):  # Ajouter la vérification pour éviter les erreurs
                    option['attrs']['data-image'] = team.thumbnail.url
            except (ValueError, self.choices.queryset.model.DoesNotExist):
                pass  # Si l'équipe n'existe pas, ignorer
        return option