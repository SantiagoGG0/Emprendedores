"""
Core models for Suluhisho platform.
Includes Module, ModuleProgress, ValidationRule, and Example models.
"""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Module(models.Model):
    """
    Represents one of the 7 steps in the ideation journey.
    """
    # Module identifiers
    IKIGAI = 'ikigai'
    FIELD_DIARY = 'field_diary'
    EMPATHY = 'empathy'
    JTBD = 'jtbd'
    IDEATION = 'ideation'
    VALUE_PROP = 'value_prop'
    VALIDATION = 'validation'
    
    MODULE_CHOICES = [
        (IKIGAI, 'Paso 1: ¿Quién eres y qué te mueve? (Ikigai)'),
        (FIELD_DIARY, 'Paso 2: Abre los ojos (Diario de Campo)'),
        (EMPATHY, 'Paso 3: Enamórate del problema (Mapa de Empatía + POV)'),
        (JTBD, 'Paso 4: ¿Qué trabajo está contratando tu cliente? (JTBD)'),
        (IDEATION, 'Paso 5: Genera ideas (Brainstorming + SCAMPER)'),
        (VALUE_PROP, 'Paso 6: Construye tu propuesta de valor (Value Proposition Canvas)'),
        (VALIDATION, 'Paso 7: Valida con personas reales (Entrevistas)'),
    ]
    
    key = models.CharField(
        max_length=50,
        unique=True,
        choices=MODULE_CHOICES,
        verbose_name='Identificador del módulo'
    )
    
    order = models.IntegerField(
        unique=True,
        verbose_name='Orden',
        help_text='Orden secuencial del módulo (1-7)'
    )
    
    title = models.CharField(max_length=255, verbose_name='Título')
    
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Descripción del propósito del módulo'
    )
    
    instructions = models.TextField(
        verbose_name='Instrucciones',
        help_text='Instrucciones paso a paso para completar el módulo',
        blank=True
    )
    
    # Theoretical content sections (from PDF)
    why_exists = models.TextField(
        verbose_name='Por qué existe este paso',
        help_text='Fundamento teórico y justificación del módulo',
        blank=True
    )
    
    how_to_guide = models.TextField(
        verbose_name='Cómo hacerlo - Guía paso a paso',
        help_text='Instrucciones detalladas con ejemplos orientadores',
        blank=True
    )
    
    common_errors = models.TextField(
        verbose_name='Errores comunes',
        help_text='Lista de errores frecuentes que evitar',
        blank=True
    )
    
    deliverable_description = models.TextField(
        verbose_name='Descripción del entregable',
        help_text='Qué debe registrar el emprendedor en la plataforma',
        blank=True
    )
    
    estimated_time_minutes = models.IntegerField(
        verbose_name='Tiempo estimado (minutos)',
        help_text='Tiempo aproximado para completar el módulo'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text='Si está desactivado, no aparecerá en el recorrido'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['order']
    
    def __str__(self):
        return f"Paso {self.order}: {self.title}"


class ModuleProgress(models.Model):
    """
    Tracks an entrepreneur's progress through a specific module.
    """
    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'
    STATUS_BLOCKED = 'blocked'
    
    STATUS_CHOICES = [
        (STATUS_NOT_STARTED, 'No iniciado'),
        (STATUS_IN_PROGRESS, 'En progreso'),
        (STATUS_COMPLETED, 'Completado'),
        (STATUS_BLOCKED, 'Bloqueado'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='module_progress',
        verbose_name='Usuario'
    )
    
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='user_progress',
        verbose_name='Módulo'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_STARTED,
        verbose_name='Estado'
    )
    
    completion_percentage = models.IntegerField(
        default=0,
        verbose_name='Porcentaje de completitud',
        help_text='0-100'
    )
    
    validation_passed = models.BooleanField(
        default=False,
        verbose_name='Validación pasada',
        help_text='Si cumple todos los criterios de validación'
    )
    
    started_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de inicio'
    )
    
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de completitud'
    )
    
    # Facilitator feedback
    facilitator_notes = models.TextField(
        blank=True,
        verbose_name='Notas del facilitador'
    )
    
    facilitator_override = models.BooleanField(
        default=False,
        verbose_name='Override del facilitador',
        help_text='Si el facilitador marcó manualmente como completado'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Progreso de Módulo'
        verbose_name_plural = 'Progresos de Módulos'
        unique_together = ['user', 'module']
        ordering = ['module__order']
    
    def __str__(self):
        return f"{self.user.username} - {self.module.title} ({self.get_status_display()})"


class ValidationRule(models.Model):
    """
    Defines validation criteria for module completion.
    """
    RULE_TYPE_REQUIRED_FIELDS = 'required_fields'
    RULE_TYPE_MIN_COUNT = 'min_count'
    RULE_TYPE_CUSTOM_LOGIC = 'custom_logic'
    
    RULE_TYPE_CHOICES = [
        (RULE_TYPE_REQUIRED_FIELDS, 'Campos requeridos'),
        (RULE_TYPE_MIN_COUNT, 'Cantidad mínima'),
        (RULE_TYPE_CUSTOM_LOGIC, 'Lógica personalizada'),
    ]
    
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='validation_rules',
        verbose_name='Módulo'
    )
    
    rule_type = models.CharField(
        max_length=50,
        choices=RULE_TYPE_CHOICES,
        verbose_name='Tipo de regla'
    )
    
    field_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Nombre del campo',
        help_text='Para reglas de campos o conteo'
    )
    
    min_value = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Valor mínimo',
        help_text='Para reglas de conteo mínimo'
    )
    
    error_message = models.TextField(
        verbose_name='Mensaje de error',
        help_text='Mensaje a mostrar si no se cumple la regla'
    )
    
    is_active = models.BooleanField(default=True, verbose_name='Activa')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Regla de Validación'
        verbose_name_plural = 'Reglas de Validación'
        ordering = ['module__order', 'id']
    
    def __str__(self):
        return f"{self.module.title} - {self.get_rule_type_display()}"


