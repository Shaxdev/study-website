from account.forms import UserRegisterForm, UserLoginForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.contrib import messages


from .models import User



def register_view(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            p1 = form.cleaned_data['password1']
            p2 = form.cleaned_data['password2']
            if p1 == p2:
                form.save()
                print("ishladi-registratsiya")
                return redirect(reverse('auoth_index'))
            else:
                messages.error(request, 'Пароли должны быть одинаковыми!')
                return redirect(reverse('register-view'))
        else:
            messages.error(request, 'Email mavjud!!!')
            return redirect(reverse('register-view'))
    context = {
        "form":form
    }
    return render(request, 'auth_template/register.html', context)


def login_view(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user=user)
                return redirect(reverse("auoth_index"))
            else:
                messages.error(request, 'Данные введены неверно, проверьте и введите заново')
                # next_page = request.GET.get("next", None)
                # if next_page:
                #     return redirect(next_page)
                # else:
                #     return redirect(reverse("home"))
                    
    context = {
        "form": form
    }
    return render(request, 'auth_template/login.html', context)


# def account_logout(request):
#     if request.method == "POST":
#         logout(request)

#     return redirect(reverse("account-login"))