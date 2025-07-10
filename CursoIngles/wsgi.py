# CursoIngles/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursoIngles.settings')

# Se obtiene la aplicación de Django
application = get_wsgi_application()

# Se "envuelve" la aplicación con WhiteNoise
application = WhiteNoise(application)
