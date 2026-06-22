from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, EntrepreneurProfile
from core.models import Venture


class UserRegistrationForm(UserCreationForm):
    """Registration form with user type selection"""
    
    USER_TYPE_CHOICES = [
        ('entrepreneur', 'Emprendedor'),
        ('facilitator', 'Facilitador'),
    ]
    
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        label='¿Cómo te registras?'
    )
    
    # Entrepreneur profile fields
    full_name = forms.CharField(
        max_length=200,
        required=False,
        label='Nombre completo',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    municipality = forms.CharField(
        max_length=100,
        required=False,
        label='Municipio',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    region = forms.CharField(
        max_length=100,
        required=False,
        label='Región/Departamento',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input'})
        
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        
        if user_type == 'entrepreneur':
            if not cleaned_data.get('full_name'):
                raise forms.ValidationError('Nombre completo requerido para emprendedores')
            if not cleaned_data.get('municipality'):
                raise forms.ValidationError('Municipio requerido para emprendedores')
                
        return cleaned_data


class VentureForm(forms.ModelForm):
    """Form para crear/editar emprendimientos"""
    
    class Meta:
        model = Venture
        fields = ['name', 'status', 'description', 'territory', 'total_investment', 'hours_logged']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del emprendimiento'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'territory': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Municipio/Vereda'}),
            'total_investment': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'hours_logged': forms.NumberInput(attrs={'class': 'form-input'}),
        }
