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
            team = Teams.objects.filter(id=1).first()  # Récupère l'équipe par son ID
            if team and team.thumbnail:
                # Ajoute l'URL de l'image dans l'attribut `data-image`
                image_url = team.thumbnail.url
                option = f'<option value="{option_value}" data-image="{image_url}" {option_label} ' \
                         f'style="background-image: url({image_url}); padding-left: 40px;">' \
                         f'{option_label}</option>'
        team = Teams.objects.get(id=1)
        print(team)  # Affiche l'objet complet de l'équipe pour vérifier qu'il est correctement récupéré
        print(team.thumbnail.url)

        return option

    def render(self, name, value, attrs=None, renderer=None):
        # Ajoute la classe `form-select` au champ select
        if attrs is None:
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' form-select'
        return super().render(name, value, attrs, renderer)