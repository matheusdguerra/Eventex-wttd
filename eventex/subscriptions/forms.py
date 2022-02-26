from django.core.exceptions import ValidationError
from django import forms


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve coter apenas números!', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve coter 11 números!', 'lenghf')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data
