#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)
