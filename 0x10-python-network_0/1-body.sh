#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
res=$(curl -s -w "%{http_code}" "$1")
status_code=$(echo $res | awk '{print $NF}')

if [[ "$status_code" -eq 200 ]]; then
	echo "$res" | head -1 
fi
