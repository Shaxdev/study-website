from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# 1-usul
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# 2-usul emailga habar jonatish
from django.core.mail import send_mail
from django.conf import settings

from . import models, forms

# Create your views here.


def profile_user_info(request):
    user = request.user         
    # user_info_objects = models.UserInfo.objects.all()
    try:
        user_info = models.UserInfo.objects.get(user=user)
        if user_info:
            form = forms.UserInfoForm(instance=user_info)
        else:
            form = forms.UserInfoForm()
    except:
        form = forms.UserInfoForm()
        user_info = ''
        
    if request.POST:
        if user_info:
            form = forms.UserInfoForm(request.POST, request.FILES, instance=user_info)
        else:
            form = forms.UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            
            form_data = form.cleaned_data
            user_info.user = user
            user_info.image = form_data['image']
            user_info.ism = form_data['ism']
            user_info.familya = form_data['familya']
            user_info.sharif = form_data['sharif']
            user_info.save()
            print('Form saved')
            
            
        else:
            print('Form validmas')
            print(form.errors)
     
    context = {
        'user_info': user_info,
        'form': form,
    }
    return render(request, 'dashboard_templates/profile/change_user_info.html', context)



def change_password(request):
    
    form = PasswordChangeForm(user=request.user)
    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_user_info')
        else:
            print('Error: ', form.errors)
    context = {
        'form': form
    }
    return render(request, 'dashboard_templates/profile/change_password.html', context)



def change_email(request):
    
    return render(request, 'dashboard_templates/profile/change_email.html')



def language_set(request):
    
    return render(request, 'dashboard_templates/profile/language_set.html')



# def change_email(request):
#     user = request.user
    
#     def email_code():
#         import random
#         import string
#         available_characters = string.ascii_letters + string.digits
#         code = ''
#         for i in range(8):
#             index = random.randint(0, len(available_characters)-1)
#             code += available_characters[index]  
#         return code
    
#     email_model = models.EmailCode()
    
    
#     form = forms.EmailForm()
#     if request.POST:
#         form = forms.EmailForm(request.POST)
#         if form.is_valid():
#             user_email = form.cleaned_data['email']
#             e_code = email_code() 
#             template = render_to_string('email_message.html' , {'code': e_code})
#             email = EmailMessage(
#                 'You have to enter this code... ',
#                 template,
#                 settings.EMAIL_HOST_USER,
#                 [user_email],
#             )
#             email.fail_silently = False
#             email.send()
            
#             email_model.user = request.user
#             email_model.code = e_code
#             email_model.save()
#             return redirect('change_email')
#     context = {
#         'form': form,
#         'user': user,
#     }
#     return render(request, 'dashboard_templates/profile/change_email.html', context)


def change_email(request):
    
    def email_code():
        import random
        import string
        available_characters = string.ascii_letters + string.digits
        code = ''
        for i in range(8):
            index = random.randint(0, len(available_characters)-1)
            code += available_characters[index]
            
           
        return code
    
    
    email_model = models.EmailCode()
    if request.POST:
        salom = 'Assalomu alaykum birodar'
        email = request.POST['email']
        code = email_code()
 
        send_mail(salom, code, settings.EMAIL_HOST_USER, ['shakx995@gmail.com'],
                fail_silently=False)
        
        succes = 'your message has been sent thank you..!'
        
    else:
        succes = ''
    
    return render(request, 'dashboard_templates/profile/change_email.html', {'secces': succes})