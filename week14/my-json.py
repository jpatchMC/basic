#!/usr/bin/env python3
import requests
import json
import argparse

parser = argparse.ArgumentParser(description="This is a json grabber for provided IP")
parser.add_argument('-ip','--IPaddy',dest='IP',help="Enter an IP address, any type", type=str)
args = parser.parse_args()
IP4 = (args.IP)
print(IP4)

response = requests.get(f"https://ipinfo.io/{IP4}/json")
json_dict = json.loads(response.text)

#print(json.dumps(json_dict["data"], indent=4))
#print(json.dumps(json_dict, indent=4))#whole thing
#print(json.dumps(json_dict["data"]["id"], indent=4))#just the id line in data
#print(response.text)
#print(type(response.text))

for key in json_dict:
    print(f"{key} : {json_dict[key]}")
#    for lvl2key in json_dict[key]:
#        print(F"second level key {lvl2key} and value is: {json_dict[key][lvl2key]}")