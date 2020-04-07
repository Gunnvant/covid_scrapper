import plot_utils
import country_info
from datetime import datetime
from tqdm import tqdm
import os
import time
import config
import argparse
import json
def update_country_json(web_driver_path,base_url):
    browser=country_info.get_browser(web_driver_path)
    soup=country_info.get_soup(browser,base_url)
    country_links=country_info.get_country_links(soup)
    with open('country.json', 'w', encoding='utf-8') as f:
        json.dump(country_links, f, ensure_ascii=False, indent=4)
    print("Updated country names and links")
def country_meta():
    con=open("country.json","r")
    data=con.read()
    data=json.loads(data)
    return data
def initialize(web_driver_path):
    now=datetime.now()
    curr_time=now.strftime("%d_%m_%y %H_%M_%S")
    base_path=f"./data/data_{curr_time}"
    os.mkdir(base_path)
    browser=country_info.get_browser(web_driver_path)
    return base_path,browser
def fetch_all(web_driver_path):
    base_path,browser=initialize(web_driver_path)
    country_links=country_meta()
    for name,link in tqdm(country_links.items()):
        browser.get(link)
        time.sleep(2)
        num_charts=plot_utils.get_number_charts(browser)
        d=[]
        for i in range(num_charts):
            d.append(plot_utils.get_chart_data(browser,i))
        plot_utils.writer(name,d,base_path)
def fetch_some(web_driver_path,names):
    country_links=country_meta()
    c_names=[i for i in country_links]
    N=set(names.split(","))
    intersection=set(c_names).intersection(N)
    if len(intersection)==len(N):
        base_path,browser=initialize(web_driver_path)
        stub="https://www.worldometers.info/coronavirus/country/{}"
        for n in tqdm(names.split(",")):
            url=stub.format(country_links[n])
            browser.get(url)
            time.sleep(2)
            num_charts=plot_utils.get_number_charts(browser)
            d=[]
            for i in range(num_charts):
                d.append(plot_utils.get_chart_data(browser,i))
            plot_utils.writer(n,d,base_path)
    else:
        print("Name of countries not provided either as comma separated string or illegal values of country names, see country.json for more info on country names")
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--country',type=str,default='All',help='comma separated list of country names default value is All,\
         see the country.json for valid values of country names')
    parser.add_argument('--update' ,type=str,default='No',help='update country json')
    args = parser.parse_args()
    web_driver_path=config.web_driver_path
    base_url=config.base_url
    if args.country=="All" and args.update=='No':
        fetch_all(web_driver_path)
    if args.country=='All' and args.update=='Yes':
        update_country_json(web_driver_path,base_url)
        fetch_all(web_driver_path)
    if args.country!='All' and args.update=='No':
        names=args.country
        fetch_some(web_driver_path,names)
    if args.country!='All' and args.update=='Yes':
        names=args.country
        update_country_json(web_driver_path,base_url)
        fetch_some(web_driver_path,names)