from django import forms
from django.core.exceptions import ValidationError
import re

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, label='Номер телефона')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^89\d{9}$', phone):
            raise ValidationError('Введите номер телефона в формате 8-9...')
        return phone