from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
import json

from core.models import Module, ModuleProgress, ReferenceContent, Venture, Investment, VentureEntrepreneur
from core.decorators import user_type_required

User = get_user_model()


@login_required
def dashboard_view(request):
    """Dashboard principal - redirige según tipo de usuario"""
    
    user = request.user
    
    # Redirigir según tipo de usuario
    if user.user_type in ['admin', 'ally']:
        return redirect('admin_dashboard')
    elif hasattr(user, 'entrepreneur_profile'):
        return entrepreneur_dashboard(request)
    elif hasattr(user, 'facilitator_profile'):
        return facilitator_dashboard(request)
    else:
        # Admin o usuario sin perfil
        return redirect('/admin/')


def entrepreneur_dashboard(request):
    """Dashboard para emprendedores"""
    
    user = request.user
    
    # Obtener todos los módulos ordenados
    modules = Module.objects.filter(is_active=True).order_by('order')
    
    # Iconos por módulo
    module_icons = {
        'ikigai': '🎯',
        'field_diary': '📔',
        'empathy': '❤️',
        'jtbd': '🎯',
        'ideation': '💡',
        'value_prop': '🎁',
        'validation': '✅'
    }
    
    # Preparar datos de cada módulo con su progreso
    modules_data = []
    completed_count = 0
    
    for idx, module in enumerate(modules):
        # Obtener progreso del usuario para este módulo
        progress, _ = ModuleProgress.objects.get_or_create(
            user=user,
            module=module,
            defaults={'status': 'not_started', 'completion_percentage': 0}
        )
        
        # Determinar si está bloqueado (debe completar el anterior)
        is_locked = False
        if idx > 0:
            prev_module = modules[idx - 1]
            prev_progress = ModuleProgress.objects.filter(
                user=user,
                module=prev_module
            ).first()
            
            if not prev_progress or prev_progress.status != 'completed':
                is_locked = True
        
        # Contar completados
        if progress.status == 'completed':
            completed_count += 1
        
        # URLs según el módulo
        from django.urls import reverse
        
        form_url = None
        view_url = None
        
        if module.key == 'ikigai':
            form_url = reverse('ikigai:form')
            view_url = reverse('ikigai:view')
        elif module.key == 'field_diary':
            form_url = reverse('field_diary:form')
            view_url = reverse('field_diary:view')
        elif module.key == 'empathy':
            form_url = reverse('empathy:form')
            view_url = reverse('empathy:view')
        elif module.key == 'jtbd':
            form_url = reverse('jtbd:form')
            view_url = reverse('jtbd:view')
        elif module.key == 'ideation':
            form_url = reverse('ideation:form')
            view_url = reverse('ideation:view')
        elif module.key == 'value_prop':
            form_url = reverse('value_prop:form')
            view_url = reverse('value_prop:view')
        elif module.key == 'validation':
            form_url = reverse('validation:form')
            view_url = reverse('validation:view')
        
        modules_data.append({
            'module': module,
            'progress': progress,
            'icon': module_icons.get(module.key, '📝'),
            'is_locked': is_locked,
            'form_url': form_url,
            'view_url': view_url
        })
    
    # Calcular progreso general
    total_modules = len(modules)
    overall_progress = int((completed_count / total_modules) * 100) if total_modules > 0 else 0
    
    context = {
        'modules': modules_data,
        'overall_progress': overall_progress,
        'completed_modules': completed_count,
    }
    
    return render(request, 'dashboard/entrepreneur.html', context)


def facilitator_dashboard(request):
    """Dashboard para facilitadores (por implementar)"""
    
    # TODO: Implementar dashboard de facilitador
    # - Lista de emprendedores asignados
    # - Progreso de cada uno
    # - Alertas de entregables pendientes de validar
    
    context = {
        'message': 'Dashboard de facilitador - próximamente'
    }
    
    return render(request, 'dashboard/facilitator.html', context)


