import tkinter as tk
import engine
import config
import os
def download_all():
    web_driver_path=path_text_chrome.get()
    if os.path.exists(web_driver_path):
        engine.fetch_all(web_driver_path)
    else:
        raise Exception("Path doesn't exists")
def update_json():
    web_driver_path=path_text_chrome.get()
    if os.path.exists(web_driver_path):
        base_url=config.base_url
        engine.update_country_json(web_driver_path,base_url)
    else:
        raise Exception("Path doesn't exists")
def download_some():
    web_driver_path=path_text_chrome.get()
    names=names_text.get()
    if os.path.exists(web_driver_path):
        engine.fetch_some(web_driver_path,names)
    else:
        raise Exception("Path doesn't exists")

root=tk.Tk()
h=tk.Label(root,text="Covid scrapper",font=('Arial Bold',10))
h.grid(row=0,column=0)
path_chrome=tk.Label(root,text='''Path to chrome executables''',font=('Arial',10),justify=tk.LEFT)
path_chrome.grid(row=1,column=0)
path_text_chrome=tk.Entry(root,width=80)
path_text_chrome.grid(row=1,column=1)
btn_dnl_all=tk.Button(root,text='Download all',font=('Arial',8),command=download_all)
btn_dnl_all.grid(row=3,column=0)
btn_update_json=tk.Button(root,text='Update json',font=('Arial',8),command=update_json)
btn_update_json.grid(row=3,column=1)
label_names=tk.Label(root,text='Names of countries',font=('Arial',10))
label_names.grid(row=4,column=0)
names_text=tk.Entry(root,width=80,font=('Arial',10))
names_text.grid(row=4,column=1)
btn_dnl_some=tk.Button(root,text='Download Some',font=('Arial',8),command=download_some)
btn_dnl_some.grid(row=5,column=1)
root.mainloop()