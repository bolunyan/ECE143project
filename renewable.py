from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import imageio

from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import zipfile
import io
import geopandas as gpd
import os
import copy
import math

import scipy.stats
import itertools as it
import ast
import time

#######

#######


def getWikiTables():
    '''
    Reads links in links.txt and returns tables with tables
    in folder name corresponding to name of the wiki page.
    '''
    
    with open('WikiLinks/WikiLinks.txt', 'r') as f:
        links = f.readlines()
    tableLists = []
    for link in links:
        tableLists.append(pd.read_html(link))
    for num1, pageTables in enumerate(tableLists):
        name = links[num1]
        name = name.split('/')[-1].split('\n')[0]
        folder = 'Plot_Data/WikiTables/' + name
        try:
            os.mkdir(folder)
        except:
            pass
        for num2, table in enumerate(pageTables):
            print('Saving file to Plot_Data/WikiTables/' + folder + '/Table' + str(num2))
            table.to_pickle(folder + '/Table' + str(num2))

def get_data_generation_1999_2019():
    '''
        scrap the data for USA Renewable energy generation for 1999-2019
        and save it in folder Plot_Data, then return the pandas
        Dataframe
    '''
    ## Scrap the Data from Internet
    html = urlopen('https://en.wikipedia.org/wiki/Energy_in_the_United_States')
    soup = BeautifulSoup(html.read(),'html.parser')
    tables = soup.find_all('table', {'class':'wikitable'})

    # Search through the tables for the one with the headings we want.
    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        if headings[:4] == ['Year', 'Fossil fuel', 'Nuclear', 'Renewable']:
            break

    # Extract the columns we want and write to a semicolon-delimited text file.
    column_list = ['Year','Coal','Oil','Gas','Subtotal_fossil','Nuclear','Hydro',\
    'Geothermal','Solar','Wind','Wood','Bio_other','Subtotal_renewable', 'Misc','Total']
    energy = pd.DataFrame(index = list(range(20)), columns = column_list)
    data_list = list()
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        Data = [td.text.strip() for td in tds]
        data_list.append(Data)
    data_list = np.array(data_list[0:20])
    count = 0 
    for col in column_list:
        energy[col] = data_list[:,count]
        count += 1
    energy = energy.drop([1,3,5,7,13,18])
    # Edit the wrong data
    energy['Year'][0] = '2018'
    energy.to_csv('Plot_Data/energy_consumpton_USA.csv', index = None, header=True)
    html.close()
    return energy



def get_data_hydro_2004_2018():
    '''
        scrap the data of usa hydro energy generation from 2004-2018
        and save it to the current directory, then return the pandas
        Dataframe
    '''
    html = urlopen('https://en.wikipedia.org/wiki/Hydroelectric_power_in_the_United_States')
    soup = BeautifulSoup(html.read(),'html.parser')
    tables = soup.find_all('table', {'class':'wikitable'})

    # Search through the tables for the one with the headings we want.
    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        if headings[:4] == ['Year', 'Summer capacity']:
            break
    # Extract the columns we want and write to a semicolon-delimited text file.
    column_list = ['Year','Summer Capacity','Electricity Generation','Capacity Factor','Year Growth Capacity',\
                   'Year Growth Produced', 'Portion of Renewable', 'Portion of Total']
    hydro = pd.DataFrame(index = list(range(15)), columns = column_list)
    data_list = list()
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        Data = [td.text.strip() for td in tds]
        data_list.append(Data)

    data_list = np.array(data_list)
    count = 0 
    for col in column_list:
        hydro[col] = data_list[:,count]
        count += 1
    hydro.to_csv (r'Plot_Data/hydro_power_usa.csv', index = None, header=True)
    html.close()
    return hydro

def convert_to_list(pd):
    '''
        convert a string list to float list
    '''
    assert isinstance(pd, list)
    for i in range(len(pd)):
        string = str(pd[i])
        num = string.replace('%','')
        num = num.replace(',','')
        num = float(num)
        pd[i] = num
    return pd

