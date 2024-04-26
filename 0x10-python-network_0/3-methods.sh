#!/bin/bash
#sends a DELETE request to the URL
curl -i -l -s -X OPTIONS "$1" | grep "Allow" | cut -d ":" -f2 | cut -c2-
