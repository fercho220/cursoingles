import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ==============================================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-for-dev')

# DEBUG se leerá desde las variables de entorno de Render. En local será False por defecto.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Configuración de hosts permitidos para Render
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ==============================================================================
# 🧩 APLICACIONES
# ==============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ingles',
    'usuario',
    'import_export',
    'crispy_forms',
    'crispy_bootstrap4', # CORRECTO
    'rest_framework',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# ==============================================================================
# ⚙️ MIDDLEWARE
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # --- AÑADIDO: WhiteNoise para servir archivos estáticos ---
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

# --- CORREGIDO: Forma estándar y robusta para leer la DATABASE_URL ---
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}


# ==============================================================================
# 🔐 VALIDACIÓN DE CONTRASEÑAS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# ==============================================================================
# 🌐 INTERNACIONALIZACIÓN
# ==============================================================================

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==============================================================================
# 🗂️ ARCHIVOS ESTÁTICOS Y DE MEDIOS
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# --- AÑADIDO: Almacenamiento de estáticos para WhiteNoise ---
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ==============================================================================
# 🔑 CLAVE PRIMARIA POR DEFECTO
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
