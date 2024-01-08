#!/usr/bin/python3
"Authenticate to GitHub and print the user id"
import requests
from sys import argv

if __name__ == '__main__':
    headers = {'Authorization': f'Bearer {argv[2]}'}
    res = requests.get('https://api.github.com/user', headers=headers)
    print(res.json().get('id'))
