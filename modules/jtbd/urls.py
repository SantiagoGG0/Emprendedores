from django.urls import path
from . import views

app_name = 'jtbd'

urlpatterns = [
    path('', views.jtbd_form_view, name='form'),
    path('ver/', views.jtbd_view_completed, name='view'),
    path('guia/', views.jtbd_intro_view, name='intro'),
]
