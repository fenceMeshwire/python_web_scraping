#!/usr/bin/env python3

# Python 3.9.5

# 06_data_extraction_from_ul_and_div.py

# Dependencies:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import os

# ____________________________________________________________________________________________________
EXPORT_PATH = "/..."
DRIVER_PATH = "/..."
os.chdir(EXPORT_PATH)
edge_options = Options()
edge_options.add_argument("--disable-extensions")
driver = webdriver.Edge(executable_path=DRIVER_PATH)

url = "https://app.traderepublic.com/"
driver.implicitly_wait(5)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# ____________________________________________________________________________________________________
ul_pf = soup.find("ul", {"class": "portfolioInstrumentList"})

result_pf = {}
for li in ul_pf.find_all('li'):
    id = li.get('id')
    name = li.find("span", {"class":"instrumentListItem__name"})
    name = name.text
    price = li.find("span", {"class":"instrumentListItem__currentPrice"})
    price = price.text
    price = price.replace("\xa0", " ")
    result_pf[id] = (name, price)

pf = pd.DataFrame.from_dict(result_pf, orient='index', columns=['name','price'])
pf.to_csv('portfolio.csv', sep=';', encoding='utf8', index=True, header=False)

# ____________________________________________________________________________________________________
div_pl = soup.find("div", {"class": "positionsList"})

result_pf_qty = {}
for li in div_pl.find_all("div", {"class": "instrumentListItem__info"}):
    # print(li)
    name = li.find("span", {"class":"instrumentListItem__name"})
    name = name.text
    qty = li.find("span", {"class":"tag instrumentListItem__sharesTag"})
    qty = qty.text
    cur_price = li.find("span", {"class":"instrumentListItem__currentPrice"})
    cur_price = cur_price.text
    cur_price = cur_price.replace("\xa0€", "")
    cur_price = cur_price.replace(".", "")
    result_pf_qty[name] = (qty, cur_price)

pf_qty_cur_price = pd.DataFrame.from_dict(result_pf_qty, orient='index', columns=['qty','cur_price'])
pf_qty_cur_price.to_csv('portfolio_qty_cur_price.csv', sep=';', encoding='utf8', index=True, header=False)
# ____________________________________________________________________________________________________

pf = pd.read_csv('portfolio.csv', sep=";")
pf_qty = pd.read_csv('portfolio_qty_cur_price.csv', sep=";")

pf = pf.drop('price', axis=1)
df = pf.merge(pf_qty, on='name', how='left')

ttl = df['total'].sum()
df['per'] = df['total'].div(ttl).round(4)

df.to_csv('portfolio_summary.csv', sep=';', encoding='utf8', columns=list(df.columns), index=False, header=True)
# ____________________________________________________________________________________________________

driver.quit()
