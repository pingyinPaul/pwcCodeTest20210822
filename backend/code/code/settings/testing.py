from .base import *

SECRET_KEY = '7av833#2!e99tt%5o#p3&ey$md214yioc#dj-)2$@^*44wd=i3'

DEBUG = False

ALLOWED_HOSTS = ['
        "58.87.113.135",
        "43.129.21.76",
        ']


DATABASES = {
        'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': "testdb",

        'USER': "postgres",

        'PASSWORD': "sanitadmin",

        'HOST': "127.0.0.1",

        'PORT': "5432",}}

CORS_ORIGIN_WHITELIST = (
    'http://58.87.113.135','http://43.129.21.76', 'http://localhost:3000', 'https://codeteleonco.cn', 'http://codeteleonco.cn',
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

X_FRAME_OPTIONS = 'ALLOW-FROM http://58.87.113.135'

FRONT_END = 'http://58.87.113.135'

COM_FRONT_END = 'http://43.129.21.76'

EMAIL_PAGE_DOMAIN = "http://58.87.113.135:10001/happymailbox/"

ALI_APP_ID = '2016110100784944'

ALI_APP_PRIVATE_KEY = 'MIIEowIBAAKCAQEAiGGEouIhFfXr+9dv5+F6MVacE0ywx/YWLjkDOoXqXv2rrYSCsVi9sYMOwi8/ksmx2EjU5ebyUgld5qN9cnpfdjsMI6X62QKPna/hbQEg6z6S3n3T/rbkJJu8ZZTR74KAPk6oYRG/oEgUQGLr1LEgIAFp9m20Cwf0LLQNTHyKB/7E/KiZuLWfaUddBjr/+Y4wzaC6T7rC2DjwZTh7o7Rqofes5fDHm9pbDmvOlhaOANYwqEHmHNAGdkxDdcZ0/13+4mpo0VUZEocm8/zG09UPswTqWKU6XdIuBwHfTweV6wBTh2SJ5xnsTE1D9vx1g6WvxVYNst69/PABPvkiYXt6JQIDAQABAoIBAQCDdZyodVh3Fqn2A+B2n71tOZMQd2ggF3Gh9IrMKrGUBukpRQXFdUjEhxP+0hRxpcGsPegaA9eohCbjXsxZQOQrzxcQdbmq3PEaiqK8s83LdHGVzaw/ZoPbVdLwB9elCyIa7S8ZAka4dUIwHio8xs+0iihdxbk6uNwBCz2WcKWMtfpG3G9bfj3OZmorzjwmT3FJqQ16xQhY3Ju3SVwgluCR2aajIgYW7wF8vxt973wKakWGc/oV2igHilf/B8tncCCXIdGrgqtqaKrthQDOc8pKz7sHFwWPFw/yLjxTgiGD0WZ2lLzRRmpntpF5vJn0jEHMBvy07kOqnHM0nlFQAIKxAoGBAMpQvicVXvGaDlAsB3b+BhaNAMmbNm7evuyoxScBksQ5d8nz8CWxVloVC6f0wZOG4GAtPgVmdKtASQPD2/EZHZeLbcYjCECRN2WbBH7tnimKz2GvqxkOxeaN16PlHW/fgm+3xTyIfs/mYUtzQOVBag/CJ0MacWBt0TArSA1EaZXDAoGBAKyR2xaVV9c9J/7KHp/u7BHJWB5WEaXbulk+KAGl3RxUtvcTGZtQmZfrg41MXWIdFdx5CA7F3lsGmxpwgr865o2ZA/WB0cDmP8ResTEcUe8P1nTXIk+1aOfIRpbDvSmaZqbxkZM1hHN31F1Wd3vlCMgpqVV24JTpZEzmCfwkJWn3AoGAI0HQ8YSy6A294tDZeC4qp3FpKrkm0kl1Ik8DFJoclp+hNYuSVS9Dai1yu5FWzrvZjEk2HsDNIi7wynwubyS+WHOO7NGcFYx5B/bs4KXOQ1UScOapPZOqf1RGuSQrbhyYYZm4AKWU2+w9FmX+cDVnI1nld7c6/OAGbYuNYeqDL/sCgYA78P3UvlMgpFF8IuC4VNkS5IkDIIpIviXgUcK7r805xgM3lx7R4BE5v8iWD+xv5AJv7mpqFzjBDW5apLIFkoP6sye44zrkchW8M9gAYwHis/Gd7Awy+6RQvjQmsh7GkKcPXeFe7LvxD7JoKVyfYFLIlBAJa51enCMGwvC88CE+yQKBgBs35fSOiWfSvt79ufaHZeWbZ7UITKTolQ4weHQp0rXel2g2KiQ0Bb2DamdsIZnzNFYOC8GxtrtPxVxyzxR4XSxpTAKwd3r2qdBQhrNFyWddoGZQhKfnowdOflvrC0VUsB2jQ/2xByhuombd864WO9AFbJ9U/bfHyw+uGpBq+9NQ'

ALI_ALIPAY_PUBLIC_KEY = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAquE3b6JXt9GqE/i3ixAxQ/VSl/zgyxC1Otyg4CA24Ih2vW0OmbieWYUZfj6L6ukyK/1womvDzQ08+cOVn38hqslhjrVIE5VqOCRPya+AFUOY3JMvLma8Mbh9tQQfx61EulnxNhfkK2iNaJVndzQ9/WbOsMnboFNDU1LfxLXNa1ApzIgTi4+lVmEDd5YLysWn5EvOKNvj1z2EbztCu0b0hByzfCdHDZvQ69LyaeBHaYpFSgtTBEMIubUGl3IUWI+bz/evRsRdzaajFywNA0TFg9jfXXva5UrogXdqiB343XdXmcujoQv88zBl2UvBsa+iV9m/NkngCkRmoIT1r/O3SQIDAQAB'