def convert_to_num(string):
    '''
    convert a string to a float number 
    '''
    assert isinstance(string, str)
    string = str(string)
    num = string.replace(',','')
    num = float(num)
    return num

def get_data_hydro_production():
    ''' 
        scrap the data of usa hydro energy generation from 1999-2019
        and save it to the current directory, then return the pandas
        Dataframe
    '''
    html = urlopen('https://en.wikipedia.org/wiki/List_of_U.S._states_by_electricity_production_from_renewable_sources')
    soup = BeautifulSoup(html.read(),'html.parser')
    tables = soup.find_all('table', {'class':'wikitable'})

    # Search through the tables for the one with the headings we want.
    table = tables[0]
    # Extract the columns we want and write to a semicolon-delimited text file.
    column_list = ['Rank','Rank w/o Hydropower','state','with Hydro', 'w/o Hydro','with Hydro(GWH)',\
                   'w/o Hydro(GWH)', 'Total electricity']
    statehydro = pd.DataFrame(index = list(range(51)), columns = column_list)
    data_list = list()
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        Data = [td.text.strip() for td in tds]
        data_list.append(Data)

    data_list = np.array(data_list)
    count = 0 
    for col in column_list:
        statehydro[col] = data_list[:,count]
        count += 1
    statehydro.to_csv (r'Plot_Data/state_hydro_production.csv', index = None, header=True)
    html.close()
    return statehydro

def get_data_hydro_potential():
    '''
        get the data of hydroelectric potential in the USA,
        and save it to the current directory, then return the pandas
        Dataframe
    '''
    hydroPotential = {
        'New Jersey':  549,
        'Rhode Island':   59,
        'Massachusetts':   1197,
        'Connecticut':    922,
        'Maryland':   814,
        'New York':    6711,
        'Delaware':    31,
        'Florida':     682,
        'Ohio':  3046,
        'Pennsylvania':  8368,
        'Illinois':    4883,
        'California':  30024,
        'Hawaii':  2602,
        'Virginia':    3657,
        'Michigan':    1181,
        'Indiana':    2394,
        'North Carolina':  3037,
        'Georgia':     1988,
        'Tennessee':   5745,
        'New Hampshire':   1741,
        'South Carolina':  1889,
        'Louisiana':   2423,
        'Kentucky':   4255,
        'Wisconsin':  2287,
        'Washington':  27249,
        'Alabama':     4103,
        'Missouri':    7198,
        'Texas':   3006,
        'West Virginia':   4408,
        'Vermont':     1710,
        'Minnesota':  1255,
        'Mississippi':   2211,
        'Iowa':  2818,
        'Arkansas':    6093,
        'Oklahoma':    3016,
        'Arizona':     1303,
        'Colorado':    7789,
        'Maine':  3916,
        'Oregon':  18184,
        'Kansas':  2508,
        'Utah':  3528,
        'Nebraska':    3142,
        'Nevada':  846,
        'Idaho':   18758,
        'New Mexico':  1363,
        'South Dakota':  1047,
        'North Dakota':  347,
        'Montana':     14547,
        'Wyoming':      4445,
        'Alaska':     23676}
    column_list = list(hydroPotential.keys())
    potentials = pd.DataFrame(index = list(range(1)), columns = column_list)
    for key,value in hydroPotential.items():
        potentials[key] = value
    potentials.to_csv (r'Plot_Data/hydro_potentials.csv', index = None, header=True)
    return potentials

#########################################################
################Scraping Wind Data#######################
#########################################################