class Example(models.Model):
    """
    Stores example cases for each module, contextualized to Colombian territories.
    """
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='examples',
        verbose_name='Módulo'
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name='Título del ejemplo'
    )
    
    territory_context = models.CharField(
        max_length=255,
        verbose_name='Contexto territorial',
        help_text='Ej: Municipio de Ituango, Antioquia (PDET)'
    )
    
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Narrativa del ejemplo aplicado al territorio'
    )
    
    key_learnings = models.TextField(
        blank=True,
        verbose_name='Aprendizajes clave',
        help_text='Lecciones que ilustra este ejemplo'
    )
    
    is_featured = models.BooleanField(
        default=False,
        verbose_name='Destacado',
        help_text='Mostrar como ejemplo principal'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Ejemplo'
        verbose_name_plural = 'Ejemplos'
        ordering = ['module__order', '-is_featured', 'id']
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"


class ReferenceContent(models.Model):
    """
    Knowledge base entries: glossary terms, concepts, resources.
    """
    CATEGORY_METHODOLOGY = 'methodology'
    CATEGORY_TERRITORIAL = 'territorial'
    CATEGORY_PLATFORM = 'platform'
    
    CATEGORY_CHOICES = [
        (CATEGORY_METHODOLOGY, 'Metodología'),
        (CATEGORY_TERRITORIAL, 'Contexto Territorial'),
        (CATEGORY_PLATFORM, 'Plataforma'),
    ]
    
    key = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Identificador único',
        help_text='Ej: jtbd, pov, pdet, empathy_map'
    )
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name='Categoría'
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name='Título',
        help_text='Ej: Jobs To Be Done, PDET, Mapa de Empatía'
    )
    
    short_definition = models.TextField(
        verbose_name='Definición corta',
        help_text='2-3 líneas. Aparece en modal y búsqueda.'
    )
    
    detailed_explanation = models.TextField(
        verbose_name='Explicación detallada',
        help_text='Markdown con ejemplos. Aparece en página completa glosario.'
    )
    
    external_links = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Links externos',
        help_text='Lista de dicts: [{"title": "...", "url": "...", "type": "video|article|tool"}]'
    )
    
    keywords = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Palabras clave',
        help_text='Lista para búsqueda: ["emprendimiento", "rural", "validación"]'
    )
    
    related_modules = models.ManyToManyField(
        Module,
        blank=True,
        related_name='reference_contents',
        verbose_name='Módulos relacionados'
    )
    
    order = models.IntegerField(
        default=0,
        verbose_name='Orden',
        help_text='Para ordenamiento en glosario'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Contenido de Referencia'
        verbose_name_plural = 'Contenidos de Referencia'
        ordering = ['category', 'order', 'title']
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"


class Venture(models.Model):
    """
    Emprendimiento - entidad negocio que agrupa entrepreneurs, inversiones, y progreso.
    """
    STATUS_DIAGNOSTIC = 'diagnostic'
    STATUS_ACTIVE = 'active'
    STATUS_PAUSED = 'paused'
    STATUS_COMPLETED = 'completed'
    
    STATUS_CHOICES = [
        (STATUS_DIAGNOSTIC, 'En Diagnóstico'),
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_PAUSED, 'Pausado'),
        (STATUS_COMPLETED, 'Completado'),
    ]
    
    name = models.CharField(
        max_length=255,
        verbose_name='Nombre del emprendimiento'
    )
    
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=STATUS_DIAGNOSTIC,
        verbose_name='Estado'
    )
    
    description = models.TextField(
        verbose_name='Descripción',
        blank=True
    )
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='created_ventures',
        verbose_name='Creado por'
    )
    
    entrepreneurs = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='VentureEntrepreneur',
        related_name='ventures',
        verbose_name='Emprendedores'
    )
    
    total_investment = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Inversión total'
    )
    
    hours_logged = models.IntegerField(
        default=0,
        verbose_name='Horas registradas'
    )
    
    territory = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Territorio/Municipio'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Emprendimiento'
        verbose_name_plural = 'Emprendimientos'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_completion_percentage(self):
        """Calculate average completion across all entrepreneurs."""
        entrepreneurs = self.ventureentrepreneur_set.all()
        if not entrepreneurs:
            return 0
        
        total = 0
        for ve in entrepreneurs:
            progress = ModuleProgress.objects.filter(user=ve.entrepreneur)
            completed = progress.filter(status='completed').count()
            total += (completed / 7.0) * 100
        
        return int(total / entrepreneurs.count()) if entrepreneurs else 0


