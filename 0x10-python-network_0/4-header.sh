#!/bin/bash
#sends a GET request to the URL
curl -s -X "GET" --header "X-School-User-Id: 98" "$1"
