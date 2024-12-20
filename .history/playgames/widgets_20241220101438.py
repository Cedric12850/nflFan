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
        option = super().render_option(selected_choices, option_value, option_label)

        # Vérifiez que l'option a une valeur (si l'option existe)
        if option_value:
            team = Team.objects.filter(id=option_value).first()  # Récupère l'équipe par son ID
            if team:
                # Si l'équipe existe, récupère son logo et sa ville
                image_url = team.thumbnail.url if team.thumbnail else ''
                city_name = team.town
                team_name = team.name

                # Crée un texte à afficher dans l'option avec la ville et l'image
                option_label = f'{city_name} {team_name}'

                # Ajoute l'image dans le style background-image pour l'option
                # Le padding-left permet de donner un peu d'espace pour l'image
                option = f'<option value="{option_value}" data-image="{image_url}" ' \
                         f'style="background-image: url({image_url}); padding-left: 40px;">' \
                         f'{option_label}</option>'

        return option

    def render(self, name, value, attrs=None, renderer=None):
        # Ajoute la classe `form-select` au champ select pour l'intégration avec Bootstrap
        if attrs is None:
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' form-select'
        return super().render(name, value, attrs, renderer)