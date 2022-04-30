import argparse
from ret_dlp import retr
from create_dlp import creat
from del_dlp import delet
from updat_dlp import updat
parser = argparse.ArgumentParser(description = "Python script that can retrieve, create or delete Deny List Policies as well as update Deny Policy comments.")
parser.add_argument("option", type = int, help="Select 1 for retrieving, 2 for creating, 3 for deleting or 4 for updating Deny List Policies")
parser.add_argument("auth", type = str, help="Please provide Authorization token for accessing the EDR API.")
parser.add_argument("--id", type= str, help="Provide id for either retrieving, updating or deleting Deny List Policy")
parser.add_argument("--ip", type= str, help="Provide IP address for retrieving Deny List Policy with specific IP address")
parser.add_argument("--url", type= str, help="Provide URL for retrieving Deny List Policy with specific URL")
parser.add_argument("--domain", type= str, help="Provide Domain name for retrieving Deny List Policy with specific domain name")
parser.add_argument("--md5", type= str, help="Provide md5 value for retrieving Deny List Policy with specific md5 value")
parser.add_argument("--sha256", type= str, help="Provide sha256 value for retrieving Deny List Policy with specific sha256 value")
parser.add_argument("--next", type= str, help="Provide the path to a response JSON to retrieve next set of Deny list Policies")
parser.add_argument("--limit", type= int, help="Provide int value of limit for retrieving Deny List Policy")
parser.add_argument("--body", type = str, help= "Provide the path to a JSON object required for Creating or Updating Deny List Policies")

arg = parser.parse_args()

if arg.auth is None:
	print("Please provide the Authorization token for accessing the EDR API.")

if arg.option == 1:
	retr(arg.auth, arg.id, arg.ip, arg.url, arg.domain, arg.md5, arg.sha256, arg.next, arg.limit)
elif arg.option == 2:
	creat(arg.auth, arg.body)
elif arg.option == 3:
	delet(arg.auth, arg.id)
elif arg.option == 4:
	updat(arg.auth, arg.id, arg.body)
elif arg.option is None:
	print("Please provide a valid option i.e. 1, 2, 3 or 4")