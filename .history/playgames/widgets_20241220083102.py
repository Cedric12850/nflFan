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
        if value:  # Ajoute l'URL du thumbnail pour chaque équipe
            team = self.choices.queryset.filter(pk=value).first()
            if team:
                option['attrs']['data-image'] = team.thumbnail.url
        return option