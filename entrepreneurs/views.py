from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import EntrepreneurProfile, FacilitatorProfile


def login_view(request):
    """Login propio (no admin)"""
    
    # Si ya está autenticado, redirect dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido/a, {user.get_full_name() or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    """Logout"""
    auth_logout(request)
    messages.info(request, 'Sesión cerrada')
    return redirect('login')


def register_view(request):
    """Registration for new users"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['user_type']
            user.save()
            
            # Create profile based on user type
            if user.user_type == 'entrepreneur':
                EntrepreneurProfile.objects.create(
                    user=user,
                    full_name=form.cleaned_data['full_name'],
                    municipality=form.cleaned_data['municipality'],
                    department=form.cleaned_data.get('region', ''),
                    territory_type='pdet'
                )
            else:
                FacilitatorProfile.objects.create(
                    user=user,
                    full_name=form.cleaned_data.get('full_name', user.username),
                    organization='Suluhisho'
                )
            
            messages.success(request, f'¡Cuenta creada! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})
