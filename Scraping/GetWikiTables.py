import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import urllib.request as ulib
import ast
import os
import numpy as np
import pandas as pd
import unicodedata
import re
import time

def getWikiData(driver, URL):
    driver.get(URL)
    time.sleep(5)
    elements = driver.find_elements_by_class_name('mw-collapsible-text')
    for element in elements:
        element.click()
#     a=input()
    page = driver.page_source
    soup = Soup(page)
    desiredText = soup.findAll('table')
    captions = []
    for num, table in enumerate(desiredText):
        try:
            captions.append(table.find('caption').contents[0])
        except:
            captions.append('No Caption: %d' %num)
    return (captions, desiredText)

def getTablesFromLinks(links):
    for link in links:
        print(link)
        foldername = link.split('/')[-1]
        print(foldername)
        try:
            os.mkdir(foldername)
        except:
            pass
        chromePath = r'C:\Users\swapn\Documents\CSE 237D\drone_dataset\chromedriver.exe'
        print(chromePath)
        driver = webdriver.Chrome(chromePath)
        captions, tables = getWikiData(driver, link)
        nTables = []
        for i, table in enumerate(tables):
            for tag in table.findAll(['sup', 'span', 'a']):
                tag.replaceWith('')
            filename = captions[i]
            try:
                filename = (re.sub('[^\w\s-]', '', filename).strip().lower())
                filename = (re.sub('[-\s]+', '-', filename))
            except:
                filename = ('caption' + str(i))
            
            try:
                pd.read_html(table.prettify())[0].to_csv(foldername+'//'+filename+'.csv')  
            except:
                try:
                    pd.read_html(table.prettify()).to_csv(foldername+'//'+filename+'.csv')
                except:
                    print('Failed at' + str(filename))