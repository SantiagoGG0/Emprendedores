from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Deliverable, TextDeliverable, VoiceDeliverable, ImageDeliverable


class TextDeliverableAdmin(PolymorphicChildModelAdmin):
    base_model = TextDeliverable
    list_display = ['user', 'module', 'version', 'is_current', 'is_validated', 'created_at']


class VoiceDeliverableAdmin(PolymorphicChildModelAdmin):
    base_model = VoiceDeliverable
    list_display = ['user', 'module', 'version', 'is_current', 'transcription_status', 'duration_seconds', 'created_at']
    list_filter = ['transcription_status']


class ImageDeliverableAdmin(PolymorphicChildModelAdmin):
    base_model = ImageDeliverable
    list_display = ['user', 'module', 'version', 'is_current', 'field_reference', 'created_at']


@admin.register(Deliverable)
class DeliverableParentAdmin(PolymorphicParentModelAdmin):
    base_model = Deliverable
    child_models = (TextDeliverable, VoiceDeliverable, ImageDeliverable)
    list_display = ['user', 'module', 'version', 'is_current', 'is_validated', 'created_at']
    list_filter = [PolymorphicChildModelFilter, 'is_current', 'is_validated', 'module']
    search_fields = ['user__username', 'user__email']
    raw_id_fields = ['user', 'module']
