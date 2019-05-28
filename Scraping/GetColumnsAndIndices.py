import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import ast
import os
import time
import itertools as it

def getColumnsAndIndices(chromePath, tablenames, link1, link2):
    '''
    Returns the columns and indices for the EIA data as a dictionary.
    The keys of the dictionary are tablenames, the values are a list of
    ((list of columns) and (list of indices))
    
    Input:
    chromePath: str
    tablenames: list(str)
    link1: str
    link2: str
    
    Output: dict(str: list(list(str), list(str)))
    '''
    
    assert isinstance(chromePath, str)
    assert isinstance(tablenames, list)
    assert isinstance(link1, str)
    assert isinstance(link2, str)
    
    driver = webdriver.Chrome(chromePath)
    monthcoldict = {}
    for tablename in tablenames:
        url = 'https://www.eia.gov/totalenergy/data/browser/?tbl=T' + tablename + '#/?f=M'
        driver.get(url)
        time.sleep(5)
        soup = Soup(driver.page_source)
        myindices = soup.findAll("span", {"class": "description_text_wrapper"})
        mycolumnnames = soup.findAll("span", {"class": "slick-column-name"})
        
        indices = [(i.contents)[0].strip() for i in myindices]
        columns = [(i.contents) for i in mycolumnnames]
        
        months = np.asarray([i[0] for i in list(it.filterfalse(lambda x: str(x) in ['[]', "[\' \']"], columns))])
        monthcoldict[tablename] = [months, indices]
    driver.quit()
    return monthcoldict