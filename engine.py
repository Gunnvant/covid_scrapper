import plot_utils
import country_info
from datetime import datetime
from tqdm import tqdm
import os
import time
import config
web_driver_path=config.web_driver_path
base_url=config.base_url
now=datetime.now()
curr_time=now.strftime("%d_%m_%y %H_%M_%S")
base_path=f"./data/data_{curr_time}"
os.mkdir(base_path)
browser=country_info.get_browser(web_driver_path)
soup=country_info.get_soup(browser,base_url)
country_links=country_info.get_country_links(soup)
for name,link in tqdm(country_links.items()):
    browser.get(link)
    time.sleep(2)
    num_charts=plot_utils.get_number_charts(browser)
    d=[]
    for i in range(num_charts):
        d.append(plot_utils.get_chart_data(browser,i))
    plot_utils.writer(name,d,base_path)