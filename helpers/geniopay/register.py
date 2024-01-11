import requests
import json
from .security import generate_custom_hmac
from django.conf import settings


def genioRegister( body_data ):

        base_url = settings.GENIOPAY_BASE_URL
        secret_key = settings.GENIOPAY_SECRET_KEY
        path = "/v1/accounts"

        url = f"{base_url}{path}"
        method = "POST"

        payload = json.dumps(body_data)

        headers = {
        'X-Auth-Client': settings.GENIOPAY_CLIENT_KEY,
        'X-HMAC-Signature': generate_custom_hmac(secret_key, body_data, path, method) ,
        'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        status_code = response.status_code
        status_message = response.text
        print(status_code , status_message)

        return status_code,status_message


        
