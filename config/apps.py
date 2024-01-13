
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_celery_beat",

    # third apps 
    'account.apps.AccountConfig',
    'transfer.apps.TransferConfig',
]




