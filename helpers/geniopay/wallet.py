import requests
import json
import uuid
from django.conf import settings
from account.tasks import getVirtualAccountDetails

random_uuid = uuid.uuid4()
random_uuid_str = str(random_uuid)

def createWallet(auth_token , user_id , user, data_body ):
    # Create Virtual Account
    # POST https://api.geniopay.com/v1/accounts
    base_url = settings.GENIOPAY_BASE_URL
    secret_key = settings.GENIOPAY_SECRET_KEY
    path = "/v1/accounts"

    url = f"{base_url}{path}"
    method = "POST"

    print(auth_token)
    print(user_id)
    print(data_body)
    print(random_uuid_str)

    try:
        response = requests.post(
            url=url,
            headers={
                "X-Auth-Client": settings.GENIOPAY_CLIENT_KEY,
                "Authorization": f"Token  {auth_token}",
                "X-IDEMPOTENCY-KEY": f"{random_uuid_str}",
                "Content-Type": "application/json; charset=utf-8",
                
            },
            data=json.dumps({
                "friendly_name": data_body.get("friendly_name"),
                "currency":  data_body.get("currency"),
                "default":  data_body.get("default"),
                "user":  f"{user_id}"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        
        res = response.json()
        print(res.get("id"))
        # testing
        getVirtualAccountDetails.delay( auth_token = auth_token , account_id = res.get("id") , user = user)
        return response
    
    except requests.exceptions.RequestException:
        print('HTTP Request failed')




def getWalletBalance():
    pass