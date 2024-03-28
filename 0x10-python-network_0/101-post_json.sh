#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
if [ $# -ne 2 ]; then echo "Usage: $0 <URL> <JSON_FILE>"; exit 1; fi; curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
