import hmac
import hashlib


def generate_custom_hmac(secret_key, body, path, method):
    fields_values = [path, method, body, secret_key]
    message = str(fields_values).encode("utf-8")
    return hmac.new(secret_key.encode("utf-8"), msg=message, digestmod=hashlib.sha256).hexdigest()







secret_key = "cRcpzLRunm5WJt9mRnLySoPdoM2mjFlRcuSOFbB8xOo9kLxW1JQDrT98EjLBQGfh"

body = {
  "email": "latey42691@tanlanav.com",
  "password": "M_Mise83839ws"
}

# body = {
#   "first_name": "Peter",
#   "last_name": "John",
#   "email": "meperid502@pursip.com",
#   "password": "M080341i",
#   "account_type": "PERSONAL",
#   "country": "NG",
#   "time_zone": "Europe/London",
#   "language": "en",
#   "mobile": "+2347067679537",
#   "accept_terms": true,
#   "agreed_to_data_usage": true
# }

path = "/v1/auth/login"
method = "POST"

generate_key = generate_custom_hmac(secret_key, body, path, method)

print(generate_key)


















# headers = {
#     "X-Auth-Client": settings.API_KEY,
#     "X-HMAC-Signature": generate_custom_hmac(secret_key, body, path, 'POST')
# }


# respone = requests.post("/v1/accounts", data=body, headers=headers)