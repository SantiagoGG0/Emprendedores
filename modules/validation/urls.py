from django.urls import path
from . import views

app_name = 'validation'

urlpatterns = [
    path('', views.validation_view, name='form'),
    path('completar/', views.validation_complete, name='complete'),
    path('ver/', views.validation_view_completed, name='view'),
    path('guia/', views.validation_intro_view, name='intro'),
]
