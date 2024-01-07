#!/usr/bin/python3
"sends a POST request to the passed URL with the email, and displays the body"
import requests
from sys import argv

if __name__ == '__main__':
    data = {'email': argv[2]}
    response = requests.post(argv[1], data=data)
    print(response.text)
