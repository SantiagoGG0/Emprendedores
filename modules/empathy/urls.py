from django.urls import path
from . import views

app_name = 'empathy'

urlpatterns = [
    path('', views.empathy_form_view, name='form'),
    path('ver/', views.empathy_view_completed, name='view'),
    path('guia/', views.empathy_intro_view, name='intro'),
]
