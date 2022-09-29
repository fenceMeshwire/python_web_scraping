#!/usr/bin/env python3

# 02_base_header.py

# Purpose: Change the HTML header to look like a regular request.

# Dependency
import requests

url = 'https://www.python.org'
base_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

base_request = requests.get(url, headers=base_header)
status_code = base_request.status_code

# Results
print(status_code) # 200 OK
print(base_request.request.headers) # {...}
