from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from entrepreneurs.models import EntrepreneurProfile

User = get_user_model()


class Command(BaseCommand):
    help = 'Crea un emprendedor de prueba para testing'

    def handle(self, *args, **options):
        # Crear usuario emprendedor
        username = 'maria'
        email = 'maria@example.com'
        password = 'demo123'
        
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'user_type': 'entrepreneur',
                'phone_number': '3001234567',
                'profile_complete': True,
                'is_staff': False,
                'is_superuser': False
            }
        )
        
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'✓ Usuario creado: {username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'⟳ Usuario ya existe: {username}')
            )
        
        # Crear perfil de emprendedor
        profile, created = EntrepreneurProfile.objects.get_or_create(
            user=user,
            defaults={
                'full_name': 'María López',
                'identification_number': '1234567890',
                'department': 'Meta',
                'municipality': 'La Macarena',
                'village_or_neighborhood': 'Vereda San José',
                'territory_type': 'pdet',
                'is_displaced': True,
                'is_conflict_victim': True,
                'is_ethnic_minority': False,
                'education_level': 'secondary'
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'✓ Perfil de emprendedor creado para {user.username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'⟳ Perfil ya existe para {user.username}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n🎉 Usuario demo listo:')
        )
        self.stdout.write(f'   Usuario: {username}')
        self.stdout.write(f'   Contraseña: {password}')
        self.stdout.write(f'\n   Inicia sesión en: http://127.0.0.1:8000/admin/')
