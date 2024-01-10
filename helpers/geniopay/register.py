import requests
import json
from .hmac import generate_hmac
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
        'X-HMAC-Signature': generate_hmac(secret_key, body_data, path, method) ,
        'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
