from pathlib import Path
import os

# =====================================================
# 📁 BASE
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# 🔐 SEGURANÇA
# =====================================================

SECRET_KEY = 'django-insecure-trocar-em-producao'

DEBUG = True  # ❌ Em produção: False

ALLOWED_HOSTS = ['*']  # ✔ evita problema com IP


# =====================================================
# 📦 APPS
# =====================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🔐 necessário para allauth
    'django.contrib.sites',

    # 🔐 autenticação
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 🌐 login Google
    'allauth.socialaccount.providers.google',

    # 📊 seu app
    'core',
]

SITE_ID = 1


# =====================================================
# ⚙️ MIDDLEWARE
# =====================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # 🚨 ESSENCIAL (se não tiver dá erro!)
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================================================
# 🌐 URLS
# =====================================================

ROOT_URLCONF = 'painel.urls'


# =====================================================
# 🎨 TEMPLATES
# =====================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 📁 templates globais
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # obrigatório allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =====================================================
# 🗄️ BANCO
# =====================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ✔ simples (free)
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================================================
# 🔐 SENHAS
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
]


# =====================================================
# 🌎 LOCALIZAÇÃO
# =====================================================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True


# =====================================================
# 📁 STATIC (CSS/JS)
# =====================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"  # ✔ usado na cloud


# =====================================================
# 🔑 LOGIN
# =====================================================

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'


# =====================================================
# 🔐 AUTH BACKENDS
# =====================================================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# =====================================================
# 🔐 CONFIG ALLAUTH
# =====================================================

ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']


# =====================================================
# ☁️ GOOGLE LOGIN + DRIVE
# =====================================================

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
            'https://www.googleapis.com/auth/drive'
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}


# =====================================================
# ☁️ GOOGLE CLOUD STORAGE (BUCKET)
# =====================================================

# 🔑 caminho da chave JSON que você baixou
GOOGLE_APPLICATION_CREDENTIALS = os.path.join(BASE_DIR, 'chave.json')

# 🪣 nome do bucket criado
GS_BUCKET_NAME = 'agente-educacao-uesb-2026'

# 📦 django-storages
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'