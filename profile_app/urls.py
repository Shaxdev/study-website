from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
# app_name = 'profile_app'

urlpatterns = [
    path('', views.profile_user_info, name='profile_user_info'),
    path('change_password/', views.change_password, name='change_password'),
    
    path('change_email/', views.change_email, name='change_email'),
    path('language_set/', views.language_set, name='language_set'),
]
