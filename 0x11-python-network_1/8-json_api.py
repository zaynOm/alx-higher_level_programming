#!/usr/bin/python3
"sends a POST request to a url with a letter as a parameter."
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        data = {'q': argv[1]}
        res = requests.post('http://0.0.0.0:5000/search_user', data=data)
        try:
            json = res.json()
            print(f'[{json.get("id")}] {json.get("name")}')
        except requests.exceptions.JSONDecodeError:
            print('Not a valid JSON')
    elif json == {}:
        print('No result')
