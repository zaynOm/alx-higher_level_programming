#!/usr/bin/python3
"sends a POST request to the passed URL with the email, and displays the body"
from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode())
