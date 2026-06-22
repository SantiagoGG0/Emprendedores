"""
Decorators for access control.
"""

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def user_type_required(*user_types):
    """
    Decorator to restrict views by user_type.
    
    Usage:
        @user_type_required('admin', 'ally')
        def admin_dashboard(request):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            if request.user.user_type not in user_types:
                messages.error(request, 'No tienes permiso para acceder a esta página.')
                return redirect('dashboard')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
