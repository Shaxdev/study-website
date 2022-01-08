from django.urls import path

from . import views

urlpatterns = [
    path('', views.dash_model, name='dash_model'), 
    path('inside_model/<int:pk>', views.inside_model_view, name='inside_model'),
    path('test/', views.test_view, name='test_view'),
]
