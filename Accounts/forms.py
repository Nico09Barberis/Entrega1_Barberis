import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCretionForm(UserCreationForm):
    
    username = forms.CharField(label='username', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir password', widget=forms.PasswordInput)
    
 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { key: '' for key in fields}


class MyUserEditForm(forms.Form):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='repetir password', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label='nombre', max_length=30, required=False)
    last_name = forms.CharField(label='apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)
    