#wind power data from Wikipedia for each state
def wind_data_wiki():
    '''
    scrape wind production data from wikipedia and return as pandas.DataFrame
    '''
    html = urlopen('https://en.wikipedia.org/wiki/Growth_of_wind_power_in_the_United_States')
    soup = BeautifulSoup(html.read(),'html.parser')
    tables = soup.find_all('table', {'class':'wikitable'})

    #Search through the tables for the one with the headings we want
    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        if headings[:4] == ['State', '2015']:
            break

    # Extract the columns we want and write to a semicolon-delimited text file.
    column_list = ['State','2015','2014','2013','2012','2011', '2010', '2009','2008',
                  '2007','2006','2005','2004','2003', '2002', '2001','2000']
    wind = pd.DataFrame(index = list(range(41)), columns = column_list)
    data_list = list()
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        Data = [td.text.strip() for td in tds]
        data_list.append(Data)

    data_list = np.array(data_list)
    count = 0 
    for col in column_list:
        wind[col] = data_list[:,count]
        count += 1
    html.close()
    wind.index=wind['State']
    wind = wind.drop('State',axis=1)
    return wind

def convert_dataframe_with_str_to_float(wind):
    '''
    Convert a dataframe with string values to respective float values
    '''
    assert isinstance(wind, pd.DataFrame)
    index=list(wind.index)+['Alabama','Arkansas','Florida','Georgia','Kentucky','Louisiana',
                        'South Carolina','Mississippi','Virginia']
    wind_float=pd.DataFrame(index=index)
    wind_float.index.name='State'
    for i in range(11):
        wind_float[str(2015-i)]=list(wind[str(2015-i)])+['0','0','0','0','0','0','0','0','0']
        for j in range(len(wind_float[str(2015-i)])):
            wind_float[str(2015-i)][j]=float(wind_float[str(2015-i)][j].replace(',',''))
    return wind_float

def scrape_wind_data_from_wiki():
    '''
    Scrape wind data from wikipedia and store it in the CSV file "Plot_Data/wind_wiki.csv"
    '''
    wind=wind_data_wiki()
    wind_float=convert_dataframe_with_str_to_float(wind)
    wind_float.to_csv('Plot_Data/wind_wiki.csv')
    print('Saved wind wiki data to Plot_Data/wind_wiki.csv')
    return wind_float


#########################################################
#################Scraping EIA Data#######################
#########################################################

def getColumnsAndIndices(chromePath=None, tablenames=None, link1=None, link2=None):
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
    from bs4 import BeautifulSoup as Soup
    
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

#Save EIA Data year wise in a folder
#Above links are used to open certain tables from the tablenames, according to the months and indices extracted above

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
    
    from bs4 import BeautifulSoup as Soup
    
    
    assert isinstance(link1, str)
    assert isinstance(link2, str)
    assert isinstance(inpath, str)
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    
    for year in range(year1, year2+1):
            i = str(year) + str("{:02d}".format(1))
            j = str(year) + str("{:02d}".format(1+11))
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

def getTablesFromEIA(link1=None, link2=None, link3=None, tablenames=None, chromePath=None, year1=None, year2=None):
    '''
    Fetches EIA Tables By Generating Apt Links.
    Uses getTableDataFromEIA as a helper function.
    Saves the data in aptly named txt files.
    
    Input:
    link1: str
    link2: str
    link3: str
    tablenames: list(str)
    chromePath: str
    year1: int
    year2: int
    '''
    assert isinstance(link1, str)
    assert isinstance(link2, str)
    assert isinstance(link3, str)
    assert isinstance(tablenames, list)
    assert all(isinstance(i, str) for i in tablenames)
    assert isinstance(chromePath, str)
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    
    from bs4 import BeautifulSoup as Soup
    
    outtables = []
    try:
        os.mkdir('Plot_Data')
    except:
        pass
    
    try:
        os.mkdir('Plot_Data/eiadata')
    except FileExistsError:
        pass
    
    driver = webdriver.Chrome(chromePath)
    
    for tablename in tablenames:
        foldername = 'Plot_Data/eiadata/'+tablename
        try:
            os.mkdir(foldername)
        except FileExistsError:
            pass
        getTableDataFromEIA(link1+tablename+link2, link3, foldername, driver, year1, year2)
    driver.quit()

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
    from bs4 import BeautifulSoup as Soup
    
    assert isinstance(tablenames, list)
    assert all(isinstance(i, str) for i in tablenames)
    assert isinstance(monthcoldict, dict)
    assert all(isinstance(i, str) for i in monthcoldict.keys())
    assert all(isinstance(i, list) for i in monthcoldict.values())
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    
    outtables = []
    for tablename in tablenames:
        table1 = []
        months = monthcoldict[tablename][0]
        indices = monthcoldict[tablename][1]
        for num, year in enumerate(range(year1, year2+1)):
            i = str(year) + str("{:02d}".format(1))
            j = str(year) + str("{:02d}".format(1+11))
            if year == 2019:
                j = i
            path = 'Plot_Data/eiadata/'+ tablename + '/renewable'+i+'-'+j+'.txt'
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
        

