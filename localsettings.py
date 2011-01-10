# localsettings.py is never shared between developers or machines. Therefore
# it must be added localsettings.py to .gitignore or .hgignore 
# Do not copy stuff from settings.py blindly, only override the settings that
# need to be overriden.

LOCAL_DEV = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_db_name',
        'USER': 'local_db_user',
        'PASSWORD': 'local_db_password',
        'HOST': '',
        'PORT': '',
    }
}


# Do not override INSTALLED_APPS or MIDDLEWARE_CLASSES from settings.py(unless
# you are 100% sure that you want to do).
LOCAL_APPS = (

)

LOCAL_MIDDLEWARE_CLASSES = (

)
