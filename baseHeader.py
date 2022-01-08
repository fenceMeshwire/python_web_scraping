#!/usr/bin/env python3

# baseHeader.py

# Purpose: Change the HTML header to look like a regular request.

# Dependency
import requests

url = 'http://webscrapingfordatascience.com/usercheck/'
baseHeader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

baseRequest = requests.get(url, headers=baseHeader)
statusCode = baseRequest.status_code

# Results
print(statusCode) # 200 OK
print(baseRequest.text) # Welcome, normal user!
print(baseRequest.request.headers) # {...}
