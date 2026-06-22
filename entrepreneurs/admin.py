from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, EntrepreneurProfile, FacilitatorProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'user_type', 'phone_number', 'profile_complete', 'is_active']
    list_filter = ['user_type', 'profile_complete', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'phone_number', 'first_name', 'last_name']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('user_type', 'phone_number', 'profile_complete')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Información Adicional', {
            'fields': ('user_type', 'phone_number')
        }),
    )


@admin.register(EntrepreneurProfile)
class EntrepreneurProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'municipality', 'department', 'territory_type', 'assigned_facilitator']
    list_filter = ['territory_type', 'department', 'education_level', 'is_displaced', 'is_conflict_victim']
    search_fields = ['full_name', 'identification_number', 'municipality', 'department']
    raw_id_fields = ['user', 'assigned_facilitator']
    
    fieldsets = (
        ('Usuario', {'fields': ('user',)}),
        ('Información Personal', {
            'fields': ('full_name', 'identification_number', 'date_of_birth', 'gender', 'education_level')
        }),
        ('Contexto Territorial', {
            'fields': ('territory_type', 'department', 'municipality', 'village_or_neighborhood')
        }),
        ('Contexto Social', {
            'fields': ('is_displaced', 'is_conflict_victim', 'is_ethnic_minority')
        }),
        ('Información Adicional', {
            'fields': ('previous_entrepreneurship_experience', 'bio', 'assigned_facilitator')
        }),
    )


@admin.register(FacilitatorProfile)
class FacilitatorProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'organization', 'is_active', 'get_assigned_count', 'max_entrepreneurs']
    list_filter = ['is_active', 'created_at']
    search_fields = ['full_name', 'organization']
    raw_id_fields = ['user']
    
    def get_assigned_count(self, obj):
        return obj.get_assigned_entrepreneurs_count()
    get_assigned_count.short_description = 'Emprendedores asignados'
