"""response module
    local用コンフィグ server.pyにより呼び出し。
"""
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0!*rs&^)+p^4bsh=4cbm&(i5r=doaj3m-u3-&g7hn*iaz-11a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES = {
    'default': {
        # postgresql前提のため他のDBにする方はengineも変更してください。
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '自身のdb設定',
        'USER': '自身のdb設定',
        'PASSWORD': '自身のdb設定',
        'HOST': '自身のdb設定',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 30,
        },
        'TEST': {
            'NAME': 'unitdb'
        }
    }
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'local': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'loggers': {
        # 自作したログ出力
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Djangoのエラー・警告・開発WEBサーバのアクセスログ
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 実行SQL
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# original settings

# Azure
SCOPES = ['User.Read']
TENANT_ID = '自身のAzureパラメータ'
AUTHORITY = '自身のAzureパラメータ'
CLIENT_ID = '自身のAzureパラメータ'
REDIRECT_PATH = 'https://localhost/general-ui/callback/'
CLIENT_SECRET = '自身のAzureパラメータ'
ENDPOINT = '自身のAzureパラメータ'

# Domain
DOMAIN = 'localhost'
