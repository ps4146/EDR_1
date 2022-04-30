import requests
from requests.structures import CaseInsensitiveDict
import json

def updat(auth, id, body):
	f = open(body)
	data= json.load(f)
	f.close()

	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}".format(id)
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth

	resp = requests.patch(api_url, headers = headers, data = data)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass