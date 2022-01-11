# from django
from django import forms
# from django.contrib.auth.models import User
from account.models import User
from django.forms import fields
from django.forms.models import fields_for_model

# from apps
from . import models
        
class UserInfoForm(forms.ModelForm):   
    class Meta:
        model = models.UserInfo
        fields = ['ism', 'familya', 'sharif', 'image' ]


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']