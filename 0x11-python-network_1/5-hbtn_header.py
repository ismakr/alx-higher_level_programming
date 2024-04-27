#!/usr/bin/python3
"""Python script that fetches url and return X-Request-Id var"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        print(r.headers['X-Request-Id'])
    except():
        print("None")