# Saving Data to CSV Files
def saveDataToCSV(outtables=None, tablenames=None):
    '''
    Save outtables data to CSV Files.
    
    Input:
    outtables: list(list(pandas))
    tablenames: str
    '''
    from bs4 import BeautifulSoup as Soup
    
    assert isinstance(outtables, list)
    assert all((isinstance(i, list) and all(isinstance(j, pd.DataFrame) for j in i)) for i in outtables)
    
    for num, tables in enumerate(outtables):
        for table in tables:
            column = str(table.columns[0]).split()[0] + '-' + str(table.columns[-1])
            path = 'Plot_Data/eiadata/' + tablenames[num] + '/' + column + '.csv'
            print('Saving to ' + path)
            try:
                table.to_csv(path)
            except:
                print('No folder names \'Plot_Data/eiadata/\'!')
            print('Successfully saved to ' + path + '!')            


def scrapeEIA():
    '''
    Scrape all EIA Data. Store it in folder Plot_Data/eiadata.
    '''
    from bs4 import BeautifulSoup as Soup
#     Test above written codes

    tablenames = ['10.01', '10.02A', '10.02B', '10.02C', '10.05', '10.06']
    chromePath = r'chromedriver.exe' #Link to Selenium's Automated Chrome Driver
    link1 = '''https://www.eia.gov/totalenergy/data/browser/?tbl=T'''
    link2 = '''#/?f=M&'''
    link3 = '''&charted='''

    #Gets Tablenames
    monthcoldict = getColumnsAndIndices(chromePath, tablenames, link1, link2)

    year1 = 1973
    year2 = 2019

    #link1, link2 and link3 construct the final link to be parsed into Selenium
    getTablesFromEIA(link1, link2, link3, tablenames, chromePath, year1, year2)

    # Extract Data From Above Saved Tables
    outtables = []
    outtables = getDataFromSavedTables(tablenames, monthcoldict, year1, year2)

    #Saves outtables data to csv files
    saveDataToCSV(outtables, tablenames)


###############################################################################
#########################Calculating Solar Potential###########################
###############################################################################


