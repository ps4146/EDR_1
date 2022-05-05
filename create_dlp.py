#Creating Deny List policy from json stored on disk
import requests
from requests.structures import CaseInsensitiveDict
import json

def creat(auth, ip, domain, url, md5, sha256, comm, api_url):
	# f = open(body)
	# data= json.load(f)
	# f.close()

	if all([x is None for x in [ip, domain, url, md5, sha256]]):
		print("Need a ip, url, domain, md5 value or sha256 value to create a Deny List Policy")
		return
	if comm is None:
		comm=""
	pol_list = []
	
	if ip is not None:
		pol_list.append({"target_type":"ip", "target_value":ip, "comment":comm})
	if domain is not None:
		pol_list.append({"target_type":"domain", "target_value":domain, "comment":comm})
	if url is not None:
		pol_list.append({"target_type":"url", "target_value":url, "comment":comm})
	if md5 is not None:
		pol_list.append({"target_type":"md5", "target_value":md5, "comment":comm})
	if sha256 is not None:
		pol_list.append({"target_type":"sha256", "target_value":sha256, "comment":comm})
	data = {"verb":"create","policies":pol_list}

	#api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list"
	api_url = api_url + "/atpapi/v2/policies/deny_list"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + auth

	resp = requests.post(api_url, headers = headers, data = data)
	print(resp.status_code)
	print()
	print(resp.json())
	# id1 = resp.json()['ids'][0]
	# with open(id1, 'w') as f1:
	# 	json.dump(resp.json(), f1)