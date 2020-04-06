"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 1.11.24.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import env
import dj_database_url

#  So to actually use our env.py variables, we have to put import env at the top of our settings.py file. And that will import the entire file, and therefore, allow us access to our environmental variables.



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# cloud 9 would be: [os.environ.get('c9_HOSTNAME')]
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

# So within settings under INSTALLED_APPS, we have to put in django_forms_bootstrap in order for that to work. i had to pip install django-forms-bootstrap 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'accounts',
    'products',
    'cart',
    'checkout',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

#  And because we now have multiple templates folders, we need to specify in our settings that all directories called templates potentially contain templates.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
        },
    },
]

# in the above templates, context_processors are a list of things that are available on every webpage

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Yeah that's normal. working in development mode, you have to work on sqlite3 db. But when you go to Heroku, it'll be postgres db so you'll lose all database details and superuser, have to create fresh on postgres. 

# when i migrate the database from dbsqlite(local) to postgres (production) i had a problem migrating when inputting the ususal python manage.py makemigrations. So i was told by a tutor to select option 2 then input 'python manage.py migrate --run-syncdb'

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# This is something you did in the Django auth app. By adding these in, you should now have login capability.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 'accounts.backends.CaseInsensitiveAuth'
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# We're going to add in to our settings our STATICFILES_DIRS. And this is just a path to show that any directory called static can contain static files.
STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, "static"),
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# add in the stripe publishable key
# WE ARE GOING TO create an environment variable called STRIPE_PUBLISHABLE and same for STRIPE_SECRET. The reason we're using environment variables is we don't want these keys, particularly the secret key, to be visible to any of our users. Otherwise, they would be able to hack into our account.
# So OS, by meaning operating system, means whatever computer this is running on. So in this case right now, it's our computer, so we're going to have to create a new file called env.py at the top level of our project. 
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Now, this is purely to fix an issue that you have with Cloud9. Dont know what this means
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'





