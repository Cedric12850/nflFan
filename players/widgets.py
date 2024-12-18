from django import forms

from team.models import Teams

class CustomWidgets:
    text_input = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Texte ici...'
    })
    number_input = forms.NumberInput(attrs={
        'class': 'form-control',
        'min': 0,
    })
    select_input = forms.Select(attrs={
        'class': 'form-select',
    })
    checkbox_input = forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    })
    textarea_input = forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
    })
    date_input = forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
    })
    
    file_input = forms.FileInput(attrs={
        'class': 'form-control-file',
    })

    @staticmethod
    def text_input_with_placeholder(placeholder):
        return forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': placeholder
        })
    