#!/usr/bin/python3
""" Python script that takes your GitHub credentials. """
import requests
import sys

# GitHub username and personal access token
username = sys.argv[1]
password = sys.argv[2]

# URL for the GitHub API to get user information
url = "https://api.github.com/user"

# Send GET request with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check if request was successful
if response.status_code == 200:
    # Parse response JSON
    user_data = response.json()
    # Display user id
    print("Your GitHub user id:", user_data['id'])
else:
    print("Error:", response.status_code)
