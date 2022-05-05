import argparse
from ret_dlp import retr
from create_dlp import creat
from del_dlp import delet
from updat_dlp import updat
from credentials import cred
parser = argparse.ArgumentParser(description = "Python script that can retrieve, create or delete Deny List Policies as well as update Deny Policy comments.")
parser.add_argument("option", type = int, help="Select 1 for retrieving, 2 for creating, 3 for deleting or 4 for updating Deny List Policies")
#parser.add_argument("auth", type = str, help="Please provide Authorization token for accessing the EDR API.")
parser.add_argument("--id", type= str, help="Provide id for either retrieving, updating or deleting Deny List Policy")
parser.add_argument("--ip", type= str, help="Provide IP address for retrieving or creating Deny List Policy with specific IP address")
parser.add_argument("--url", type= str, help="Provide URL for retrieving or creating Deny List Policy with specific URL")
parser.add_argument("--domain", type= str, help="Provide Domain name for retrieving or creating Deny List Policy with specific domain name")
parser.add_argument("--md5", type= str, help="Provide md5 value for retrieving or creating Deny List Policy with specific md5 value")
parser.add_argument("--sha256", type= str, help="Provide sha256 value for retrieving or creating Deny List Policy with specific sha256 value")
parser.add_argument("--next", type= str, help="Provide the path to a response JSON to retrieve next set of Deny list Policies")
parser.add_argument("--limit", type= int, help="Provide int value of limit for retrieving Deny List Policy")
parser.add_argument("--comment", type= int, help="Provide a comment for creating or updating Deny List Policies")
# parser.add_argument("--body", type = str, help= "Provide the path to a JSON object required for Creating or Updating Deny List Policies")

arg = parser.parse_args()

#if arg.auth is None:
#	print("Please provide the Authorization token for accessing the EDR API.")

# config = configparser.ConfigParser()
# config.read('config.ini')
# base_url = config['Symantec EDR']['base-url']
# client_id = config['Symantec EDR']['client-id']
# client_secret = config['Symantec EDR']['client-secret']

base_url, auth = cred()
if auth == -1:
	pass
elif arg.option == 1:
	retr(auth, arg.id, arg.ip, arg.url, arg.domain, arg.md5, arg.sha256, arg.next, arg.limit, base_url)
elif arg.option == 2:
	creat(auth, arg.ip, arg.domain, arg.url, arg.md5, arg.sha256, arg.comment, base_url)
elif arg.option == 3:
	delet(auth, arg.id, base_url)
elif arg.option == 4:
	updat(auth, arg.id, arg.comment, base_url)
elif arg.option is None:
	print("Please provide a valid option i.e. 1, 2, 3 or 4")