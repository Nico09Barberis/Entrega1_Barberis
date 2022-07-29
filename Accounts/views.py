from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import MyUserCretionForm

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
           
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                
                return render(request, 'index.html', {})
                
            else:
                return render(request, 'accounts/login.html', {'form': form})
            
        else:
            return render(request, 'accounts/login.html', {'form': form})
        
    form = AuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
   
    if request.method == 'POST':
        form = MyUserCretionForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
        else:
            return render(request, 'accounts/register.html', {'form': form})
           
    form = MyUserCretionForm()
    return render(request, 'accounts/register.html', {'form': form})
    
    