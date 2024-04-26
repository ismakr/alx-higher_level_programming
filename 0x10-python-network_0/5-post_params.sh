#!/bin/bash
#sends a POST request to the URL
curl -s -X "POST" -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -d "" "$1"
