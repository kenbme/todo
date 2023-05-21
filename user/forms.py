from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    email = forms.EmailField(max_length=50)
