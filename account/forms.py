from django import forms

class LoginForm(forms.Form):
    usermane = forms.CharField()
    passworld = forms.CharField(widget=forms.PasswordInput)
