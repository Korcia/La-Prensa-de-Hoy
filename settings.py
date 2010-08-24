# Django settings for laprensadehoy project.
import os.path

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))
BASE_PATH = os.path.dirname(__file__)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jose_lpdh.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Settings para enviar emails via Gmail
#EMAIL_USE_TLS = True
#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587

# Settings para comprobar envio de boletines a traves de email
ARTICLES_FROM_EMAIL = {
    'protocol': 'IMAP4',
    'host': '',
    'port': 993,
    'keyfile': '/path/to/keyfile',
    'certfile': '/path/to/certfile',
    'user': 'boletines',
    'password': '',
    'ssl': True,
    'autopost': True,
    'markup': 'm',
    'acknowledge': True,
    }
    
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ES'

SITE_ID = 2

SESSION_COOKIE_DAYS = 90
SESSION_COOKIE_AGE = 60 * 60 * 24 * SESSION_COOKIE_DAYS 

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''
#MEDIA_ROOT = BASE_PATH+'/media'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''
#MEDIA_URL = '/media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'
#ADMIN_MEDIA_PREFIX = '/media/admin/'
# Make this unique, and don't share it with anybody.
SECRET_KEY = '&+xsyc=_(rkwu^$wgn5w01o6owa49_9s5!$wfg$_9si&=k+y&1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'laprensadehoy.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.messages',
    'prensahoy',
    'coltrane',
    'coltranefree',
    #'registration',
    'accounts',
    'management',
)
ACCOUNT_ACTIVATION_DAYS = 7
#AUTH_PROFILE_MODULE = "prensahoy.UsuarioPrensaHoyPerfil"
#AUTH_PROFILE_MODULE = "registration.RegistrationProfile"
AUTH_PROFILE_MODULE = 'accounts.userprofile'
LOGIN_URL = "/usuarios/login/"
#LOGIN_URL = ''
#LOGIN_REDIRECT_URL = '/resumenes/'
LOGIN_REDIRECT_URL = '/usuarios/mi_cuenta/'
LOGOUT_REDIRECT_URL = '/'
