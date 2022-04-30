import requests
from requests.structures import CaseInsensitiveDict

def updat(bear_token, auth, id):
	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}?Authorization=".format(id)+auth
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + bear_token

	resp = requests.delete('http://httpbin.org/post', headers = headers, data = data)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass