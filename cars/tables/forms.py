from django import forms

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, label='Номер телефона')