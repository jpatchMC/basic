#! /usr/bin/env python3
import requests

try:
    response = requests.get("http://www.madisoncollege.edu")
    response.raise_for_status()

    
    print(type(response))
    print(f"status code: {response.status_code}")
    print(f"text:{response.text[:250]}")
    print(f"Headers: {response.headers}")
    
    for key,value in response.headers.items():
        print(f"{key} :{ value}")

except Exception as exc:
    print(f"error {exc}")