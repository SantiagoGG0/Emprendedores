"""
User models for Suluhisho platform.
Includes custom User model and profile types for Entrepreneurs and Facilitators.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    Supports phone-based authentication for low-literacy users.
    """
    USER_TYPE_ENTREPRENEUR = 'entrepreneur'
    USER_TYPE_FACILITATOR = 'facilitator'
    USER_TYPE_ADMIN = 'admin'
    USER_TYPE_ALLY = 'ally'
    USER_TYPE_CLIENT = 'client'
    
    USER_TYPE_CHOICES = [
        (USER_TYPE_ENTREPRENEUR, 'Emprendedor'),
        (USER_TYPE_FACILITATOR, 'Facilitador'),
        (USER_TYPE_ADMIN, 'Administrador'),
        (USER_TYPE_ALLY, 'Aliado'),
        (USER_TYPE_CLIENT, 'Cliente/Inversor'),
    ]
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_ENTREPRENEUR,
        verbose_name='Tipo de usuario'
    )
    
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Número de teléfono'
    )
    
    profile_complete = models.BooleanField(
        default=False,
        verbose_name='Perfil completo'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_user_type_display()})"
    
    def get_profile(self):
        """Return the appropriate profile based on user type."""
        if self.user_type == self.USER_TYPE_ENTREPRENEUR:
            return getattr(self, 'entrepreneur_profile', None)
        elif self.user_type == self.USER_TYPE_FACILITATOR:
            return getattr(self, 'facilitator_profile', None)
        return None


class EntrepreneurProfile(models.Model):
    """
    Profile for entrepreneurs using the platform.
    Stores personal and territorial context.
    """
    EDUCATION_LEVEL_CHOICES = [
        ('none', 'Sin educación formal'),
        ('primary', 'Primaria'),
        ('secondary', 'Bachillerato'),
        ('technical', 'Técnico/Tecnológico'),
        ('university', 'Universitario'),
        ('postgraduate', 'Posgrado'),
    ]
    
    TERRITORY_TYPE_CHOICES = [
        ('rural', 'Rural'),
        ('urban_peripheral', 'Urbano periférico'),
        ('urban_central', 'Urbano central'),
        ('pdet', 'Territorio PDET'),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='entrepreneur_profile',
        verbose_name='Usuario'
    )
    
    # Personal information
    full_name = models.CharField(max_length=255, verbose_name='Nombre completo')
    identification_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Número de identificación'
    )
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    gender = models.CharField(max_length=50, blank=True, verbose_name='Género')
    
    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVEL_CHOICES,
        blank=True,
        verbose_name='Nivel educativo'
    )
    
    # Territorial context
    territory_type = models.CharField(
        max_length=20,
        choices=TERRITORY_TYPE_CHOICES,
        verbose_name='Tipo de territorio'
    )
    department = models.CharField(max_length=100, verbose_name='Departamento')
    municipality = models.CharField(max_length=100, verbose_name='Municipio')
    village_or_neighborhood = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Vereda/Barrio'
    )
    
    # Context flags
    is_displaced = models.BooleanField(default=False, verbose_name='Víctima de desplazamiento')
    is_conflict_victim = models.BooleanField(default=False, verbose_name='Víctima del conflicto')
    is_ethnic_minority = models.BooleanField(default=False, verbose_name='Minoría étnica')
    
    # Additional info
    previous_entrepreneurship_experience = models.BooleanField(
        default=False,
        verbose_name='Experiencia previa en emprendimiento'
    )
    bio = models.TextField(blank=True, verbose_name='Biografía')
    
    # Facilitator assignment
    assigned_facilitator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_entrepreneurs',
        limit_choices_to={'user_type': User.USER_TYPE_FACILITATOR},
        verbose_name='Facilitador asignado'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Perfil de Emprendedor'
        verbose_name_plural = 'Perfiles de Emprendedores'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.municipality}, {self.department}"


class FacilitatorProfile(models.Model):
    """
    Profile for facilitators/mentors who support entrepreneurs.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='facilitator_profile',
        verbose_name='Usuario'
    )
    
    full_name = models.CharField(max_length=255, verbose_name='Nombre completo')
    organization = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Organización'
    )
    
    # Coverage areas
    departments_covered = models.JSONField(
        default=list,
        verbose_name='Departamentos que cubre',
        help_text='Lista de departamentos donde trabaja'
    )
    municipalities_covered = models.JSONField(
        default=list,
        verbose_name='Municipios que cubre',
        help_text='Lista de municipios donde trabaja'
    )
    
    specialization = models.TextField(
        blank=True,
        verbose_name='Especialización',
        help_text='Áreas de expertise o sectores específicos'
    )
    
    max_entrepreneurs = models.IntegerField(
        default=20,
        verbose_name='Máximo de emprendedores',
        help_text='Número máximo de emprendedores que puede acompañar simultáneamente'
    )
    
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Perfil de Facilitador'
        verbose_name_plural = 'Perfiles de Facilitadores'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.organization}"
    
    def get_assigned_entrepreneurs_count(self):
        """Return the number of currently assigned entrepreneurs."""
        return self.user.assigned_entrepreneurs.count()
    
    def can_accept_more_entrepreneurs(self):
        """Check if facilitator can accept more entrepreneurs."""
        return self.get_assigned_entrepreneurs_count() < self.max_entrepreneurs