def home_view(request):
    """Landing page o redirect a dashboard si está autenticado"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request, 'home.html')


# =====================================================
# VISTAS DE GLOSARIO (Base de Conocimiento)
# =====================================================

@login_required
def glossary_modal_view(request, key):
    """Vista modal HTMX - retorna HTML parcial con detalles de término"""
    
    term = get_object_or_404(ReferenceContent, key=key, is_active=True)
    
    # Renderizar solo el contenido del modal (sin layout base)
    return render(request, 'includes/glossary_modal.html', {
        'term': term
    })


@login_required
def glossary_search_view(request):
    """API HTMX para búsqueda de términos (sidebar ayuda)"""
    
    query = request.GET.get('q', '').strip()
    module_key = request.GET.get('module', None)
    
    # Filtrar términos activos
    terms = ReferenceContent.objects.filter(is_active=True)
    
    # Búsqueda por texto
    if query:
        terms = terms.filter(
            Q(title__icontains=query) |
            Q(short_definition__icontains=query) |
            Q(keywords__icontains=query)
        )
    
    # Filtrar por módulo si viene de un módulo específico
    if module_key:
        try:
            module = Module.objects.get(key=module_key)
            terms = terms.filter(related_modules=module)
        except Module.DoesNotExist:
            pass
    
    # Limitar a 5 resultados
    terms = terms.order_by('order')[:5]
    
    # Retornar HTML parcial con lista de resultados
    return render(request, 'includes/glossary_search_results.html', {
        'terms': terms,
        'query': query
    })


@login_required
def glossary_full_view(request):
    """Página completa de glosario con tabs (metodología, territorial, plataforma)"""
    
    # Obtener términos por categoría
    methodology_terms = ReferenceContent.objects.filter(
        category='methodology',
        is_active=True
    ).order_by('order')
    
    territorial_terms = ReferenceContent.objects.filter(
        category='territorial',
        is_active=True
    ).order_by('order')
    
    platform_terms = ReferenceContent.objects.filter(
        category='platform',
        is_active=True
    ).order_by('order')
    
    context = {
        'methodology_terms': methodology_terms,
        'territorial_terms': territorial_terms,
        'platform_terms': platform_terms,
    }
    
    return render(request, 'knowledge_base/glossary.html', context)


# ========================
# Admin Dashboard Views
# ========================

@login_required
@user_type_required('admin', 'ally')
def admin_dashboard_view(request):
    """Dashboard administrativo con métricas y gestión de emprendimientos."""
    
    # Métricas principales
    total_ventures = Venture.objects.count()
    total_entrepreneurs = User.objects.filter(user_type='entrepreneur').count()
    total_allies = User.objects.filter(user_type='ally').count()
    total_clients = User.objects.filter(user_type='client').count()
    total_investment = Investment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Ventures por estado
    ventures_by_status = Venture.objects.values('status').annotate(count=Count('id'))
    status_data = {item['status']: item['count'] for item in ventures_by_status}
    
    # Usuarios por rol para gráfico
    users_by_role_data = [
        {'role': 'Admin', 'count': User.objects.filter(user_type='admin').count()},
        {'role': 'Aliado', 'count': total_allies},
        {'role': 'Cliente', 'count': total_clients},
        {'role': 'Emprendedor', 'count': total_entrepreneurs},
    ]
    users_by_role_json = json.dumps(users_by_role_data)
    
    # Ventures por estado para gráfico
    ventures_status_labels = []
    ventures_status_counts = []
    status_map = {
        'diagnostic': 'Diagnóstico',
        'active': 'Activo',
        'paused': 'Pausado',
        'completed': 'Completado'
    }
    for status_key in ['diagnostic', 'active', 'paused', 'completed']:
        ventures_status_labels.append(status_map.get(status_key, status_key))
        ventures_status_counts.append(status_data.get(status_key, 0))
    
    ventures_status_json = json.dumps({
        'labels': ventures_status_labels,
        'data': ventures_status_counts
    })
    
    # Ventures recientes
    recent_ventures = Venture.objects.select_related('created_by').prefetch_related(
        'ventureentrepreneur_set__entrepreneur'
    ).order_by('-created_at')[:10]
    
    # Agregar datos calculados a ventures
    for venture in recent_ventures:
        venture.entrepreneurs_count = venture.ventureentrepreneur_set.count()
        venture.completion = venture.get_completion_percentage()
    
    context = {
        'total_ventures': total_ventures,
        'total_entrepreneurs': total_entrepreneurs,
        'total_allies': total_allies,
        'total_clients': total_clients,
        'total_investment': total_investment,
        'users_by_role_json': users_by_role_json,
        'ventures_status_json': ventures_status_json,
        'recent_ventures': recent_ventures,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)


@login_required
@user_type_required('admin')
def venture_create_view(request):
    """Crear nuevo emprendimiento."""
    from entrepreneurs.forms import VentureForm
    
    if request.method == 'POST':
        form = VentureForm(request.POST)
        if form.is_valid():
            venture = form.save(commit=False)
            venture.created_by = request.user
            venture.save()
            messages.success(request, f'Emprendimiento "{venture.name}" creado exitosamente.')
            return redirect('admin_dashboard')
    else:
        form = VentureForm()
    
    return render(request, 'admin_dashboard/venture_form.html', {'form': form})


@login_required
@user_type_required('admin')
def venture_update_view(request, venture_id):
    """Actualizar emprendimiento existente."""
    from entrepreneurs.forms import VentureForm
    
    venture = get_object_or_404(Venture, id=venture_id)
    
    if request.method == 'POST':
        form = VentureForm(request.POST, instance=venture)
        if form.is_valid():
            form.save()
            messages.success(request, f'Emprendimiento "{venture.name}" actualizado.')
            return redirect('admin_dashboard')
    else:
        form = VentureForm(instance=venture)
    
    return render(request, 'admin_dashboard/venture_form.html', {'form': form, 'venture': venture})


@login_required
@user_type_required('admin')
def venture_associate_view(request, venture_id):
    """Asociar entrepreneurs, allies o clients a un emprendimiento."""
    venture = get_object_or_404(Venture, id=venture_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_entrepreneur':
            entrepreneur_id = request.POST.get('entrepreneur_id')
            role = request.POST.get('role', 'member')
            entrepreneur = get_object_or_404(User, id=entrepreneur_id, user_type='entrepreneur')
            
            VentureEntrepreneur.objects.get_or_create(
                venture=venture,
                entrepreneur=entrepreneur,
                defaults={'role': role}
            )
            messages.success(request, f'{entrepreneur.get_full_name()} agregado al emprendimiento.')
        
        elif action == 'add_investment':
            client_id = request.POST.get('client_id')
            amount = request.POST.get('amount')
            client = get_object_or_404(Client, id=client_id)
            
            Investment.objects.create(
                venture=venture,
                client=client,
                amount=amount
            )
            
            # Actualizar total_investment del venture
            venture.total_investment = Investment.objects.filter(venture=venture).aggregate(
                Sum('amount')
            )['amount__sum'] or 0
            venture.save()
            
            messages.success(request, f'Inversión de ${amount} registrada.')
        
        return redirect('venture_associate', venture_id=venture_id)
    
    # GET request - mostrar formulario
    entrepreneurs = User.objects.filter(user_type='entrepreneur')
    from core.models import Client
    clients = Client.objects.select_related('user').all()
    
    venture_entrepreneurs = venture.ventureentrepreneur_set.select_related('entrepreneur').all()
    investments = Investment.objects.filter(venture=venture).select_related('client').order_by('-date')
    
    context = {
        'venture': venture,
        'entrepreneurs': entrepreneurs,
        'clients': clients,
        'venture_entrepreneurs': venture_entrepreneurs,
        'investments': investments,
    }
    
    return render(request, 'admin_dashboard/venture_associate.html', context)
