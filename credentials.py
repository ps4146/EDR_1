import configparser
import base64
import json
import requests
from requests.structures import CaseInsensitiveDict

def cred():
	config = configparser.ConfigParser()
	config.read('config.ini')
	base_url = config['Symantec EDR']['base-url']
	client_id = config['Symantec EDR']['client-id']
	client_secret = config['Symantec EDR']['client-secret']

	user_pass = client_id+":"+client_secret
	pass1 = user_pass.encode('utf-8')
	pass2 = base64.b64encode(pass1)

	api_url = base_url+"/atpapi/oauth2/tokens?grant_type=client_credentials&scope=customer"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/x-www-form-urlencoded"
	headers["Authorization"] = "Basic "+pass2.decode()
	headers["Accept"] = "application/json"

	resp = requests.post(api_url, headers=headers, verify=False)
	print(resp.status_code)
	if resp.ok:
		auth = resp.json()['access_token']
		return base_url, auth
	else:
		print("Authorization request failed.")
		return base_url, -1