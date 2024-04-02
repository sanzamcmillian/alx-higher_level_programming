#!/usr/bin/python3
""" Python script that takes in a letter. """
import requests
import sys


q = sys.argv[1] if len(sys.argv) > 1 else ""

# URL for the POST request
url = "http://0.0.0.0:5000/search_user"

# Payload for the POST request
payload = {'q': q}

# Send POST request
response = requests.post(url, data=payload)

# Check if response contains valid JSON
try:
    data = response.json()
except ValueError:
    print("Not a valid JSON")
    sys.exit()

# Check if JSON is empty
if not data:
    print("No result")
else:
    print("[{}] {}".format(data['id'], data['name']))
