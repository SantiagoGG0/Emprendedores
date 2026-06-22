from django.urls import path
from . import views

app_name = 'ikigai'

urlpatterns = [
    path('', views.ikigai_form_view, name='form'),
    path('ver/', views.ikigai_view_view, name='view'),
    path('guia/', views.ikigai_intro_view, name='intro'),
]
