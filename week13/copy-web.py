#! /usr/bin/env python3
import requests
#Josh Patch, trying to save a webpage locally
try:
    response = requests.get("https://notpurple.com")
    with open ("My_Web_File.html" , "w") as hfile:
        hfile.write(response.text)

except Exception as exc:
    print(f"error {exc}")