#!/usr/bin/python3
# Python script that fetches url and return X-Request-Id var
import requests
import sys
r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
