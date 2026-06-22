from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable
from .forms import EmpathyMapForm


@login_required
def empathy_form_view(request):
    """Vista formulario Mapa de Empatía"""
    module = get_object_or_404(Module, key='empathy')
    
    if not hasattr(request.user, 'entrepreneur_profile'):
        messages.error(request, 'Solo emprendedores pueden acceder')
        return redirect('dashboard')
    
    progress, created = ModuleProgress.objects.get_or_create(
        user=request.user,
        module=module,
        defaults={'status': 'in_progress'}
    )
    
    # Cargar datos existentes
    initial_data = {}
    existing = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if existing and existing.data:
        initial_data = existing.data
    
    if request.method == 'POST':
        form = EmpathyMapForm(request.POST)
        if form.is_valid():
            # Marcar anteriores como no actuales
            TextDeliverable.objects.filter(
                user=request.user,
                module=module
            ).update(is_current=False)
            
            # Crear deliverable
            empathy_data = {
                'persona': form.cleaned_data['persona'],
                'piensa_siente': form.cleaned_data['piensa_siente'],
                've': form.cleaned_data['ve'],
                'dice_hace': form.cleaned_data['dice_hace'],
                'oye': form.cleaned_data['oye'],
                'frustraciones': form.cleaned_data['frustraciones'],
                'necesidades': form.cleaned_data['necesidades'],
                'pov': form.cleaned_data['pov']
            }
            
            TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=empathy_data,
                summary=form.cleaned_data['pov'],
                is_current=True,
                is_validated=True
            )
            
            # Completar módulo
            progress.completion_percentage = 100
            progress.status = 'completed'
            progress.save()
            
            messages.success(request, '¡Felicidades! Has completado el Mapa de Empatía')
            return redirect('dashboard')
    else:
        form = EmpathyMapForm(initial=initial_data)
    
    context = {
        'module': module,
        'progress': progress,
        'form': form,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/empathy/form.html', context)


@login_required
def empathy_view_completed(request):
    """Vista solo lectura"""
    module = get_object_or_404(Module, key='empathy')
    
    deliverable = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if not deliverable:
        messages.error(request, 'No has completado este módulo')
        return redirect('empathy:form')
    
    context = {
        'module': module,
        'data': deliverable.data
    }
    
    return render(request, 'modules/empathy/view.html', context)


@login_required
def empathy_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='empathy')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
