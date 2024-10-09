from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']