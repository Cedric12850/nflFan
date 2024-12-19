from django import forms


class CustomWidgets:
    text_input = forms.TextInput(attrs={
        'class': 'form-control',
    })
    mail_input = forms.EmailInput(attrs={
        'class': 'form-control',
    })
    password_input = forms.PasswordInput(attrs={
        'class': 'form-control',
    })

    @staticmethod
    def text_input_with_placeholder(placeholder):
        return forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': placeholder
        })
