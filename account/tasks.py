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


@celery_app.task()
def send_email_func():
    #  sending email to the customer alerting him of the succesful order 
    send_mail(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
    )

    return "email sent successful"