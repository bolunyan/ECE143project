import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import ast
import os
import time
import itertools as it

def getTableDataFromEIA(link1=None, link2=None, inpath=None, driver=None, year1=None, year2=None):
    '''
    Returns tabledata from EIA website by generating the appropriate link.
    Saves the returned data in an aptly names file.
    
    Input:
    link1: str
    link2: str
    inpath: str
    driver: selenium.webdriver object
    year1: int
    year2: int
    '''
    assert isinstance(link1, str)
    assert isinstance(link2, str)
    assert isinstance(inpath, str)
    assert isinstance(driver, webdriver)
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    
    for year in range(year1, year2+1):
            i = str(year) + str("{:02d}".format(month))
            j = str(year) + str("{:02d}".format(month+11))
            link3 = 'start='+i+'&end='+j
            if year == 2019:
                j=i
            driver.get(link1+link3+link2)
            time.sleep(5)
            html = driver.page_source
            soup = Soup(html)
            elements = soup.findAll('div', {'class' : ['slick-cell l3 r3', 'slick-cell l4 r4', 'slick-cell l5 r5', 'slick-cell l6 r6', 'slick-cell l7 r7', 'slick-cell l8 r8', 'slick-cell l9 r9', 'slick-cell l10 r10', 'slick-cell l11 r11', 'slick-cell l12 r12', 'slick-cell l13 r13', 'slick-cell l14 r14']})                           
            collist = []
            for element in elements:
                collist.append(element.contents)

            path = inpath + '/renewable'+i+'-'+j+'.txt'
            with open(path, 'w') as f:
                print('Saving data for ' + i + ' to ' + j + ' to path ' + path)
                f.write(str(collist))
                
def getDataFromSavedTables(tablenames=None, monthcoldict=None, year1=None, year2=None):
    '''
    Save data from saved txt files into list of pandas objects.
    
    Input:
    tablenames: list(str)
    monthcoldict: dict(str: list(list(str), list(str)))
    year1: int
    year2: int
    
    Output: list(list(pandas))
    '''
    
    assert isinstance(tablenames, list)
    assert all(isinstance(i, str) for i in tablenames)
    assert isinstance(monthcoldict, dict)
    assert all(isinstance(i, str) for i in monthcoldict.keys())
    assert all(isinstance(i, list) for i in monthcoldict.values())
    assert all(isinstance(i, list) for i[0] in j for j in monthcoldict.values())
    assert all(isinstance(i, list) for i[1] in j for j in monthcoldict.values())
    assert all(isinstance(i, list) for i in j[0] for j in k for k in monthcoldict.values())
    assert all(isinstance(i, list) for i in j[1] for j in k for k in monthcoldict.values())
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    
    outtables = []
    for tablename in tablenames:
        table1 = []
        months = monthcoldict[tablename][0]
        indices = monthcoldict[tablename][1]
        for num, year in enumerate(range(year1, year2+1)):
            i = str(year) + str("{:02d}".format(month))
            j = str(year) + str("{:02d}".format(month+11))
            if year == 2019:
                j = i
            path = 'eiadata/'+ tablename + '/renewable'+i+'-'+j+'.txt'
            with open(path, 'r') as f:
                lista = f.read()
                f.close()
            listb = ast.literal_eval(lista)
            
            listc = []
            
            for i in listb:
                if (len(i) > 0) and (i != ['NA']) and (i != ['-']) and (i != ['NM']): # Neutralizing empty data
                    listc.append(i[0])
                else:
                    listc.append(0)
            
#             try:
            listc = np.array(listc).astype(float)
            listc = listc.reshape(len(indices), -1)
#             except Exception as e:
#             print(e)
#             print(tablename, year, listc)
            
            try:
                table1.append(pd.DataFrame(data=listc, columns=months[(12*num):(12*(num+1))], index=indices))
            except ValueError as e:
                if(listc.shape[1] > 1):
                    listc = listc[::, 0:1].reshape(1, -1).flatten()
                table1.append(pd.DataFrame(data=listc, columns=months[(12*num):(12*(num+1))], index=indices))
        outtables.append(table1)
    return outtables
        