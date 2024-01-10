#!/bin/bash
# sends a JSON POST request to a URL, and displays the body of the response.
curl -sX POST --json "$(cat "$2")" "$1"
