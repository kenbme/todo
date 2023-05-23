from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def is_valid(self):
        valid = super().is_valid()
        if self.already_registered():
            valid = False
            self.add_error(None, "Username or Email already registered.")
        return valid

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data.get("username"),
            password=self.cleaned_data.get("password"),
            email=self.cleaned_data.get("email"),
        )

    # AUX
    def already_registered(self):
        return (
            User.objects.filter(username=self.data.get("username")).exists()
            or User.objects.filter(email=self.data.get("email")).exists()
        )
