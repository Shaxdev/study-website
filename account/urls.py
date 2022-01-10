from django import urls
from django.http.request import validate_host
from django.urls import path


from . import views


urlpatterns = [
    path('register/', views.register_view, name='register-view'),
    path('login/', views.login_view, name='login-view'),
]