from django import forms


class LoginForm(forms.Form):
    """Форма лоигна (dont use)"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)