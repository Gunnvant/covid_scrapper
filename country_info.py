from selenium import webdriver 
import os
from bs4 import BeautifulSoup
import numpy as np
import platform
def get_browser(web_driver_path):
    if platform.system()=='Windows':
        curr_dir=os.getcwd()
        os.chdir(web_driver_path)
        browser=webdriver.Chrome()
        os.chdir(curr_dir)
    else:
        browser = webdriver.Chrome(web_driver_path)
    return browser
def get_soup(browser,base_url):
    browser.get(base_url)
    html=browser.page_source
    soup=BeautifulSoup(html,'html.parser')
    return soup
def get_country_links(soup):
    stub="https://www.worldometers.info/coronavirus/{}"
    tables=soup.find_all("table",attrs={'id':'main_table_countries_today'})
    rows=tables[0].find_all("tr")
    country_links={}
    for row in rows[1:]:
        r1c1=row.find_all("td")[0]
        country=r1c1.text.strip()
        try:
            link=r1c1.a['href']
        except:
            continue
        country_links[country]=stub.format(link)
    return country_links