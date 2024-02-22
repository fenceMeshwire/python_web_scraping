#!/usr/bin/env python3

# Python 3.9.5

# 05_html_table_to_csv.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import os

# Export file location
EXPORT_PATH = "C:\\Users\\...\\storage"
# Webdriver file location
DRIVER_PATH = "C:\\Users\\...\\msedgedriver.exe"
# Change directory to export file location
os.chdir(EXPORT_PATH)

edge_options = Options()
edge_options.add_argument("--disable-extensions")
driver = webdriver.Edge(executable_path=DRIVER_PATH)

url = "https://sample.com"

driver.implicitly_wait(5)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.select_one('#id...')
table = pd.read_html(str(div))
filename = 'data_export.csv'
table[0].to_csv(filename, sep=';', encoding='utf-8')

driver.quit()
