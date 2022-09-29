#!/usr/bin/env python3

# 04_find_heading.py

# Purpose: Find the <h1>heading</h1> in a given website and transform it into a string.

# Dependencies
from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org//'
base_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

base_requests = requests.get(url, headers=base_header)
status_code = base_requests.status_code

if status_code == 200:
    htmlContents = base_requests.text
    bs = BeautifulSoup(htmlContents, 'html.parser')
    doc_name = bs.select('h1')[0].text.strip()
else:
    doc_name = None
    print('Cannot get information, please check HTML status code.')

# Result
print('HEADING:', doc_name)
