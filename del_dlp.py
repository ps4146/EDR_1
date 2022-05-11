import requests
from requests.structures import CaseInsensitiveDict
import json

def delet(auth, id, api_url):
#	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}".format(id)
	if id is None:
		print("Cannot delete the Deny List Policy without an id")
		return
	api_url = api_url + "/atpapi/v2/policies/deny_list/{}".format(id)
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth

	resp = requests.delete(api_url, headers = headers, verify=False)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass
