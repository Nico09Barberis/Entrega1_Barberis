from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCretionForm(UserCreationForm):
    
    username = forms.CharField(label='username', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir password', widget=forms.PasswordInput)
    
    first_name = forms.CharField(label='nombre', max_length=30)
    last_name = forms.CharField(label='apellido', max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = { key: '' for key in fields}