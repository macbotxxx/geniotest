import hmac
import hashlib


def generate_hmac(secret_key, body, path, method):
    fields_values = [path, method, body, secret_key]
    message = str(fields_values).encode("utf-8")
    return hmac.new(secret_key.encode("utf-8"), msg=message, digestmod=hashlib.sha256).hexdigest()

