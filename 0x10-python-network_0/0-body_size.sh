#!/bin/bash
#takes in a URL, sends a request to that URL, and displays
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
