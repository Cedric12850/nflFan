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
        # Appel à la méthode de rendu standard pour l'option
        option = super().render_option(selected_choices, option_value, option_label)

        # Si l'option a une valeur, alors récupérez les informations de l'équipe
        if option_value:
            team = Teams.objects.filter(id=option_value).first()  # Récupère l'équipe par son ID
            if team:
                # Si l'équipe existe, récupère son logo et sa ville
                image_url = team.thumbnail.url if team.thumbnail else ''
                city_name = team.town
                team_name = team.name

                # Création de l'élément <img> avec l'image et affichage du nom de la ville et de l'équipe
                if image_url:
                    # Création d'un élément <img> pour l'afficher dans l'option
                    img_tag = f'<img src="{image_url}" alt="{team_name}" style="width: 20px; margin-right: 10px;">'
                else:
                    img_tag = ''  # Pas d'image, on n'ajoute rien

                # L'option affichera d'abord l'image, puis le nom de la ville et de l'équipe
                option = f'<option value="{option_value}" {option_label}>' \
                         f'{img_tag} {city_name} {team_name}</option>'

        return option

    def render(self, name, value, attrs=None, renderer=None):
        # Ajoute la classe `form-select` au champ select pour l'intégration avec Bootstrap
        if attrs is None:
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' form-select'
        return super().render(name, value, attrs, renderer)