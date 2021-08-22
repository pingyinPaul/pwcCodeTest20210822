from .base import *

SECRET_KEY = '7av833#2!e99tt%5o#p3&ey$md214yioc#dj-)2$@^*44wd=i3'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES_ENGINE = 'django.db.backends.sqlite3'

DATABASES_NAME = 'db.sqlite3'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3001', 'http://localhost:3000', 'https://codeteleonco.cn', 'http://codeteleonco.cn',
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

X_FRAME_OPTIONS = 'ALLOW-FROM http://localhost https://codeteleonco.cn'

FRONT_END = 'http://localhost:3000'

COM_FRONT_END = 'http://localhost:3000'

EMAIL_PAGE_DOMAIN = "http://localhost:8000"

