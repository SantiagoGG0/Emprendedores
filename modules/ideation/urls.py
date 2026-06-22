from django.urls import path
from . import views

app_name = 'ideation'

urlpatterns = [
    path('', views.ideation_form_view, name='form'),
    path('ver/', views.ideation_view_completed, name='view'),
    path('guia/', views.ideation_intro_view, name='intro'),
]
