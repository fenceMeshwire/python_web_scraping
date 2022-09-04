#!/usr/bin/env python3

# Python 3.9.5

# 01_get_html_code.py

# Dependency
import requests

url = 'https://www.python.org'

response = requests.get(url)

if response.status_code == 200:
    html = response.text

print(html)
