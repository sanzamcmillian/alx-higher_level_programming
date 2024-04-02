#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

if 'X-Request-Id' in response.headers:
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)
else:
    print("X-Request-Id header not found in the response.")
