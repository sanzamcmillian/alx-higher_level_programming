#!/bin/bash

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
URL=$1

# Send a request to the URL and get the size of the response body in bytes
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

# Display the size of the response body
echo "$SIZE"

