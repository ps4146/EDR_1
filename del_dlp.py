import requests
from requests.structures import CaseInsensitiveDict

def updat(auth, id):
	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}".format(id)
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth

	resp = requests.delete(api_url, headers = headers, data = data)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass