#!/usr/bin/python3
"sends a request to a URL and displays the value of the variable X-Request-Id"
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
