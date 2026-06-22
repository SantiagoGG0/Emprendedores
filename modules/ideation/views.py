from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Module, ModuleProgress, Example
from deliverables.models import TextDeliverable
from .forms import IdeationForm


@login_required
def ideation_form_view(request):
    module = get_object_or_404(Module, key='ideation')
    
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
        form = IdeationForm(request.POST)
        if form.is_valid():
            TextDeliverable.objects.filter(
                user=request.user,
                module=module
            ).update(is_current=False)
            
            ideas = [
                form.cleaned_data['idea_1'],
                form.cleaned_data['idea_2'],
                form.cleaned_data['idea_3'],
                form.cleaned_data['idea_4'],
                form.cleaned_data['idea_5']
            ]
            if form.cleaned_data.get('idea_6'):
                ideas.append(form.cleaned_data['idea_6'])
            
            ideation_data = {
                'ideas': ideas,
                'top_1': form.cleaned_data['top_1'],
                'top_2': form.cleaned_data['top_2'],
                'top_3': form.cleaned_data['top_3'],
                'idea_final': form.cleaned_data['idea_final']
            }
            
            TextDeliverable.objects.create(
                user=request.user,
                module=module,
                data=ideation_data,
                summary=form.cleaned_data['idea_final'],
                is_current=True,
                is_validated=True
            )
            
            progress.completion_percentage = 100
            progress.status = 'completed'
            progress.save()
            
            messages.success(request, '¡Felicidades! Has completado la Ideación')
            return redirect('dashboard')
    else:
        form = IdeationForm(initial=initial_data)
    
    context = {
        'module': module,
        'progress': progress,
        'form': form,
        'territorial_example': Example.objects.filter(module=module, is_featured=True).first(),
        'current_module': module,
    }
    
    return render(request, 'modules/ideation/form.html', context)


@login_required
def ideation_view_completed(request):
    module = get_object_or_404(Module, key='ideation')
    
    deliverable = TextDeliverable.objects.filter(
        user=request.user,
        module=module,
        is_current=True
    ).first()
    
    if not deliverable:
        messages.error(request, 'No has completado este módulo')
        return redirect('ideation:form')
    
    context = {
        'module': module,
        'data': deliverable.data
    }
    
    return render(request, 'modules/ideation/view.html', context)


@login_required
def ideation_intro_view(request):
    """Vista instruccional antes del formulario"""
    module = get_object_or_404(Module, key='ideation')
    
    return render(request, 'knowledge_base/instructional_content_page.html', {
        'module': module
    })
