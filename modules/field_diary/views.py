from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable, ImageDeliverable
from .forms import DiaryEntryForm


@login_required
def field_diary_view(request):
    """Vista principal del diario de campo - lista entradas y permite agregar nuevas"""
    module = get_object_or_404(Module, key='field_diary')
    
    # Verificar perfil emprendedor
    if not hasattr(request.user, 'entrepreneur_profile'):
        messages.error(request, 'Debes tener un perfil de emprendedor para acceder a este módulo')
        return redirect('dashboard')
    
    # Obtener o crear progreso
    progress, created = ModuleProgress.objects.get_or_create(
        user=request.user,
        module=module
    )
    
    # Marcar como en progreso si es nuevo
    if created or progress.status == 'not_started':
        progress.status = 'in_progress'
        progress.save()
    
    # Obtener todas las entradas de diario existentes
    diary_entries = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).order_by('created_at')
    
    # Parsear JSON de cada entrada
    entries_data = []
    for entry in diary_entries:
        data = entry.data
        # Buscar foto asociada (ImageDeliverable con mismo timestamp)
        image = ImageDeliverable.objects.filter(
            user=request.user,
            module=module,
            created_at=entry.created_at
        ).first()
        entries_data.append({
            'id': entry.id,
            'situacion': data.get('situacion', ''),
            'personas_afectadas': data.get('personas_afectadas', ''),
            'contexto': data.get('contexto', ''),
            'foto': image.file if image else None,
            'created_at': entry.created_at
        })
    
    # Procesar formulario para nueva entrada
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear TextDeliverable con datos JSON
            entry_data = {
                'situacion': form.cleaned_data['situacion'],
                'personas_afectadas': form.cleaned_data['personas_afectadas'],
                'contexto': form.cleaned_data['contexto']
            }
            
            text_deliverable = TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=entry_data
            )
            
            # Si hay foto, crear ImageDeliverable
            if form.cleaned_data.get('foto'):
                ImageDeliverable.objects.create(
                    user=request.user,
                    module=module,
                    file=form.cleaned_data['foto'],
                    created_at=text_deliverable.created_at  # Mismo timestamp
                )
            
            # Actualizar progreso basado en número de entradas
            total_entries = diary_entries.count() + 1
            progress.completion_percentage = min(int((total_entries / 3) * 100), 100)
            progress.save()
            
            messages.success(request, f'Entrada {total_entries} guardada. {"¡Ya puedes completar el módulo!" if total_entries >= 3 else f"Necesitas {3 - total_entries} más para completar."}')
            return redirect('field_diary:form')
    else:
        form = DiaryEntryForm()
    
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
    
    return render(request, 'modules/field_diary/form.html', context)


@login_required
def field_diary_complete(request):
    """Marca el módulo como completado"""
    if request.method != 'POST':
        return redirect('field_diary:form')
    
    module = get_object_or_404(Module, key='field_diary')
    
    # Verificar que tenga al menos 3 entradas
    entries_count = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).count()
    
    if entries_count < 3:
        messages.error(request, f'Necesitas al menos 3 entradas. Actualmente tienes {entries_count}.')
        return redirect('field_diary:form')
    
    # Marcar como completado
    progress = ModuleProgress.objects.get(
        user=request.user,
        module=module
    )
    progress.status = 'completed'
    progress.completion_percentage = 100
    progress.save()
    
    messages.success(request, '¡Felicidades! Has completado el Diario de Campo')
    return redirect('dashboard')


@login_required
def field_diary_view_completed(request):
    """Vista de solo lectura del diario de campo completado"""
    module = get_object_or_404(Module, key='field_diary')
    
    # Obtener todas las entradas
    diary_entries = TextDeliverable.objects.filter(
        user=request.user,
        module=module
    ).order_by('created_at')
    
    entries_data = []
    for entry in diary_entries:
        data = entry.data
        image = ImageDeliverable.objects.filter(
            user=request.user,
            module=module,
            created_at=entry.created_at
        ).first()
        entries_data.append({
            'situacion': data.get('situacion', ''),
            'personas_afectadas': data.get('personas_afectadas', ''),
            'contexto': data.get('contexto', ''),
            'foto': image.file if image else None,
            'created_at': entry.created_at
        })
    
    context = {
        'module': module,
        'entries': entries_data
    }
    
    return render(request, 'modules/field_diary/view.html', context)


@login_required
def field_diary_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='field_diary')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
