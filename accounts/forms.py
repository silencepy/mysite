from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)


class Meta:
    model = User
    fields = ("username", "email")


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError("密码不匹配。")
    return cd['password2']