def MakeCSPDataForSolar():
    '''
    Generate Commercial Solar Power dataset.
    Dataset generated from underlying solar datasets from the following sources:
    - NSRDB Website: Dataset for Direct Normal Irradiance
    - Solar2017.xlsx: Commercial Solar Generation Dataset
    '''
    
    file1 = 'nsrdb_v3_0_1_1998_2016_dni.zip' #Downloaded from NSRDB Website
    folder = 'Potential/Solar'

    assert os.path.exists(file1), 'File nsrdb_v3_0_1_1998_2016_dni.zip does not exist. Download from NSRDB Website.'  

    with open(file1, 'rb') as f:
        z = zipfile.ZipFile(io.BytesIO(f.read()))
    try:
        os.mkdir(folder)
    except:
        pass
    
    print('Extracting file: ' + file1 + ' to ' + folder)
    z.extractall(path=(folder+'/')) # extract to folder
    print("Done")
    filelist1 = os.listdir(folder)
    filename1 = [filename for filename in filelist1 if filename.endswith(('shp'))]
    DNIRef = gpd.read_file(folder + '/' + filename1[0]) # Reference File for Geometry Data
    DNIRef.index.name = 'gid'
    print('Dataset Shapefile Found: ' + filename1[0] + '. Projection is: ' + str(DNIRef.crs))

    #############################################################################################

    #Following is the link to the US States TigerFile/Shape Dataset
    # Downloaded from https://ago-item-storage.s3.us-east-1.amazonaws.com/b07a9393ecbd430795a6f6218443dccc/states_21basic.zip?X-Amz-Security-Token=AgoJb3JpZ2luX2VjED8aCXVzLWVhc3QtMSJHMEUCIQDQdpoSuNCbhG6wJlenbUNX2kyLa4sFDMfTsteGQK%2FGjAIgPbTGp4stv7MRiAmVzXkqqgzkdT9EYeeRZqlSrYCPLoAq2gMIVxAAGgw2MDQ3NTgxMDI2NjUiDOTLwnU9a645VeeQ9Cq3A6egVUMTRTy5hc5I%2BRhU3eBLbQ6Kw692uZmVqMv%2FcnUD4N7OwUcwJshtuR5%2BWlW4IbtD195j7DeKyB26c3zbBFnSAltQWTSfe6IqTVl0%2BtSa9BJyhzocmGoybOpV5XOO%2Bi4Q1NbZnvQsdooHnVaPL1B3pjuEiQZcVi%2BCZ%2F%2FTjd7KQh3aao0cGhBRTO3iJVFFi1ix4m4jsQ%2BWwdEjyCf4NivvTmUJtdoFues1j0yD15u1hL5QeF8i%2BB3B3FpNQGOKGh3wTcti%2BIDCChbTnGUp0ScXVSv%2BYSJB08JDDAn9NbDPpuchJvT2JydOyS89HA7sF2m2aeaZ1msTqZc1tRxjf%2BavIuQ%2Froz%2BcXNfwvSXFGUKqkKdlZiikoI8QYy6Ds7oxRTl8Zjv1%2FaVehLVtmaykgg5seSgBEl8n9YbHQgmQAjr5OTCJtLKRP2NqKLu79EUojR%2Fa%2BIO5JLNGFmlPVpBn0ALtUn57cUHC9EckkuesWWUN6C%2FUEr5ukyMUxFp%2B%2BU5fnF9p%2FzqyLi%2FKQaJyJXVU4QEaq%2BdIwXPweCTZzQtgk%2BB%2FO2cjxi58pcv2HN8uT200J4CmXwe2VIw2sK45wU6tAED0Xyqflp6flORpmLbasEMEZzHfzCsGJCOn%2FbebpgRVBy66uqxNIq8u%2F88kd70ys14o%2Byz1J%2FaI0TiYSh2FoEPntjnrLltX62ZFIiDrRIUGcnCdXT7%2Bxa9wB0ZB7VCYtocE4BgoaQL7SnF8roTmvloXh1zW10GL7gK7wg83WLVloY8pwlZ8kUGm8WLFAVEaEb0yUnz1pXq05bStAqo1haecQ26roRFIFFC%2B%2BBaSnHNlSEsciE%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190529T065735Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYZTTEKKEWR5RPRVV%2F20190529%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=54040bc54e4d15f5a9edc1423b8c43d6f890a057bd51be4da17f97edc80872fa'
    file2 = 'states_21basic.zip'
    folder2 = 'Potential/States/'

    assert os.path.exists(file2), 'File ' + file2 + ' does not exist!'

    with open(file2, 'rb') as f:
        z = zipfile.ZipFile(io.BytesIO(f.read()))

    try:
        os.mkdir(folder2)
    except:
        pass

    print('Extracting file: ' + file2 + ' to ' + folder2)
    z.extractall(path=(folder2+'/')) # extract to folder
    print("Done")
    filelist2 = os.listdir(folder2)
    filename2 = [filename for filename in filelist2 if filename.endswith(('shp'))]
    States = gpd.read_file(folder2 + '/' + filename2[0]) # Reference File for Geometry Data
    print('Dataset Shapefile Found: ' + filename2[0] + '. Projection is: ' + str(States.crs))

    ###############################################################################################

    # Following dataset downloaded from NSRDB Website: https://maps.nrel.gov/nsrdb-viewer/

    print('Reading data from CSV Files...')

    DNITables = {}
    folder3 = 'Potential/Solar/NSRDB-YearWise/'
    for year in range(2001, 2017):
        filename3 = folder3 + 'nsrdb_v3_0_1_' + str(year) + '_dni.csv'
        print(filename3)
        DNITables[year] = gpd.GeoDataFrame(pd.read_csv(filename3))

    DNITablesMerged = DNIRef

    print('Merging Data with Original Reference File...')

    for i in range(2001, 2017):
        currTable = DNITables[i]
        currTable.dni = currTable.dni.astype('float64')
        currTable.gid = currTable.gid.astype('int64')
        currTable.gid = (currTable.gid - 1) # Zero indexing
        currTable = currTable.rename(columns={'dni': str(i)})
        currTable = currTable.drop(columns=['FID'])
        DNITablesMerged = DNITablesMerged.merge(currTable, on='gid')
        print('Done merging original reference with ' + str(i) + ' data.')
    DNITablesMerged.set_index('gid', inplace=True)
    DNITablesMerged.drop(columns=['DNI'], inplace=True)
    print('Done with merging all!')

    #####################################################################################################

    DesiredStates = States.loc[::, ['STATE_NAME', 'STATE_ABBR', 'geometry']]
    DesiredStates = DesiredStates.to_crs(DNITablesMerged.crs)
    print('Merging GeoPandas Data for DNI with State Boundaries...')
    FinalMergedData = gpd.overlay(DNITablesMerged, DesiredStates, how='intersection')
    print('Merged Final Data Successfully...')

    print('Converting Table CRS to meters (3395 EPSG)...')
    FinalMergedData = FinalMergedData.to_crs({'init': 'epsg:3395'})
    print('Modified CRS is: ' + str(FinalMergedData.crs))
    a = list(States['STATE_ABBR'])
    CapFacs = {
        'AZ': 0.304,
        'CA': 0.281,
        'NV': 0.279,
        'CO': 0.273,
        'NM': 0.269,
        'TX': 0.230,
        'GA': 0.225,
        'TN': 0.210,
        'NC': 0.200,
        'FL': 0.200,
        'DE': 0.199,
        'IN': 0.194,
        'MD': 0.192,
        'IL': 0.190,
        'NY': 0.185,
        'OH': 0.184,
        'NJ': 0.175,
        'PA': 0.159
    }
    for state in a:
        if state not in CapFacs.keys():
            CapFacs[state]=0.150 # Default Capacity Factor

        CSPArea = pd.DataFrame(columns=list(CapFacs.keys()), index=list(range(2001, 2017)), dtype='float64')

    print('Calculating Net Area for CSP Calculations...')
    for state in list(CapFacs.keys()):
        temp = FinalMergedData[FinalMergedData['STATE_ABBR'] == state]
        tempSeries = []
        for year in range(2001, 2017):
            print('Calculating for Year: ' + str(year) + ' in state: ' + state)
            temp1 = temp[temp[str(year)] >= 5].area #Only consider with DNI >= 5 kWh/m2/day
            temp1 = math.fsum(temp1)/10**6
            tempSeries.append(temp1)
        CSPArea[state] = (tempSeries)

    CSPArea.index.name = 'Year'
    TargetFolder = 'Potential/Solar/'

    try:
        os.mkdir(TargetFolder)
    except:
        pass
    print('Saving merged area data for Direct Normal Irradiance dataset...')
    CSPArea.to_csv(TargetFolder + 'CSP_Area_km2_1998_2016.csv')

    try:
        CSPArea.set_index(['Year'], inplace=True)
    except:
        pass

    #####################################################################################################
    CSPPotential = pd.DataFrame(columns=list(CapFacs.keys()), index=list(range(2001, 2017)), dtype='float64')


    for state in CapFacs.keys():
        CSPPotential[state] = CSPArea[state] * 32.895 * CapFacs[state] * 8760

    print('Saving Maximum Potential to ' + TargetFolder + ' ...')
    CSPPotential.to_csv(TargetFolder + 'MaximumPotential.csv')

    print('Now calculating for actual energy production!')

    ActualData = pd.read_excel('Potential/Solar/Solar2017.xlsx', skiprows=1) # Online Dataset for Commercial Solar Power (CSP), Downloaded from "https://www.eia.gov/electricity/data/eia860/xls/eia8602017.zip"
    ActualData = ActualData[ActualData['State'].isin(list(CapFacs.keys()))] # States in consideration
    ActualData = ActualData[ActualData['Technology'] == 'Solar Photovoltaic'] # Used for large CSPs
    ActualData['Net Energy'] = ActualData['Nameplate Capacity (MW)'] * 8760

    ActualEnergy = pd.DataFrame(columns=list(CapFacs.keys()), index=list(range(2001, 2017)))

    for state in CapFacs.keys():
        temp = ActualData[ActualData['State'] == state]
        tempSeries = []
        for year in range(2001, 2017):
            temp1 = math.fsum(temp[temp['Operating Year'] == year]['Net Energy'])
            tempSeries.append(temp1)
        ActualEnergy[state] = (tempSeries)

    print('Saving Actual Energy Production to ' + TargetFolder + ' ...')
    ActualEnergy.to_csv(TargetFolder + 'ActualPotential.csv')

    print('Calculating and Saving Percentage of Potential Achieved...')

    try:
        os.mkdir(TargetFolder)
    except:
        pass

    PercentPot = (ActualEnergy/CSPPotential) * 100
    PercentPot.to_csv(TargetFolder + 'PercentPotential.csv')

    print('Successfully calculated and saved all metrics in Potential/Solar ...')

