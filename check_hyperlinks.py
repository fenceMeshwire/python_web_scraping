#!/usr/bin/env python3

# check_hyperlinks.py

# Purpose: Checking hyperlinks on a website for availability

# Dependencies
import requests
from selenium import webdriver

driver = webdriver.Firefox()
url = 'http://webscrapingfordatascience.com'
driver.get(url)

driver.implicitly_wait(3)

links = driver.find_elements_by_css_selector('a')

workingLinks = []
notWorkingLinks = []

for link in links:
    try:
        statusCode = requests.head(link.get_attribute('href')).status_code
        hyperlink = link.get_attribute('href')
        if statusCode == 200:
            print('Hyperlink is valid:\t', hyperlink)
            workingLinks.append(hyperlink)
        else:
            print('Hyperlink is invalid:\t', hyperlink)
            notWorkingLinks.append(notWorkingLinks)
    except BaseException as err:
        notWorkingLinks.append(err)
        print(err)

print('These hyperlinks work:')
print(workingLinks)
print()
print("Those hyperlinks dont't work:")
print(notWorkingLinks)

driver.quit()
