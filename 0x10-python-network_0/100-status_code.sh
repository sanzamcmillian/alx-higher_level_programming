#!/bin/bash
#Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
echo "$(curl -w "%{http_code}" -s -o /deev/null "$1")"
