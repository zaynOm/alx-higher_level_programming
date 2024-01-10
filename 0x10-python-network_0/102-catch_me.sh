#!/bin/bash
# sends a JSON POST request to a URL, and displays the body of the response.
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
