import requests
from requests.structures import CaseInsensitiveDict
import json

def updat(bear_token, auth, id, body):
	f = open(body)
	data= json.load(f)
	f.close()

	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}?Authorization=".format(id)+auth
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + bear_token

	resp = requests.patch('http://httpbin.org/post', headers = headers, data = data)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass