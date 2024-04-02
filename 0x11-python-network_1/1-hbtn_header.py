#!/usr/bin/python3
""" Python script that takes in a URL. """
import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')

print(request_id)
