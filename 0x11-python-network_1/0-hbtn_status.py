#!/usr/bin/python3
import urllib.request
from pprint import pprint
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    page = response.read()
    if "utf-8" in str(response.headers.get('Content-Type')):
        check = "ok"
    else:
        check = ""
    print("Body response:\n\t- type: {}\n\t- content: {}\
          \n\t- utf8 content: {}".format(type(response.read()), page, check))
