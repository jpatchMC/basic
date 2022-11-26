#! /usr/bin/env python3
import requests

try:
    response = requests.get("http://www.google.com")
    response.raise_for_status()

    
    #if response.ok:
    print(type(response))
    print(f"status code: {response.status_code}")
    print(f"text:{response.text[:250]}")
#else:
#    print(f"error")
except Exception as exc:
    print(f"error {exc}")