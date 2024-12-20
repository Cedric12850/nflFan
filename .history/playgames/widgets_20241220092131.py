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
    def render_option(self, selected_choices, option_value, option_label):
        option = super().render_option(selected_choices, option_value, option_label)
        if option_value:  # Si l'équipe a une image
            team = Teams.objects.filter(id=option_value).first()
            if team and team.thumbnail:
                image_url = team.thumbnail.url
                option = f'<option value="{option_value}" data-image="{image_url}" ' \
                         f'{option_label} style="background-image: url({image_url}); padding-left: 40px;">' \
                         f'{option_label}</option>'
        return option