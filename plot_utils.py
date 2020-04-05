
import pandas as pd
import os
js1='return Highcharts.charts[{}].series[0].xAxis.categories'
js2='return Highcharts.charts[{}].series[0].yData'
js3='return Highcharts.charts[{}].renderTo.id'

def get_chart_data(browser,chart_idx):
    data=dict()
    data['x']=browser.execute_script(js1.format(chart_idx))
    data['y']=browser.execute_script(js2.format(chart_idx))
    data['title']=browser.execute_script(js3.format(chart_idx))
    return data

def get_number_charts(browser):
    js='return Highcharts.charts.length'
    num=browser.execute_script(js)
    return num
def writer(country,data,base_path):
    w=pd.ExcelWriter(f'{os.path.join(base_path,country)}.xlsx', engine='xlsxwriter')
    for d in data:
        title=d['title']
        x=d['x']
        y=d['y']
        table=pd.DataFrame({"X":x,"Y":y})
        table.to_excel(w,sheet_name=title)
    w.close()