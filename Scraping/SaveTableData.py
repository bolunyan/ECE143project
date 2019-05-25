import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import ast
import os
import time
import itertools as it

def saveDataToCSV(outtables=None, tablenames=None):
    '''
    Save outtables data to CSV Files.
    
    Input:
    outtables: list(list(pandas))
    tablenames: str
    '''
    
    assert isinstance(outtables, list)
    assert all((isinstance(i, list) and all(isinstance(j, pd.DataFrame) for j in i)) for i in outtables)
    
    for num, tables in enumerate(outtables):
        for table in tables:
            column = str(table.columns[0]).split()[0] + '-' + str(table.columns[-1])
            path = 'eiadata/' + tablenames[num] + '/' + column + '.csv'
            print('Saving to ' + path)
            try:
                table.to_csv(path)
            except:
                print('No folder names \'eiadata/\'!')
            print('Successfully saved to ' + path + '!')            