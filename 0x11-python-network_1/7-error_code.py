#!/usr/bin/python3
"""If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
