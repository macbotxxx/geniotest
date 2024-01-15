from hashlib import pbkdf2_hmac

def wallet_encrypted_key(pin):
    app_iters = 500_000  
    dk = pbkdf2_hmac('sha256', b'pin', b'bad salt' * 2, app_iters)
    return dk.hex()