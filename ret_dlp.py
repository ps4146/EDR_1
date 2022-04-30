#Retrieving deny list policies, with arguments passed to the API.
import requests
from requests.structures import CaseInsensitiveDict
import json

def retr(bear_token, auth, id, ip, url, dom, md5, sha256, nxt, lim):
	nxt_str = ""
	if nxt is not None:
		f = open(nxt)
		data= json.load(f)
		nxt_str=data['next']
		f.close()

	api_url = "https://192.168.1.15/atpapi/v2/policies/deny_list?Authorization="+auth
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "Bearer " + bear_token

	if id is not None:
		api_url= api_url+"&id="+id
	if ip is not None:
		api_url= api_url+"&ip="+ip
	if url is not None:
		api_url= api_url+"&url="+url
	if dom is not None:
		api_url= api_url+"&domain="+dom
	if md5 is not None:
		api_url= api_url+"&md5="+md5
	if sha256 is not None:
		api_url= api_url+"&sha256="+sha256
	if nxt_str is not "":
		api_url= api_url+"&next="+nxt_str
	if lim is not None:
		api_url= api_url+"&limit="+lim

	resp = requests.post(url, headers=headers)
	print(resp.status_code)
	print()
	print(resp.json())
	nxt_1 = resp.json()['next']
	with open(nxt_1, 'w') as f1:
		json.dump(resp.json(), f1)