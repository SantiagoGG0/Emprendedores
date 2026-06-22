from django.urls import path
from . import views

app_name = 'value_prop'

urlpatterns = [
    path('', views.value_prop_form_view, name='form'),
    path('ver/', views.value_prop_view_completed, name='view'),
    path('guia/', views.value_prop_intro_view, name='intro'),
]
