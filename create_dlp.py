#Creating Deny List policy from json stored on disk
import requests
from requests.structures import CaseInsensitiveDict
import json

def creat(bear_token, auth, body):
	f = open(body)
	data= json.load(f)
	f.close()

	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list?Authorization="+auth
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + bear_token

	resp = requests.post('http://httpbin.org/post', headers = headers, data = data)
	print(resp.status_code)
	print()
	print(resp.json())
	id1 = resp.json()['ids'][0]
	with open(id1, 'w') as f1:
		json.dump(resp.json(), f1)