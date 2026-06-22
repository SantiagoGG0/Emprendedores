from django.contrib import admin
from .models import (
    Module, ModuleProgress, ValidationRule, Example, ReferenceContent,
    Venture, VentureEntrepreneur, Ally, Client, Investment
)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['order', 'key', 'title', 'estimated_time_minutes', 'is_active']
    list_filter = ['is_active', 'key']
    search_fields = ['title', 'description']
    ordering = ['order']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('key', 'order', 'title', 'is_active', 'estimated_time_minutes')
        }),
        ('Contenido General', {
            'fields': ('description', 'instructions')
        }),
        ('Contenido Instruccional (Ver Guía)', {
            'fields': ('why_exists', 'how_to_guide', 'common_errors', 'deliverable_description'),
            'description': 'Contenido que aparece en la página de guía del módulo'
        }),
    )


@admin.register(ModuleProgress)
class ModuleProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'module', 'status', 'completion_percentage', 'validation_passed', 'started_at', 'completed_at']
    list_filter = ['status', 'validation_passed', 'module', 'facilitator_override']
    search_fields = ['user__username', 'user__email']
    raw_id_fields = ['user', 'module']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Progreso', {
            'fields': ('user', 'module', 'status', 'completion_percentage', 'validation_passed')
        }),
        ('Fechas', {
            'fields': ('started_at', 'completed_at', 'created_at', 'updated_at')
        }),
        ('Facilitador', {
            'fields': ('facilitator_notes', 'facilitator_override')
        }),
    )


@admin.register(ValidationRule)
class ValidationRuleAdmin(admin.ModelAdmin):
    list_display = ['module', 'rule_type', 'field_name', 'min_value', 'is_active']
    list_filter = ['rule_type', 'is_active', 'module']
    search_fields = ['field_name', 'error_message']


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['module', 'title', 'territory_context', 'is_featured']
    list_filter = ['module', 'is_featured']
    search_fields = ['title', 'territory_context', 'description']


@admin.register(ReferenceContent)
class ReferenceContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'key', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'key', 'short_definition', 'keywords']
    filter_horizontal = ['related_modules']
    ordering = ['category', 'order', 'title']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('key', 'category', 'title', 'order', 'is_active')
        }),
        ('Contenido', {
            'fields': ('short_definition', 'detailed_explanation')
        }),
        ('Metadata', {
            'fields': ('keywords', 'external_links', 'related_modules')
        }),
    )


class VentureEntrepreneurInline(admin.TabularInline):
    model = VentureEntrepreneur
    extra = 1
    raw_id_fields = ['entrepreneur']


class InvestmentInline(admin.TabularInline):
    model = Investment
    extra = 0
    readonly_fields = ['date']


@admin.register(Venture)
class VentureAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_by', 'territory', 'total_investment', 'hours_logged', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'description', 'territory']
    raw_id_fields = ['created_by']
    inlines = [VentureEntrepreneurInline, InvestmentInline]
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'status', 'territory', 'description')
        }),
        ('Gestión', {
            'fields': ('created_by', 'total_investment', 'hours_logged')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(VentureEntrepreneur)
class VentureEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ['venture', 'entrepreneur', 'role', 'joined_at']
    list_filter = ['role', 'joined_at']
    search_fields = ['venture__name', 'entrepreneur__username', 'entrepreneur__email']
    raw_id_fields = ['venture', 'entrepreneur']


@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    list_display = ['organization', 'user', 'contact_email', 'created_at']
    search_fields = ['organization', 'user__username', 'contact_email']
    filter_horizontal = ['ventures']
    raw_id_fields = ['user']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'contact_email', 'total_invested', 'created_at']
    search_fields = ['user__username', 'company', 'contact_email']
    raw_id_fields = ['user']


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['venture', 'client', 'amount', 'date']
    list_filter = ['date']
    search_fields = ['venture__name', 'client__user__username']
    raw_id_fields = ['venture', 'client']
    readonly_fields = ['date']
