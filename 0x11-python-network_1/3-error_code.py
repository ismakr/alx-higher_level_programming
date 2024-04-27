#!/usr/bin/python3
# sends a request to the URL display the body response
# and manage urllib.error.HTTPError
import urllib.request
import sys
try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
