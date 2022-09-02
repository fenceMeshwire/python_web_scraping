#!/usr/bin/env python3

# find_heading.py

# Purpose: Find the <h1>heading</h1> in a given website and transform it into a string.

# Dependencies
from bs4 import BeautifulSoup
import requests

url = 'http://webscrapingfordatascience.com/'
baseHeader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

baseRequest = requests.get(url, headers=baseHeader)
statusCode = baseRequest.status_code

if statusCode == 200:
    htmlContents = baseRequest.text
    bs = BeautifulSoup(htmlContents, 'html.parser')
    docName = bs.select('h1')[0].text.strip()
else:
    print('Cannot get information, please check HTML status code.')

# Result
print('HEADING:', docName)
