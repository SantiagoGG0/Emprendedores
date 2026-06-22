from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable
from .forms import JTBDForm


@login_required
def jtbd_form_view(request):
    module = get_object_or_404(Module, key='jtbd')
    
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
        form = JTBDForm(request.POST)
        if form.is_valid():
            TextDeliverable.objects.filter(
                user=request.user,
                module=module
            ).update(is_current=False)
            
            jtbd_data = {
                'situacion': form.cleaned_data['situacion'],
                'motivacion': form.cleaned_data['motivacion'],
                'resultado_esperado': form.cleaned_data['resultado_esperado'],
                'job_statement': form.cleaned_data['job_statement']
            }
            
            TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=jtbd_data,
                summary=form.cleaned_data['job_statement'],
                is_current=True,
                is_validated=True
            )
            
            progress.completion_percentage = 100
            progress.status = 'completed'
            progress.save()
            
            messages.success(request, '¡Felicidades! Has completado Jobs To Be Done')
            return redirect('dashboard')
    else:
        form = JTBDForm(initial=initial_data)
    
    context = {
        'module': module,
        'progress': progress,
        'form': form,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/jtbd/form.html', context)


@login_required
def jtbd_view_completed(request):
    module = get_object_or_404(Module, key='jtbd')
    
    deliverable = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if not deliverable:
        messages.error(request, 'No has completado este módulo')
        return redirect('jtbd:form')
    
    context = {
        'module': module,
        'data': deliverable.data
    }
    
    return render(request, 'modules/jtbd/view.html', context)


@login_required
def jtbd_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='jtbd')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
