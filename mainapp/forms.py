from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)