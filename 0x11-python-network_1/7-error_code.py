#!/usr/bin/python3
"sends a request to the URL and displays the body of the response"
import requests
from sys import argv

if __name__ == '__main__':
    try:
        response = requests.get(argv[1])
    except requests.HTTPError as e:
        print(f'Error code: {response.status_code}')
