#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X OPTIONS -i "$1" | grep -i "allow:" | sed 's/Allow: //' | tr ',' '\n' | tr -d '\r'
