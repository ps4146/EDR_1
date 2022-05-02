#Creating Deny List policy from json stored on disk
import requests
from requests.structures import CaseInsensitiveDict
import json

def creat(auth, body, api_url):
	f = open(body)
	data= json.load(f)
	f.close()

	#api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth

	resp = requests.post(api_url, headers = headers, data = data)
	print(resp.status_code)
	print()
	print(resp.json())
	id1 = resp.json()['ids'][0]
	with open(id1, 'w') as f1:
		json.dump(resp.json(), f1)