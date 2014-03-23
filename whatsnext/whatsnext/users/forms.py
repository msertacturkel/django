from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        widgets = {
        'password': forms.PasswordInput(),
        }
