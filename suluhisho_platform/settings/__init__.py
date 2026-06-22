"""
Settings module initialization.
"""

import os

# Default to base settings, can be overridden with DJANGO_SETTINGS_MODULE env var
# For production, set: DJANGO_SETTINGS_MODULE=suluhisho_platform.settings.production
if os.getenv('DJANGO_ENV') == 'production':
    from .production import *
else:
    from .base import *
