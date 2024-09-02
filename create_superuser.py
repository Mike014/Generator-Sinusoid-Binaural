# -*- coding: utf-8 -*-
import os
import django
from django.core.exceptions import ImproperlyConfigured

# Imposta la variabile di ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generator_sinusoid.settings')

try:
    # Configura Django
    django.setup()
except ImproperlyConfigured as e:
    print(f"Errore di configurazione: {e}")
    exit(1)

from django.contrib.auth.models import User

# Crea il superuser se non esiste già
if not User.objects.filter(username='Mik_014').exists():
    User.objects.create_superuser('Mik_014', 'mikgrimaldi7@gmail.com', '0329199028Aa')
    print("Superuser creato con successo.")
else:
    print("Il superuser esiste già.")