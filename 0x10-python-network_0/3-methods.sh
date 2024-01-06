#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | sed -n '/^Allow: /{s///;p}'
