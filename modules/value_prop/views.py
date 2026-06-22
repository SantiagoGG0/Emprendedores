from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable
from .forms import ValuePropForm


@login_required
def value_prop_form_view(request):
    module = get_object_or_404(Module, key='value_prop')
    
    if not hasattr(request.user, 'entrepreneur_profile'):
        messages.error(request, 'Solo emprendedores pueden acceder')
        return redirect('dashboard')
    
    progress, created = ModuleProgress.objects.get_or_create(
        user=request.user,
        module=module,
        defaults={'status': 'in_progress'}
    )
    
    initial_data = {}
    existing = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if existing and existing.data:
        initial_data = existing.data
    
    if request.method == 'POST':
        form = ValuePropForm(request.POST)
        if form.is_valid():
            TextDeliverable.objects.filter(
                user=request.user,
                module=module
            ).update(is_current=False)
            
            value_prop_data = {
                'frustraciones': [
                    form.cleaned_data['frustracion_1'],
                    form.cleaned_data['frustracion_2'],
                    form.cleaned_data['frustracion_3']
                ],
                'ganancias': [
                    form.cleaned_data['ganancia_1'],
                    form.cleaned_data['ganancia_2'],
                    form.cleaned_data['ganancia_3']
                ],
                'productos': [
                    form.cleaned_data['producto_1'],
                    form.cleaned_data['producto_2']
                ],
                'aliviadores': [
                    form.cleaned_data['aliviador_1'],
                    form.cleaned_data['aliviador_2']
                ],
                'creadores': [
                    form.cleaned_data['creador_1'],
                    form.cleaned_data['creador_2']
                ],
                'propuesta_valor': form.cleaned_data['propuesta_valor']
            }
            
            TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=value_prop_data,
                summary=form.cleaned_data['propuesta_valor'],
                is_current=True,
                is_validated=True
            )
            
            progress.completion_percentage = 100
            progress.status = 'completed'
            progress.save()
            
            messages.success(request, '¡Felicidades! Has completado la Propuesta de Valor')
            return redirect('dashboard')
    else:
        form = ValuePropForm(initial=initial_data)
    
    context = {
        'module': module,
        'progress': progress,
        'form': form,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/value_prop/form.html', context)


@login_required
def value_prop_view_completed(request):
    module = get_object_or_404(Module, key='value_prop')
    
    deliverable = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if not deliverable:
        messages.error(request, 'No has completado este módulo')
        return redirect('value_prop:form')
    
    context = {
        'module': module,
        'data': deliverable.data
    }
    
    return render(request, 'modules/value_prop/view.html', context)


@login_required
def value_prop_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='value_prop')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
