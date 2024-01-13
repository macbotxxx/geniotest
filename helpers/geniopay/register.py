import requests
import json
from .security import generate_custom_hmac
from django.conf import settings


def genioRegister( body_data , password ):
        """
        this registers the user with geniopay endpoint
        """

        base_url = settings.GENIOPAY_BASE_URL
        secret_key = settings.GENIOPAY_SECRET_KEY
        path = "/v1/profiles"

        url = f"{base_url}{path}"
        method = "POST"
        payload = json.dumps({
                "first_name": body_data.get("first_name"),
                "last_name": body_data.get("last_name"),
                "email": body_data.get("email"),
                "password": password,
                "account_type": body_data.get("account_type"),
                "country": body_data.get("country"),
                "time_zone": body_data.get("time_zone"),
                "language": body_data.get("language"),
                "mobile": body_data.get("mobile"),
                "accept_terms": body_data.get("accept_terms"),
                "agreed_to_data_usage": body_data.get("agreed_to_data_usage")
                })
        
        headers = {
        'X-Auth-Client': settings.GENIOPAY_CLIENT_KEY,
        'X-HMAC-Signature': generate_custom_hmac(secret_key, body_data, path, method),
        'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response


        

def verifyEmail( body_data ):
        base_url = settings.GENIOPAY_BASE_URL
        path = "/v1/profiles/verify-email-address"
        url = f"{base_url}{path}"
        method = "POST"

        try:
                response = requests.post(
                url=url,
                headers={
                        "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
                        "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                        "key": body_data.get("key")
                })
                )

                return response.json()
        
        except requests.exceptions.RequestException:
                print('HTTP Request failed')
                return response.json()



def getAccountID(body_data):
        base_url = settings.GENIOPAY_BASE_URL
        secret_key = settings.GENIOPAY_SECRET_KEY
        path = "/v1/profiles/login"

        url = f"{base_url}{path}"
        method = "POST"

        payload = {
        "email": "meperid502@pursip.com",
        "password": "M080341i"
        }
        headers = {
        "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
        "X-HMAC-Signature": generate_custom_hmac(secret_key, body_data, path, method)
        }

        response = requests.request(method, url, json=payload, headers=headers)

        print(response.text)


def getAccountDetails(body_data):

        url = "https://api.geniopay.com/v1/profiles/me"

        response = requests.request("GET", url)

        print(response.text)
