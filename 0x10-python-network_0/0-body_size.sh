#!/bin/bash
#takes in a URL, sends a request to that URL, and displays
#the size of the body of the response
curl -s --head "$1" | grep -w "Content-Length:" | cut -d " " -f2