###############################################################################
#########################Calculating Wind Potential############################
###############################################################################


def CalcWindPotential():
    '''
    Scrapes Wind Energy Data to calculate Maximum Potential,
    Actual Energy Achieved and Percentage Potential Achieved.
    Saves Output in CSV Files.
    
    --------
    Example:
    >>> CalcWindPotential()
    
    'Wind Energy Database ShapeFile...'
    Shape of the dataframe: (59338, 25)
    Projection of dataframe: {'init': 'epsg:4269'}
    
    'US States Database ShapeFile...'
    Shape of the dataframe: (51, 6)
    Projection of dataframe: {'init': 'epsg:4269'}
    Successfully saves all data. Output files are at 'Wind/Wind_Potential_AllStates.csv', 'Wind/Wind_ActualEne_AllStates.csv' and 'Wind/Wind_Percent_AllStates.csv'
    '''
    file1 = 'uswtdbSHP.zip' #Downloaded from NSRDB Website
    folder = 'Potential/Wind'

    assert os.path.exists(file1), 'File uswtdbSHP.zip does not exist. Download from WindExchange Website.'  

    with open(file1, 'rb') as f:
        z = zipfile.ZipFile(io.BytesIO(f.read()))
    try:
        os.mkdir(folder)
    except:
        pass
    
    print('Extracting file: ' + file1 + ' to ' + folder)
    z.extractall(path=(folder+'/')) # extract to folder
    print("Done")
    
    windcopy = gpd.read_file('Potential/Wind/uswtdb_v2_0_20190417.shp')
    print('Wind Energy Database ShapeFile...')
    print("Shape of the dataframe: {}".format(windcopy.shape))
    print("Projection of dataframe: {}".format(windcopy.crs))

    states = gpd.read_file('Potential/States/states.shp')
    print('US States Database ShapeFile...')
    print("Shape of the dataframe: {}".format(states.shape))
    print("Projection of dataframe: {}".format(states.crs))

    windcopy = windcopy.rename(columns={'t_state':'State Code', 't_hh': 'Height', 'p_cap':'ProjCap', 't_cap':'TurbineCap', 'p_year':'Year'})
    windcopy = windcopy[windcopy['Height'] >= 80]          # Potential Measured only for Turbines with Height more than 80m
    windcopy = windcopy[windcopy['ProjCap'] >= 0]
    shp1 = len(windcopy['ProjCap'])
    x = scipy.stats.truncnorm((0.121 - 0.345)/0.224, (0.569 - 0.345)/0.224, loc=0.345, scale=0.224) # # 0.345 +- 0.224 km2/MW :: https://www.nrel.gov/docs/fy09osti/45834.pdf
    windcopy['Area'] = windcopy['ProjCap'] * x.rvs(shp1)
    yearlist = sorted(list(set(windcopy['Year'])))
    dropColumns = ['case_id', 'faa_ors', 'faa_asn', 'usgs_pr_id', 't_county', 't_fips', 'p_name', 'p_tnum', 't_manu', 't_model', 't_rd', 't_rsa', 't_ttlh', 't_conf_atr', 't_conf_loc', 't_img_date', 't_img_srce', 'xlong', 'ylat']    
    windcopy = windcopy.drop(labels=dropColumns, axis=1)
    #Energy Potential = Power density (5MW/m2) * Capacity factor (25.5%) * 8760 (hours/year) / 1000 (converting to GWh)
    windcopy['Energy Potential'] = windcopy['Area'] * 5 * 0.255 * 8760 / 1000
    windcopy['Actual'] = windcopy['ProjCap'] * 0.255 * 8760 / 1000

    EnergyPot = pd.DataFrame(columns=sorted(set(windcopy['Year'])), index=sorted(set(windcopy['State Code'])))
    EnergyPot.iloc[:, :] = 0
    EnergyPot.index.name = 'State Code'

    ActualEne = pd.DataFrame(columns=sorted(set(windcopy['Year'])), index=sorted(set(windcopy['State Code'])))
    ActualEne.iloc[:, :] = 0
    ActualEne.index.name = 'State Code'

    for state in set(windcopy['State Code']):
        temp = windcopy[windcopy['State Code'] == state]
        for year in range(1999, 2019):
            temp1 = temp[temp['Year'] == year]
            sum1 = math.fsum(temp1['Energy Potential'])
            sum2 = math.fsum(temp1['Actual'])
            EnergyPot.loc[state, year] = sum1
            ActualEne.loc[state, year] = sum2

    PercentPot = ActualEne/EnergyPot
    PercentPot = PercentPot.fillna(0)
    PercentPot = (PercentPot*100).astype(int)

    for state in (list(states['STATE_ABBR'])):
        if state not in ActualEne.index:
            ActualEne.loc[state] = np.repeat(0.0, 2018-1999+1)
        if state not in EnergyPot.index:
            EnergyPot.loc[state] = np.repeat(0.0, 2018-1999+1)
        if state not in PercentPot.index:
            PercentPot.loc[state] = np.repeat(0.0, 2018-1999+1)
    try:
        os.mkdir('Potential/Wind')
    except:
        pass
    
    EnergyPot.to_csv('Potential/Wind/Wind_Potential_AllStates.csv')
    ActualEne.to_csv('Potential/Wind/Wind_ActualEne_AllStates.csv')
    PercentPot.to_csv('Potential/Wind/Wind_Percent_AllStates.csv')
    
    print('Successfully saved all data. Output files are at \'Potential/Wind/Wind_Potential_AllStates.csv\', \'Potential/Wind/Wind_ActualEne_AllStates.csv\' and \'Potential/Wind/Wind_Percent_AllStates.csv\'')