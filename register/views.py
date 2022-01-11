from django.shortcuts import redirect, render
from .models import *

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request): 
    if request.user.is_authenticated:
        return redirect('auoth_index')   
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)     
            error = form.errors
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print('email: ', email,  '  password1: ', password1, '  password2: ', password2)
            print(error)
            if form.is_valid():
                form.save()
                messages.success(request, 'Acount was created for ' + email)
                print('Success')
                return redirect('login')
            else:
                print('Failing..')    
        else:
            form = CreateUserForm()     
            error = ''
        context = {
            'form': form, 
            'error': error
        }
        return render(request, 'auth_template/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('auoth_index')   
    else:
        if request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('auoth_index')
            else:
                messages.info(request, 'email or password is incorrect')             
        
    return render(request, 'auth_template/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


            
