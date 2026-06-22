#!/usr/bin/env python
"""
Create admin superuser for production deployment.
Safe to run multiple times - will not duplicate users.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suluhisho_platform.settings.production')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Get credentials from environment or use defaults
username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
email = os.getenv('DJANGO_ADMIN_EMAIL', 'admin@suluhisho.com')
password = os.getenv('DJANGO_ADMIN_PASSWORD', 'admin123')

# Try to get or create admin user
admin, created = User.objects.get_or_create(
    username=username,
    defaults={
        'email': email,
        'user_type': 'admin',
        'is_staff': True,
        'is_superuser': True,
        'profile_complete': True
    }
)

if created:
    admin.set_password(password)
    admin.save()
    print(f'✓ Admin user created: {admin.username}')
else:
    # Update existing admin
    admin.user_type = 'admin'
    admin.is_staff = True
    admin.is_superuser = True
    admin.email = email
    admin.save()
    print(f'✓ Existing admin updated: {admin.username}')

print(f'  Email: {admin.email}')
print(f'  Type: {admin.user_type}')
print(f'  Staff: {admin.is_staff}')
print(f'  Superuser: {admin.is_superuser}')
