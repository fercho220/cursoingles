import os
from pathlib import Path
import dj_database_url

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ==============================================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-for-dev')

# DEBUG se lee desde las variables de entorno. Es 'False' en producción.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts permitidos, configurado para Render
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ==============================================================================
# 🧩 APLICACIONES INSTALADAS
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Necesario para WhiteNoise
    'django.contrib.staticfiles',
    'ingles',
    'usuario',
    'import_export',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"


# ==============================================================================
# ⚙️ MIDDLEWARE
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Debe estar aquí, segundo en la lista
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CursoIngles.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CursoIngles.wsgi.application'


# ==============================================================================
# 🛢️ BASE DE DATOS
# ==============================================================================

DATABASES = {
    'default': dj_database_url.config(
        # Fallback a una base de datos local si no está en Render
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}


# ==============================================================================
# 🔐 VALIDACIÓN DE CONTRASEÑAS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==============================================================================
# 🌐 INTERNACIONALIZACIÓN
# ==============================================================================

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==============================================================================
# 🗂️ ARCHIVOS ESTÁTICOS Y DE MEDIOS (Configuración final para Render)
# ==============================================================================

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Directorio donde `collectstatic` copiará todos los archivos para producción
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Solo en producción (`DEBUG=False`), usa el almacenamiento de WhiteNoise.
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ==============================================================================
# 🔑 CLAVE PRIMARIA POR DEFECTO
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
