#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header.
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

if 'X-Request-Id' in response.headers:
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)

