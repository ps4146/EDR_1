import configparser
import base64
import json

def cred():
	config = configparser.ConfigParser()
	config.read('config.ini')
	base_url = config['Symantec EDR']['base-url']
	client_id = config['Symantec EDR']['client-id']
	client_secret = config['Symantec EDR']['client-secret']

	user_pass = client_id+":"+client_secret
	user_pass = user_pass.encode('utf-8')
	pass2 = base64.base64encode(pass1)

	api_url = base_url+"?grant_type=client_credentials&scope=customer"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/x-www-form-urlencoded"
	headers["Authorization"] = "Basic "+pass2

	resp = requests.post(api_url, headers=headers)
	auth = resp.json()['token']['access_token']
	return base_url, auth