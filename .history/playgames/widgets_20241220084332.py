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
    
    # Forcer l'utilisation de l'ID numérique si "value" est un objet
    if isinstance(value, ModelChoiceIteratorValue):
        value = value.value  # Récupère l'ID réel de l'objet

    if value:  # Vérifie si la valeur existe
        try:
            team = self.choices.queryset.get(pk=value)  # Rechercher l'équipe
            if team and hasattr(team, 'thumbnail'):
                option['attrs']['data-image'] = team.thumbnail.url  # Ajoute le thumbnail
        except (ValueError, self.choices.queryset.model.DoesNotExist):
            pass  # Si l'équipe n'existe pas, ignorer
    return option