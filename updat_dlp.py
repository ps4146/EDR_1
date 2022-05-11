import requests
from requests.structures import CaseInsensitiveDict
import json

def updat(auth, id, comm, api_url):
	# f = open(body)
	# data= json.load(f)
	# f.close()

	if id is None:
		print("Cannot update the Deny List Policy without an id")
		return
#	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list/{}".format(id)
	api_url = api_url+ "/atpapi/v2/policies/deny_list/{}".format(id)
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth
	data = {"op":"replace","path":"/comment","value":comm}

	resp = requests.patch(api_url, headers = headers, data = data, verify=False)
	print(resp.status_code)
	print()
	try:
		print(resp.json())
	except:
		pass