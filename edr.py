import argparse
parser = argparse.ArgumentParser(description = "Python script that can retrieve, create or delete Deny List Policies as well as update Deny Policy comments.")
parser.add_argument("option", type = int, help="select 1 for retrieving, 2 for creating, 3 for deleting or 4 for updating Deny List Policies")
parser.add_argument("auth", type = str, help="Please provide Authorization token for accessing the EDR API.")
parser.add_argument("--id", type= str, help="Provide id for either retrieving, updating or deleting Deny List Policy")
parser.add_argument("--ip", type= str, help="Provide IP address for retrieving Deny List Policy with specific IP address")
parser.add_argument("--url", type= str, help="Provide URL for retrieving Deny List Policy with specific URL")
parser.add_argument("--domain", type= str, help="Provide Domain name for retrieving Deny List Policy with specific domain name")
parser.add_argument("--md5", type= str, help="Provide md5 value for retrieving Deny List Policy with specific md5 value")
parser.add_argument("--sha256", type= str, help="Provide sha256 value for retrieving Deny List Policy with specific sha256 value")
parser.add_argument("--next", type= str, help="Provide the value under \"next\" field in the response JSON to retrieve next set of Deny list Policies")
parser.add_argument("--limit", type= int, help="Provide int value of limit for retrieving Deny List Policy")
parser.add_argument("--body", type = str, help= "Provide the path to a JSON object required for Creating or Updating Deny List Policies")

args = parser.parse_args()

match args.option:
case 1:
case 2:
case 3:
case 4:
case _:
	print("Please provide a valid option i.e. 1, 2, 3 or 4 as an argument")