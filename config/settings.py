from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
import django_heroku

# Charge les variables d'environnement du fichier .env
load_dotenv()

# Définition du chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète et mode débogage
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv('DEBUG') == 'True'

# Hôtes autorisés
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Applications Django et applications tierces
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "tailwind",
    "theme",
    "authentication",
    "blog",
    "modeltranslation",  # Gestion des traductions des modèles
]

if DEBUG:
    INSTALLED_APPS += ["whitenoise.runserver_nostatic"]
else:
    INSTALLED_APPS += ["django.contrib.staticfiles"]

# Middleware utilisé par l'application
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Gestion des fichiers statiques
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # Gestion des langues
    "middleware.AdminLocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuration de l'URL principale
ROOT_URLCONF = "config.urls"

# Configuration des templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'blog.context_processors.services_processor',
            ],
        },
    },
]

# Configuration de l'application WSGI
WSGI_APPLICATION = "config.wsgi.application"

# Configuration de la base de données selon l'environnement
ENV = os.getenv('ENV', 'development')
if ENV == 'production':
    DATABASES = {
        'default': dj_database_url.config(
            default=f"postgres://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=f"postgres://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
            conn_max_age=600,
            ssl_require=False
        )
    }

# Configuration des fichiers statiques
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'theme', 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuration de l'envoi d'emails
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Configuration des langues et de la localisation
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
INTERNAL_IPS = ["127.0.0.1"]
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
AUTH_USER_MODEL = 'authentication.User'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Langues disponibles
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

# Chemins des fichiers de traduction
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Configuration django-heroku pour paramétrer automatiquement l'application pour Heroku
django_heroku.settings(locals())