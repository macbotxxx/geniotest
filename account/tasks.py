import requests
from django.contrib.auth import get_user_model
# import Django Packages
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# import celery
from config import celery_app
from celery import shared_task
from celery.schedules import crontab




@celery_app.task( name = "user_details_check" )
def details_checker(*args , **kwargs):
    """
    this constantly check for the user informations on geniopay database
    """
    url = "https://namesearch.geniopay.com/"

    querystring = {
        "q":"Ramon Olorunwa Abbas",
        "json":"on"
        }

    response = requests.request("GET", url, params=querystring)

    print(response.text)



celery_app.conf.beat_schedule = {
    # Execute the background check every 1 minute
    'background-check': {
        'task': 'user_details_check',
        'schedule': crontab(minute='*/1'),
    },
} 