class VentureEntrepreneur(models.Model):
    """
    Relación M2M entre Venture y Entrepreneur con metadata.
    """
    ROLE_LEAD = 'lead'
    ROLE_MEMBER = 'member'
    
    ROLE_CHOICES = [
        (ROLE_LEAD, 'Líder'),
        (ROLE_MEMBER, 'Miembro'),
    ]
    
    venture = models.ForeignKey(
        Venture,
        on_delete=models.CASCADE,
        verbose_name='Emprendimiento'
    )
    
    entrepreneur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Emprendedor'
    )
    
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_MEMBER,
        verbose_name='Rol'
    )
    
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de incorporación')
    
    class Meta:
        verbose_name = 'Emprendedor en Emprendimiento'
        verbose_name_plural = 'Emprendedores en Emprendimientos'
        unique_together = ['venture', 'entrepreneur']
    
    def __str__(self):
        return f"{self.entrepreneur.get_full_name()} - {self.venture.name} ({self.get_role_display()})"


class Ally(models.Model):
    """
    Aliado/Partner organizacional que puede estar asociado a ventures.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    
    organization = models.CharField(
        max_length=255,
        verbose_name='Organización'
    )
    
    ventures = models.ManyToManyField(
        Venture,
        blank=True,
        related_name='allies',
        verbose_name='Emprendimientos'
    )
    
    contact_email = models.EmailField(
        blank=True,
        verbose_name='Email de contacto'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Aliado'
        verbose_name_plural = 'Aliados'
    
    def __str__(self):
        return f"{self.organization} ({self.user.get_full_name()})"


class Client(models.Model):
    """
    Cliente/Inversor que puede invertir en ventures.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    
    company = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Empresa'
    )
    
    contact_email = models.EmailField(
        blank=True,
        verbose_name='Email de contacto'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Cliente/Inversor'
        verbose_name_plural = 'Clientes/Inversores'
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
    def total_invested(self):
        """Sum of all investments."""
        return self.investment_set.aggregate(models.Sum('amount'))['amount__sum'] or 0


class Investment(models.Model):
    """
    Inversión de un cliente en un emprendimiento.
    """
    venture = models.ForeignKey(
        Venture,
        on_delete=models.CASCADE,
        verbose_name='Emprendimiento'
    )
    
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Cliente/Inversor'
    )
    
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Monto'
    )
    
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de inversión'
    )
    
    notes = models.TextField(
        blank=True,
        verbose_name='Notas'
    )
    
    class Meta:
        verbose_name = 'Inversión'
        verbose_name_plural = 'Inversiones'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.client} → {self.venture.name}: ${self.amount}"
