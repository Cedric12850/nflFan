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
        # Appel à la méthode de rendu standard de l'option
        option = super().render_option(selected_choices, option_value, option_label)

        # Si l'option a une valeur (c'est-à-dire une équipe)
        if option_value:
            team = Team.objects.filter(id=option_value).first()  # Récupère l'équipe par son ID
            if team and team.thumbnail:
                # Ajoute l'URL de l'image et la ville dans l'attribut `data-image`
                image_url = team.thumbnail.url
                option_label = f"{team.town} {team.name}"  # Ajout du nom de la ville avant l'équipe
                option = f'<option value="{option_value}" data-image="{image_url}" ' \
                         f'style="background-image: url({image_url}); padding-left: 40px;">' \
                         f'{option_label}</option>'

        return option

    def render(self, name, value, attrs=None, renderer=None):
        # Ajoute la classe `form-select` au champ select
        if attrs is None:
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' form-select'
        return super().render(name, value, attrs, renderer)