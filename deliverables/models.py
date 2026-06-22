"""
Deliverable models for Suluhisho platform.
Supports text, voice, and image deliverables using polymorphic inheritance.
"""

from django.conf import settings
from django.db import models
from polymorphic.models import PolymorphicModel


class Deliverable(PolymorphicModel):
    """
    Base polymorphic model for all deliverables.
    Each module produces one or more deliverables.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='deliverables',
        verbose_name='Usuario'
    )
    
    module = models.ForeignKey(
        'core.Module',
        on_delete=models.CASCADE,
        related_name='deliverables',
        verbose_name='Módulo'
    )
    
    # Each deliverable can have multiple versions (edit history)
    version = models.IntegerField(
        default=1,
        verbose_name='Versión'
    )
    
    is_current = models.BooleanField(
        default=True,
        verbose_name='Versión actual',
        help_text='Solo la versión más reciente debe ser True'
    )
    
    # Validation status
    is_validated = models.BooleanField(
        default=False,
        verbose_name='Validado',
        help_text='Si cumple criterios de validación'
    )
    
    validation_errors = models.JSONField(
        default=dict,
        blank=True,
        verbose_name='Errores de validación',
        help_text='Diccionario con errores por campo'
    )
    
    overall_quality = models.IntegerField(
        default=0,
        verbose_name='Calidad general',
        help_text='Score 0-100 basado en validadores'
    )
    
    # Facilitator feedback
    facilitator_comment = models.TextField(
        blank=True,
        verbose_name='Comentario del facilitador'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Entregable'
        verbose_name_plural = 'Entregables'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'module', 'is_current']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.module.title} (v{self.version})"


class TextDeliverable(Deliverable):
    """
    Text-based deliverable (forms, descriptions, etc.)
    Stores structured data as JSON.
    """
    data = models.JSONField(
        verbose_name='Datos',
        help_text='Datos estructurados del formulario'
    )
    
    # Optional plain text summary for search/display
    summary = models.TextField(
        blank=True,
        verbose_name='Resumen',
        help_text='Resumen en texto plano para búsqueda'
    )
    
    class Meta:
        verbose_name = 'Entregable de Texto'
        verbose_name_plural = 'Entregables de Texto'


class VoiceDeliverable(Deliverable):
    """
    Voice/audio deliverable.
    Stores audio file and optional transcription.
    """
    audio_file = models.FileField(
        upload_to='deliverables/audio/%Y/%m/%d/',
        verbose_name='Archivo de audio'
    )
    
    duration_seconds = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Duración (segundos)'
    )
    
    # Optional transcription
    transcription = models.TextField(
        blank=True,
        verbose_name='Transcripción',
        help_text='Transcripción automática o manual del audio'
    )
    
    transcription_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pendiente'),
            ('processing', 'Procesando'),
            ('completed', 'Completada'),
            ('failed', 'Fallida'),
            ('not_needed', 'No necesaria'),
        ],
        default='pending',
        verbose_name='Estado de transcripción'
    )
    
    # Reference to question/field this audio answers
    field_reference = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Campo asociado',
        help_text='Nombre del campo del formulario que responde'
    )
    
    class Meta:
        verbose_name = 'Entregable de Audio'
        verbose_name_plural = 'Entregables de Audio'


class ImageDeliverable(Deliverable):
    """
    Image deliverable (photos, diagrams, etc.)
    """
    image_file = models.ImageField(
        upload_to='deliverables/images/%Y/%m/%d/',
        verbose_name='Archivo de imagen'
    )
    
    # Automatically generated thumbnail
    thumbnail = models.ImageField(
        upload_to='deliverables/thumbnails/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name='Miniatura'
    )
    
    caption = models.TextField(
        blank=True,
        verbose_name='Descripción',
        help_text='Descripción opcional de la imagen'
    )
    
    # Reference to question/observation this image documents
    field_reference = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Campo asociado',
        help_text='Nombre del campo que documenta (ej: observation_3)'
    )
    
    class Meta:
        verbose_name = 'Entregable de Imagen'
        verbose_name_plural = 'Entregables de Imagen'
