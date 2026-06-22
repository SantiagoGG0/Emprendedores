from django.urls import path
from . import views

app_name = 'field_diary'

urlpatterns = [
    path('', views.field_diary_view, name='form'),
    path('completar/', views.field_diary_complete, name='complete'),
    path('ver/', views.field_diary_view_completed, name='view'),
    path('guia/', views.field_diary_intro_view, name='intro'),
]
