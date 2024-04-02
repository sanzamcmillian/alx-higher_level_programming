#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    body = response.text
    print("\t- type:", type(body))
    print("\t- content:", body)
else:
    print("Error:", response.status_code)

