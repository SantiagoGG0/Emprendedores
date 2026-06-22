from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable
from .forms import ValidationEntryForm


@login_required
def validation_view(request):
    """Vista principal validación - múltiples entrevistas"""
    module = get_object_or_404(Module, key='validation')
    
    if not hasattr(request.user, 'entrepreneur_profile'):
        messages.error(request, 'Solo emprendedores pueden acceder')
        return redirect('dashboard')
    
    progress, created = ModuleProgress.objects.get_or_create(
        user=request.user,
        module=module
    )
    
    if created or progress.status == 'not_started':
        progress.status = 'in_progress'
        progress.save()
    
    # Obtener entradas existentes
    entries = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).order_by('created_at')
    
    entries_data = [entry.data for entry in entries]
    
    if request.method == 'POST':
        form = ValidationEntryForm(request.POST)
        if form.is_valid():
            entry_data = {
                'entrevistado': form.cleaned_data['entrevistado'],
                'pregunta_problema': form.cleaned_data['pregunta_problema'],
                'solucion_actual': form.cleaned_data['solucion_actual'],
                'reaccion_idea': form.cleaned_data['reaccion_idea'],
                'pagaria': form.cleaned_data['pagaria'],
                'precio_sugerido': form.cleaned_data.get('precio_sugerido', ''),
                'aprendizajes': form.cleaned_data['aprendizajes']
            }
            
            TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=entry_data
            )
            
            # Actualizar progreso
            total_entries = entries.count() + 1
            progress.completion_percentage = min(int((total_entries / 3) * 100), 100)
            progress.save()
            
            messages.success(request, f'Entrevista {total_entries} guardada. {"¡Ya puedes completar!" if total_entries >= 3 else f"Necesitas {3 - total_entries} más."}')
            return redirect('validation:form')
    else:
        form = ValidationEntryForm()
    
    context = {
        'module': module,
        'progress': progress,
        'form': form,
        'entries': entries_data,
        'entries_count': len(entries_data),
        'can_complete': len(entries_data) >= 3,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/validation/form.html', context)


@login_required
def validation_complete(request):
    """Completar módulo"""
    if request.method != 'POST':
        return redirect('validation:form')
    
    module = get_object_or_404(Module, key='validation')
    
    entries_count = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).count()
    
    if entries_count < 3:
        messages.error(request, f'Necesitas al menos 3 entrevistas. Tienes {entries_count}.')
        return redirect('validation:form')
    
    progress = ModuleProgress.objects.get(
        user=request.user,
        module=module
    )
    progress.status = 'completed'
    progress.completion_percentage = 100
    progress.save()
    
    messages.success(request, '¡Felicidades! Has completado la Validación')
    return redirect('dashboard')


@login_required
def validation_view_completed(request):
    """Vista solo lectura"""
    module = get_object_or_404(Module, key='validation')
    
    entries = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).order_by('created_at')
    
    entries_data = [entry.data for entry in entries]
    
    context = {
        'module': module,
        'entries': entries_data
    }
    
    return render(request, 'modules/validation/view.html', context)


@login_required
def validation_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='validation')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
