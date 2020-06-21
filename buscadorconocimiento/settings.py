"""
Django settings for buscadorconocimiento project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# para el redireccionamiento (login, logout)
from django.urls import reverse_lazy
# Database para deploy
import dj_database_url
from decouple import config
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ekphx^&3u_j95rty!i5o&hrwx#&k)c97%b+1ox!zdj$4^i+0j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', # Core authentication framework and its default models.
    'django.contrib.auth', # Cuentas de usuario
    'django.contrib.contenttypes', #Django content type system (allows permissions to be associated with models).
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # Para Deploy
    'rest_framework', # API
    'dashboard', # panel (registro)
    'buscador'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #Manages sessions across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Para el DESPLIGUE
    'corsheaders.middleware.CorsMiddleware', # Para Deploy
    'django.middleware.common.CommonMiddleware', # Para Deploy
]

ROOT_URLCONF = 'buscadorconocimiento.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'buscadorconocimiento.wsgi.application'

# aki se pone la DB a usar
# DEPLOY
DATABASES = {
    'default': dj_database_url.config(default='postgres://sjjhymirfqxeaz:54d72399e501472ec5cb68ae2dbc988ff71f5c7e7d98731364983bf29dea8e91@ec2-52-20-248-222.compute-1.amazonaws.com:5432/d851jcejapupt6'
    )
}
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'digcomp',
#         'USER': 'desarrollador',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1', #x defecto (localhost)
#         'PORT': 5432,
#     }
# }

# MODULO para el API REST# 
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
"""
# Paginacion en el result API
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
"""

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# DEJAR LOS STATIC asi para el DEPLOY
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'https://buscadorconocimiento.herokuapp.com/static/'
# Extra places for collectstatic to find static files.
# # PARA LA CARPETA STATIC
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Para deploy
django_heroku.settings(locals())
# Obligatoria si se quiere mostrar imagenes, arch, css QUE SEAN staticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# a donde va luego del logeo (no redirecciona -no va a la url-)
LOGIN_REDIRECT_URL = reverse_lazy('home')
# a donde va luego de salir
LOGOUT_REDIRECT_URL = reverse_lazy('login')

# necesario para recuperar la clave (puerto de protocolo MSTP)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 #Si tiene problemas con el envio cambie el puerto
EMAIL_HOST_USER = 'tircnais.ca@gmail.com' #correo del que envia
EMAIL_HOST_PASSWORD = 'yoco540152' #clave
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'Equipo del sitio <noreply@example.com>'