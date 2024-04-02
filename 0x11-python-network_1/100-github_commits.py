#!/usr/bin/python3
""" Python script that takes 2 arguments """
import requests
import sys

# Get repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# GitHub API endpoint for retrieving commits
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Parameters to specify that we want only the 10 most recent commits
params = {'per_page': 10}

# Send GET request to the GitHub API
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    # Parse response JSON
    commits = response.json()
    
    # Iterate through each commit and print its SHA and author name
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Error:", response.status_code)

