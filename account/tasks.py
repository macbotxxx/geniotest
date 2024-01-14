import requests
import json
from django.conf import settings
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

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from transfer.api.serializers import BankAccountSerilizer 

User = get_user_model()




@celery_app.task()
def obtainAuthToken(email , password):
    """
    this obtain the auth token from geniopay using the
    login details from the user account creation such as 
    email and password .
    """
    try:
        base_url = settings.GENIOPAY_BASE_URL
        path = "/v1/profiles/auth-token"

        url = f"{base_url}{path}"
        response = requests.post(
            url=url,
            headers={
                "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "email": email,
                "password": password
            })
        )
        
        json_response = response.json()
        token = json_response.get("token")
        # updating the user account on geniopay auth token
        accountAuthToken = User.objects.get(email = email)
        accountAuthToken.geniopay_key = token
        accountAuthToken.save()
        # get user account details and store the user ID
        obtainGenioPyaUserID.delay( token , email )
        return "Auth Token Updated Successfully"
        
    except requests.exceptions.RequestException:
        return 'HTTP Request failed'
    



@celery_app.task()
def obtainGenioPyaUserID(token , email ):
    """
    this will obtain the user details from geniopay account endpoint
    and store the user id for 
    accout creation and many more using the geniopay endpoint .
    """
    try:
        base_url = settings.GENIOPAY_BASE_URL
        path = "/v1/profiles/me"

        url = f"{base_url}{path}"
        response = requests.get(
            url=url,
            headers={
                "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Token  {token}",
            },
        )
        
        json_response = response.json()
        userID = json_response.get("id")
        
        # updating the user account on geniopay auth token
        accountUserID = User.objects.filter(email = email).first()
        accountUserID.geniopay_user_id = userID
        accountUserID.save()
        return "User ID Updated Successfully"
        
    except requests.exceptions.RequestException:
        return 'HTTP Request failed'



@celery_app.task()
def getVirtualAccountDetails(  auth_token , account_id , user ):
    """
    this will obtain the user details from geniopay account endpoint
    and store the user id for 
    accout creation and many more using the geniopay endpoint .
    """
    try:
        base_url = settings.GENIOPAY_BASE_URL
        path = f"/v1/accounts/{account_id}"

        url = f"{base_url}{path}"
        response = requests.get(
            url=url,
            headers={
                "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Token  {auth_token}",
            },
        )
        
        json_response = response.json()
        json_string = JSONRenderer().render(json_response)
        byte_stream = BytesIO(json_string)
        data = JSONParser().parse(byte_stream)

        serializer = BankAccountSerilizer(data=data)
        if serializer.is_valid():
            user_instance = User.objects.filter(id = user).first()
            user_profile_instance = serializer.save( account_user = user_instance )
            print(f"UserProfile instance created with ID: {user_profile_instance.id}")
        else:
            print(f"Validation errors: {serializer.errors}")
        return "Usser Account is created"
        
    except requests.exceptions.RequestException:
        return 'HTTP Request failed'




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