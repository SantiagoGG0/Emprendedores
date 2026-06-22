from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

from .forms import IkigaiForm
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable


@login_required
def ikigai_form_view(request):
    """Vista principal formulario Ikigai"""
    
    # Obtener módulo Ikigai
    module = get_object_or_404(Module, key='ikigai')
    
    # Verificar si usuario es emprendedor
    if not hasattr(request.user, 'entrepreneur_profile'):
        messages.error(request, "Solo emprendedores pueden acceder a los módulos")
        return redirect('dashboard')
    
    # Obtener o crear progreso
    progress, created = ModuleProgress.objects.get_or_create(
        user=request.user,
        module=module,
        defaults={'status': 'in_progress'}
    )
    
    # Cargar datos existentes si hay deliverable
    initial_data = {}
    existing_deliverable = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if existing_deliverable and existing_deliverable.data:
        # Mapear datos JSON a campos del formulario
        ikigai_data = existing_deliverable.data
        initial_data = {
            'amas_1': ikigai_data.get('que_amas', [''])[0],
            'amas_2': ikigai_data.get('que_amas', ['', ''])[1],
            'amas_3': ikigai_data.get('que_amas', ['', '', ''])[2],
            'amas_4': ikigai_data.get('que_amas', ['', '', '', ''])[3] if len(ikigai_data.get('que_amas', [])) > 3 else '',
            
            'bueno_1': ikigai_data.get('en_que_eres_bueno', [''])[0],
            'bueno_2': ikigai_data.get('en_que_eres_bueno', ['', ''])[1],
            'bueno_3': ikigai_data.get('en_que_eres_bueno', ['', '', ''])[2],
            'bueno_4': ikigai_data.get('en_que_eres_bueno', ['', '', '', ''])[3] if len(ikigai_data.get('en_que_eres_bueno', [])) > 3 else '',
            
            'necesita_1': ikigai_data.get('que_necesita_comunidad', [''])[0],
            'necesita_2': ikigai_data.get('que_necesita_comunidad', ['', ''])[1],
            'necesita_3': ikigai_data.get('que_necesita_comunidad', ['', '', ''])[2],
            'necesita_4': ikigai_data.get('que_necesita_comunidad', ['', '', '', ''])[3] if len(ikigai_data.get('que_necesita_comunidad', [])) > 3 else '',
            
            'pagarian_1': ikigai_data.get('por_que_pagarian', [''])[0],
            'pagarian_2': ikigai_data.get('por_que_pagarian', ['', ''])[1],
            'pagarian_3': ikigai_data.get('por_que_pagarian', ['', '', ''])[2],
            'pagarian_4': ikigai_data.get('por_que_pagarian', ['', '', '', ''])[3] if len(ikigai_data.get('por_que_pagarian', [])) > 3 else '',
            
            'interseccion': ikigai_data.get('frase_interseccion', '')
        }
    
    if request.method == 'POST':
        form = IkigaiForm(request.POST)
        
        if form.is_valid():
            with transaction.atomic():
                # Marcar deliverables anteriores como no actuales
                TextDeliverable.objects.filter(
                    user=request.user,
                    module=module
                ).update(is_current=False)
                
                # Crear nuevo deliverable
                ikigai_data = form.get_ikigai_data()
                deliverable = TextDeliverable.objects.create(
                    user=request.user,
                    module=module,
                    data=ikigai_data,
                    summary=ikigai_data['frase_interseccion'],
                    is_current=True,
                    is_validated=True  # Auto-validado si pasa validación del form
                )
                
                # Actualizar progreso
                progress.completion_percentage = 100
                progress.status = 'completed'
                progress.save()
                
                messages.success(request, "¡Felicidades! Has completado tu Ikigai")
                return redirect('dashboard')
    else:
        form = IkigaiForm(initial=initial_data)
    
    context = {
        'form': form,
        'module': module,
        'progress': progress,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/ikigai/form.html', context)


@login_required
def ikigai_view_view(request):
    """Vista solo lectura del Ikigai completado"""
    
    module = get_object_or_404(Module, key='ikigai')
    deliverable = get_object_or_404(
        TextDeliverable,
        user=request.user,
        module=module,
        is_current=True
    )
    
    context = {
        'module': module,
        'deliverable': deliverable,
        'ikigai_data': deliverable.data
    }
    
    return render(request, 'modules/ikigai/view.html', context)


@login_required
def ikigai_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='ikigai')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
