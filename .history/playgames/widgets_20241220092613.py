from django import forms

from team.models import Teams

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
    def render_option(self, selected_choices, option_value, option_label):
        # Rendu personnalisé des options pour inclure l'image
        option = super().render_option(selected_choices, option_value, option_label)
        if option_value:  # Si l'équipe a une image
            team = Teams.objects.filter(id=option_value).first()
            if team and team.thumbnail:
                image_url = team.thumbnail.url
                option = f'<option value="{option_value}" data-image="{image_url}" {option_label} style="background-image: url({image_url}); padding-left: 40px;">' \
                         f'{option_label}</option>'
        return option

    def render(self, name, value, attrs=None, renderer=None):
        # Ajoutez la classe form-select au select
        if attrs is None:
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' form-select'
        return super().render(name, value, attrs, renderer)