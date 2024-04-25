#!/bin/bash
#takes in a URL, sends a request to that URL, and displays
#the size of the body of the response
curl -s --head 100.25.45.81 | grep "Content-Length:" | cut -d " " -f2
