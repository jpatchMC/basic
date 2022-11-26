#!/usr/bin/env python3


### 1 ####
pydns = {"server1.testlab.com":"192.168.1.10","server2.testlab.com":"192.168.1.11","server3.testlab.com":"192.168.1.12","server4.testlab.com":"192.168.1.13","server5.testlab.com":"192.168.1.14","server6.testlab.com":"192.168.1.15"}
### 2-4 ###
print(pydns.keys())
print(pydns.values())
print(pydns.items())
### 5 ###

pydns["server7.testlab.com"] = "192.168.1.16"
pydns["server8.testlab.com"] = "192.168.1.17"
### test ###
print(pydns.keys())
print(pydns.values())

print(pydns.get("server2.testlab.com"))
print(pydns.get("server10.testlab.com"))
###print(pydns["server10.testlab.com"]) would give error rather then 0 ###