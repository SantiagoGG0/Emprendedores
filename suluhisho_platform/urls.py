"""
URL configuration for suluhisho_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    home_view, dashboard_view, 
    glossary_modal_view, glossary_search_view, glossary_full_view,
    admin_dashboard_view, venture_create_view, venture_update_view, venture_associate_view
)
from entrepreneurs.views import login_view, logout_view, register_view

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Auth
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', register_view, name='register'),
    
    # Home y Dashboard
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
    # Base de Conocimiento (Glosario)
    path('glosario/', glossary_full_view, name='glossary_full'),
    path('glosario/modal/<str:key>/', glossary_modal_view, name='glossary_modal'),
    path('glosario/buscar/', glossary_search_view, name='glossary_search'),
    
    # Módulos
    path('modulos/ikigai/', include('modules.ikigai.urls')),
    path('modulos/diario-campo/', include('modules.field_diary.urls')),
    path('modulos/empatía/', include('modules.empathy.urls')),
    path('modulos/jtbd/', include('modules.jtbd.urls')),
    path('modulos/ideacion/', include('modules.ideation.urls')),
    path('modulos/propuesta-valor/', include('modules.value_prop.urls')),
    path('modulos/validacion/', include('modules.validation.urls')),
    
    # Admin Dashboard (NO es /admin/ de Django)
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('admin-dashboard/emprendimientos/crear/', venture_create_view, name='venture_create'),
    path('admin-dashboard/emprendimientos/<int:venture_id>/editar/', venture_update_view, name='venture_update'),
    path('admin-dashboard/emprendimientos/<int:venture_id>/asociar/', venture_associate_view, name='venture_associate'),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
