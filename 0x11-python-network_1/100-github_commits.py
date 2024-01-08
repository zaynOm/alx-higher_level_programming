#!/usr/bin/python3
"print last 10 commits from a GitHub repo"
import requests
from sys import argv

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    payload = {'per_page': '10'}
    res = requests.get(url, params=payload)
    for commit in res.json():
        author = commit.get('commit').get('author').get('name')
        print(f"{commit.get('sha')}: {author}")
