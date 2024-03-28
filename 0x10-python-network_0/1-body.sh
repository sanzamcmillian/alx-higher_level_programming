#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -sL -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] &&  curl -sL "$1" || echo "$response"
