import numpy as np
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
from plotly.graph_objs import *
import plotly.plotly as py
plotly.tools.set_credentials_file(username='swaggarw', api_key='lNDGDRwz0l5VtiHflnJZ')
init_notebook_mode(connected=True)
import matplotlib.pyplot as plt
import math
import matplotlib.pylab as plb
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import imageio
plt.style.use('seaborn-whitegrid')

def Plot_Renewable_All():
    '''
    
    '''
    
    ## Pie Chart for Renewable Energy Consumption in the United States
    Renew = pd.read_csv('Plot_Data/energy_consumpton_USA_2000-2018.csv')
    Renew = Renew.sort_values('Year')
    Renew = Renew.set_index('Year')
    Renew.columns.name = 'Source'
    Renew = Renew.iloc[::, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12]]
    Renew = Renew.rename(columns={'Bio_other':'Biomass+'})
    # Renew

    trace1 = {
      "direction": "counterclockwise", 
      "domain": {
        "x": [0, 0.375], 
        "y": [0, 0.9]
      }, 
      "hole": 0.18, 
      "hoverinfo": "percent+label", 
      "labels": list(Renew.columns), 
      "name": "2008",
      "title": "2008",
      "titlefont":{"size":20},
      "opacity": 1, 
      "rotation": -50, 
      "showlegend": True, 
      "sort": True, 
      "textfont": {
        "color": "rgb(73, 68, 68)", 
        "size": 10
      }, 
      "textinfo": "label+percent", 
      "textposition": "auto", 
      "type": "pie", 
      "values": list(Renew.loc[2008]), 
    }
    trace2 = {
      "direction": "counterclockwise", 
      "domain": {
        "x": [0.5, 0.875], 
        "y": [0, 0.9]
      }, 
      "hole": 0.18, 
      "hoverinfo": "percent+label", 
      "labels": list(Renew.columns), 
      "name": "2018",
      "title": "2018",
      "titlefont":{"size":20},
      "rotation": 15, 
      "showlegend": True, 
      "sort": True, 
      "textfont": {
        "color": "rgb(50, 49, 49)", 
        "size": 10
      }, 
      "textinfo": "label+percent", 
      "textposition": "auto", 
      "type": "pie", 
      "values": list(Renew.loc[2018]), 
    }
    data = Data([trace1, trace2])
    layout = {
      "autosize": True,
      "colorway": ["#4c78a8", "#f58518", "#e45756", "#72b7b2", "#54a24b", "#eeca3b", "#b279a2", "#ff9da6", "#9d755d", "#bab0ac"], 
      "dragmode": "zoom", 
      "font": {"family": "Overpass"}, 
      "hoverlabel": {"font": {
          "family": "Droid Sans", 
          "size": 15
        }}, 
      "legend": {
        "x": 1, 
        "y": 0.7199999999999998, 
        "borderwidth": 1, 
        "font": {"size": 10}, 
        "xanchor": "left"
      }, 
      "margin": {
        "t": 75, 
        "b": 80
      }, 
      "paper_bgcolor": "rgb(255, 255, 255)", 
      "showlegend": True, 
      "title": {
        "x": 0.50, 
        "font": {"size": 36}, 
        "text": "Energy Production in the US (TWh)"
      }, 
      "xaxis": {
        "autorange": True,
        "range": [-1, 6]
      }, 
      "yaxis": {
        "autorange": True, 
        "range": [-1, 4]
      }
    }
    fig = Figure(data=data, layout=layout)
    iplot(fig, filename='Plots/Renewable_All_2008_2018', image_height=1080, image_width=1920)
    
def Plot_Renewable():
    '''
    
    '''
    
    ## Pie Chart for Renewable Energy Consumption in the United States
    Renew = pd.read_csv('Plot_Data/energy_consumpton_USA_2000-2018.csv')
    Renew = Renew.sort_values('Year')
    Renew = Renew.set_index('Year')
    Renew.columns.name = 'Source'
    Renew = Renew.rename(columns={'Bio_other':'Biomass+', 'Subtotal_fossil': 'Fossil (Total)', 'Subtotal_renewable':'Renewable Energy'})   
    Renew = Renew.iloc[::, [0, 1, 2, 11, 12]]

    trace1 = {
      "direction": "clockwise", 
      "domain": {
        "x": [0, 0.4], 
        "y": [0, 0.9]
      }, 
      "hole": 0.18,
      "pull": 0.02,  
      "hoverinfo": "percent+label", 
      "labels": list(Renew.columns), 
      "name": "2008",
      "title": "2008",
      "titlefont":{"size":20},
      "opacity": 1, 
      "rotation": 150, 
      "showlegend": True, 
      "sort": True, 
      "textfont": {
        "color": "rgb(73, 68, 68)", 
        "size": 20
      }, 
      "textinfo": "label+percent", 
      "textposition": "outside", 
      "type": "pie", 
      "values": list(Renew.loc[2008]), 
    }
    trace2 = {
      "direction": "counterclockwise", 
      "domain": {
        "x": [0.6, 1], 
        "y": [0, 0.9]
      }, 
      "hole": 0.18,
      "pull": 0.02,
      "hoverinfo": "percent+label", 
      "labels": list(Renew.columns), 
      "name": "2018",
      "title": "2018",
      "titlefont":{"size":20},
      "rotation": 0, 
      "showlegend": False, 
      "sort": True, 
      "textfont": {
        "color": "rgb(50, 49, 49)", 
        "size": 20
      }, 
      "textinfo": "label+percent", 
      "textposition": "outside", 
      "type": "pie", 
      "values": list(Renew.loc[2018]), 
    }
    data = Data([trace1, trace2])
    layout = {
      "autosize": True,
      "colorway": ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2", "#54a24b", "#eeca3b", "#b279a2", "#ff9da6", "#9d755d", "#bab0ac"], 
      "dragmode": "zoom", 
      "font": {"family": "Overpass"}, 
      "hoverlabel": {"font": {
          "family": "Droid Sans", 
          "size": 15
        }}, 
      "legend": {
        "x": 1, 
        "y": 0.5, 
        "borderwidth": 1, 
        "font": {"size": 14}, 
        "xanchor": "left"
      }, 
      "margin": {
        "t": 75, 
        "b": 80
      }, 
      "paper_bgcolor": "rgb(255, 255, 255)", 
      "showlegend": False, 
      "title": {
        "x": 0.50,
        "y":0.95,
        "font": {"size": 45, "family": "Trebuchet MS"}, 
        "text": "<b>Energy Production in the US (TWh)</b>"
      }, 
      "xaxis": {
        "autorange": True,
        "range": [-1, 6]
      }, 
      "yaxis": {
        "autorange": True, 
        "range": [-1, 4]
      }
    }
    fig = Figure(data=data, layout=layout)
    iplot(fig, filename='plots/Renewable_2008_2018', image_height=720, image_width=1080)
    
def plot_pieChart_renewable(source, year):
    '''
        plot the pie chart of the energy source of given year
    '''
    assert isinstance(source, pd.DataFrame)
    assert isinstance(year, str)
    assert 2007<= int(year)<=2018 or int(year) == 2000 or int(year) == 1999
    
    index = source.Year[source.Year == year].index.tolist()[0]
    energySource = {
    'Coal': convert_to_num(source['Coal'][index]),
    'Natural Gas': convert_to_num(source['Gas'][index]),
    'Renewable Energy': convert_to_num(source['Subtotal_renewable'][index]),
    'Oil': convert_to_num(source['Oil'][index]),
    'Electricity Import': convert_to_num(source['Misc'][index]),
    'Nuclear': convert_to_num(source['Nuclear'][index])
    }
    # Data to plot
    plt.figure(figsize=(15,8))
    labels = energySource.keys()
    sizes = energySource.values()
    explode = (0, 0, 0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    patches, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, \
                            autopct='%1.1f%%', shadow=True, startangle = 90)
    plt.legend(labels, loc="best")
    plt.setp(texts, size=12, weight="bold", color = 'black')
    plt.setp(autotexts, size=12, weight="bold", color = 'white')
    plt.title('Energy Sources, ' + year,fontsize = 20, fontweight='bold')
    plt.axis('equal')
    plt.show()
    
def GetElectricityTrends():
    '''
    
    '''
    
    Table1 = pd.read_pickle('Plot_Data/WikiTables/List_of_U.S._states_by_electricity_production_from_renewable_sources/Table0')
    Table1 = Table1.iloc[1::, [2, 3, 5]]
    Table1 = Table1.sort_values(('State', 'State'))
    Table1 = Table1.set_index(('State', 'State'))
    Table1.index.name = 'State'

    Table2 = pd.read_pickle('Plot_Data/WikiTables/List_of_states_and_territories_of_the_United_States_by_population/Table0')
    Table2 = Table2.iloc[::, [2, 3]]
    Table2 = Table2.sort_values('Name')
    Table2 = Table2.set_index('Name')
    Table2.index.name = 'State'
    Table2 = Table2[Table2.index.isin(Table1.index)]

    Table3 = pd.read_pickle('Plot_Data/WikiTables/List_of_U.S._states_and_territories_by_area/Table0')
    Table3 = Table3.iloc[::, [0, 3]]
    Table3 = Table3.sort_values(('Unnamed: 0_level_0', 'Statefederal district or territory'))
    Table3 = Table3.set_index(('Unnamed: 0_level_0', 'Statefederal district or territory'))
    Table3.index.name = 'State'
    Table3 = Table3[Table3.index.isin(Table1.index)]

    Table4 = pd.read_pickle('Plot_Data/WikiTables/List_of_U.S._state_budgets/Table0')
    Table4 = Table4.iloc[::, [0, 1]]
    Table4 = Table4.set_index('State')
    Table4 = Table4.sort_values('State')
    Table4 = Table4[Table4.index.isin(Table1.index)]
    Table4

    Table1['Population'] = Table2.iloc[::, 0]
    Table1['Area'] = Table3.iloc[::, 0]
    Table1['Budget'] = Table4.iloc[::, 0]
    Table1['logArea'] = [math.log10(i) for i in Table1['Area']]
    Table1['logPop'] = [math.log2(i) for i in Table1['Population']]

    Table1.index = Table1.index.astype(str)
    return Table1

def PlotEnergyArea(Table1=None):
    '''
    
    '''
    
    my_dpi=200
    plt.style.use('seaborn-whitegrid')

    plotTable = Table1.sort_values('logArea')
    plotTable = plotTable.iloc[::, [-2, 1]]

    fig, ax = plt.subplots(figsize=(1500/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(plotTable['logArea'], plotTable[('Renewable Electricity', 'with Hydro(GW•h)')], linewidth=2, alpha=0.7)

    plt.grid(b=True)
    ax.annotate('Oregon', (plotTable.loc['Oregon']), ha='center')
    ax.annotate('California', (plotTable.loc['California']))
    ax.annotate('Washington', (plotTable.loc['Washington']), ha='right')
    ax.annotate('New York', (plotTable.loc['New York']), ha='right')

    ax.set_title('Renewable Production vs log(Area)', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("log$_{10}$(Area(km$^2$)) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', rotation=0, labelsize=10, width=3)
    ax.set_ylabel("Production (GWh) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/AreaVsProd.png', bbox_inches='tight')
    plt.style.use('seaborn-whitegrid')
    ax.spines['bottom'].set_color('0')
    ax.spines['top'].set_color('0')
    ax.spines['right'].set_color('0')
    ax.spines['left'].set_color('0')
    
def PlotEnergyBudget(Table1=None):
    '''
    
    '''
    
    my_dpi=200

    plotTable = Table1.sort_values('Budget')
    plotTable = plotTable.iloc[::, [-3, 1]]

    fig, ax = plt.subplots(figsize=(1500/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(plotTable['Budget'], plotTable[('Renewable Electricity', 'with Hydro(GW•h)')], color='xkcd:azure', linewidth=2, alpha=0.7)

    plt.grid(b=True)
    ax.annotate('OR', (plotTable.loc['Oregon']), ha='center')
    ax.annotate('CA', (plotTable.loc['California']), ha='right')
    ax.annotate('WA', (plotTable.loc['Washington']), ha='right')
    ax.annotate('NY', (plotTable.loc['New York']), ha='center', va='top')
    ax.annotate('TX', (plotTable.loc['Texas']), ha='left')
    ax.annotate('OH', (plotTable.loc['Ohio']), ha='left', va='top')
    ax.annotate('FL', (plotTable.loc['Florida']), ha='left', va='top')
    ax.annotate('OK', (plotTable.loc['Oklahoma']), ha='center', va='bottom')

    ax.set_title('Renewable Production vs Budget (billions $)', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("Budget (billions \$) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', rotation=0, labelsize=10, width=3)
    ax.set_ylabel("Production (GWh) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/BudgetVsProd.png', bbox_inches='tight')
    plt.style.use('seaborn-whitegrid')

    ax.spines['bottom'].set_color('0')
    ax.spines['top'].set_color('0')
    ax.spines['right'].set_color('0')
    ax.spines['left'].set_color('0')
    
def PlotEnergyPop(Table1=None):
    '''
    
    '''
    my_dpi=200

    plotTable = Table1.sort_values('logPop')
    plotTable = plotTable.iloc[::, [-1, 1]]

    fig, ax = plt.subplots(figsize=(1500/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(plotTable['logPop'], plotTable[('Renewable Electricity', 'with Hydro(GW•h)')],linewidth=2, alpha=0.7)

    plt.grid(b=True)
    ax.annotate('OR', (plotTable.loc['Oregon']), ha='center')
    ax.annotate('CA', (plotTable.loc['California']), ha='right')
    ax.annotate('WA', (plotTable.loc['Washington']), ha='center')
    ax.annotate('NY', (plotTable.loc['New York']), ha='right')
    ax.annotate('TX', (plotTable.loc['Texas']), ha='right')
    ax.annotate('OH', (plotTable.loc['Ohio']), ha='left', va='top')
    ax.annotate('NC', (plotTable.loc['North Carolina']), ha='center', va='bottom')
    ax.annotate('NJ', (plotTable.loc['New Jersey']), ha='right', va='top')
    ax.annotate('FL', (plotTable.loc['Florida']), ha='left', va='top')

    ax.set_title('Renewable Production vs log(Population)', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("log$_{2}$(Population) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', rotation=0, labelsize=10, width=3)
    ax.set_ylabel("Production (GWh) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/PopVsProd.png', bbox_inches='tight')
    plt.style.use('seaborn-whitegrid')
    plotTable['logPop']
    ax.spines['bottom'].set_color('0')
    ax.spines['top'].set_color('0')
    ax.spines['right'].set_color('0')
    ax.spines['left'].set_color('0')

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

def plot_bar_hydro(hydro):
    '''
        plot the bar chart of hydro electric ratio 
    '''
    assert isinstance(hydro, pd.DataFrame)
    plt.figure(figsize=(15,7))
    #get year
    year = list(hydro['Year'])[::-1]
    #get portion of total
    percent_hydro = list(hydro['Portion of Total'])[::-1]
    percent_hydro = convert_to_list(percent_hydro) 
    # get other_renewable portion 
    percent_other_renewable = list(hydro['Portion of Renewable'])[::-1]
    percent_other_renewable = convert_to_list(percent_other_renewable) 
    percent_other_renewable = np.array(percent_hydro) / np.array(percent_other_renewable) * 100 - np.array(percent_hydro)
    # get fossil 
    percent_fossil = 100 - percent_other_renewable - np.array(percent_hydro)

    bar_width = 1 
    # positions of the left bar-boundaries
    bar_l = [i for i in range(len(year))] 
    # positions of the x-axis ticks (center of the bars as bar labels)
    tick_pos = [i+(bar_width/2) for i in bar_l]
    plt.style.use('seaborn-whitegrid')
    # Create a bar chart 
    plt.bar(bar_l, percent_fossil, label='Fossil', alpha=0.9, color='xkcd:golden yellow', width=bar_width, edgecolor='black', tick_label = year)
    plt.bar(bar_l, percent_other_renewable, bottom = percent_fossil, label='Other_renewable', alpha=0.9, color='xkcd:light sea green', width=bar_width,edgecolor='black')
    plt.bar(bar_l, percent_hydro, bottom = percent_other_renewable + percent_fossil, label='Hydro', alpha=0.9, color='xkcd:deep sky blue', width=bar_width,edgecolor='black')

    for v in range(len(percent_hydro)):
        value = '%0.1f' % percent_hydro[v]
        plt.text(x = v-0.3, y = 96, s = value + '%', color='white', fontweight='bold',fontsize =10)

    plt.legend(['Fossil','Others','Hydro'], loc="best", fontsize=16)
    plt.title('Portion of Hydropower, 2004-2018', fontsize=24, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel("Percentage",fontsize=14)
    my_dpi=200
    plt.savefig('plots/Hydro_2004_2018.png', figsize=(1500/my_dpi, 1000/my_dpi), dpi=my_dpi)
    plt.show()
    plt.style.use('seaborn-whitegrid')
#     plt.savefig('plots/Hydro_2004_2018.png')
    
def plot_bar_hydro_state(statehydro):
    '''
        plot the bar chart of hydroelectricity production by states at 2017
    '''
    assert isinstance(statehydro, pd.DataFrame)
    renew = list(statehydro['with Hydro(GWH)'])
    renew = convert_to_list(renew) 
    woHydro = list(statehydro['w/o Hydro(GWH)'])
    woHydro = convert_to_list(woHydro)
    hydro = np.array(renew) - np.array(woHydro)
    hydro = hydro[1:]
    state = list(statehydro['state'])[1:]
    hydro_dict = dict(zip(state,hydro))
    hydro_dict = sorted(hydro_dict.items(), key = lambda x:x[1], reverse = True)
    hydro_dict = dict(hydro_dict)
    # Plot the bar chart
    state = list(hydro_dict.keys())
    plt.figure(figsize=(15,7))
    plt.bar(range(len(state)), hydro_dict.values(), width=1, \
            tick_label = state, edgecolor = 'black') # plot features importances
    text = sorted(hydro,reverse = True)
    for v in range(len(state)-46):
        value = '%1.0f' % text[v]
        plt.text(x = v-0.4, y = text[v] + 1000, s = value + '(GWH)', color='black', fontweight='bold',fontsize =10)
    plt.ylabel('Production (GWh)', fontsize=14)
    plt.title('Hydroelectricity Production by States, 2017',fontsize = 20, fontweight='bold')
    plt.xticks(rotation = 45, ha='right')
    plt.style.use('seaborn-whitegrid')
    my_dpi=200
    plt.savefig('plots/Hydro_State_2004_2018.png', figsize=(1500/my_dpi, 1200/my_dpi), dpi=my_dpi)
    plt.show()
    
def plot_map_wind_generation(wind_float,year): 
    '''
        projection: Lambert Conformal Projection (lcc)
        llcrnrlon: longitude of lower left hand corner of the desired map domain (-119)
        llcrnrlat:latitude of lower left hand corner of the desired map domain (22)
        urcrnrlon:longitude of upper right hand corner of the desired map domain (64)
        urcrnrlat:latitude of upper right hand corner of the desired map domain (49)
        lon_0:center of desired map domain (-95).
        resolution: high
    '''
    assert isinstance(wind_float,pd.DataFrame)
    assert isinstance(year,str) and len(year)==4
    
    windgeneration=wind_float[year].to_dict()
    fig = plt.figure(figsize=(18.5, 10.5))
    m = Basemap(llcrnrlon=-125,llcrnrlat=15,urcrnrlon=-60,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95,resolution='l')
    # draw state boundaries.
    # data from U.S Census Bureau
    shp_info = m.readshapefile('Plot_Data/cb_2018_us_state_5m','states',drawbounds=True)
    # Energy comsumption by 2016
    # https://www.eia.gov/state/seds/sep_sum/html/pdf/sum_btu_1.pdf
    # choose a color for each state based on population density.
    colors={}
    statenames=[]
    cmap = plt.cm.Greens_r # use 'hot' colormap
    vmin = 0; vmax = 45000 # set range.
    for shapedict in m.states_info:
        statename = shapedict['NAME']
        # skip DC and Puerto Rico.
        if statename not in ['District of Columbia','Puerto Rico', 'United States Virgin Islands',\
                             'Guam','Commonwealth of the Northern Mariana Islands','American Samoa']:
            pop = windgeneration[statename]
            # calling colormap with value between 0 and 1 returns
            # rgba value.  Invert color range (hot colors are high
            # population), take sqrt root to spread out colors more.
            colors[statename] = cmap(1.-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        statenames.append(statename)
    # cycle through state names, color each one.
    ax = plt.gca() # get current axes instance
    for nshape,seg in enumerate(m.states):
        # skip DC and Puerto Rico.
        if statenames[nshape] not in ['District of Columbia','Puerto Rico', 'United States Virgin Islands',\
                             'Guam','Commonwealth of the Northern Mariana Islands','American Samoa']:
            # Offset Alaska and Hawaii to the lower-left corner. 
            if statenames[nshape] == 'Alaska':
            # Alaska is too big. Scale it down to 35% first, then transate it. 
                seg1 = list(map(lambda x : (0.35 * x[0] + 1100000, 0.35 * x[1]-1300000), seg))
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg1,facecolor=color,edgecolor='black',linewidth = 0.7)
                ax.add_patch(poly)
            if statenames[nshape] == 'Hawaii':
                seg1 = list(map(lambda x: (x[0] + 5000000, x[1]-1400000), seg))
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg1,facecolor=color,edgecolor='black',linewidth = 0.7)
                ax.add_patch(poly)
            else:   
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg,facecolor=color,edgecolor=color)
                ax.add_patch(poly)

    # Create a colorbar
    sm = plt.cm.ScalarMappable(cmap='Greens' , norm=plt.Normalize(vmin=0, vmax=45000))
    sm._A = []

    cbar = fig.colorbar(sm)
    cbar.set_label('GWH', rotation=270)

    plt.title('Wind Power Generation in '+year+' (GWh)',fontsize = 20, fontweight='bold')
    plt.show()
    my_dpi=200
    plt.style.use('seaborn-whitegrid')
    fig.savefig('plots/wind_'+year+'.png', bbox_inches='tight', figsize=(1500/my_dpi, 1200/my_dpi), dpi=my_dpi)

    
def plot_map_hydro_potential(data): 
    '''
        projection: Lambert Conformal Projection (lcc)
        llcrnrlon: longitude of lower left hand corner of the desired map domain (-119)
        llcrnrlat:latitude of lower left hand corner of the desired map domain (22)
        urcrnrlon:longitude of upper right hand corner of the desired map domain (64)
        urcrnrlat:latitude of upper right hand corner of the desired map domain (49)
        lon_0:center of desired map domain (-95).
        resolution: high
    '''
    assert isinstance(data, pd.DataFrame)

    hydroPotential = dict()
    column = data.columns.to_list()
    for state in column:
        hydroPotential[state] = list(data[state])[0]
    fig = plt.figure(figsize=(18.5, 10.5))
    m = Basemap(llcrnrlon=-125,llcrnrlat=15,urcrnrlon=-60,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95,resolution='l')
    # draw state boundaries.
    # data from U.S Census Bureau
    shp_info = m.readshapefile('Plot_Data/cb_2018_us_state_5m','states',drawbounds=True)
    # Energy comsumption by 2016
    # https://www.eia.gov/state/seds/sep_sum/html/pdf/sum_btu_1.pdf
    # choose a color for each state based on population density.
    colors={}
    statenames=[]
    cmap = plt.cm.Blues_r # use 'hot' colormap
    vmin = 0; vmax = 35000 # set range.
    for shapedict in m.states_info:
        statename = shapedict['NAME']
        # skip DC and Puerto Rico.
        if statename not in ['District of Columbia','Puerto Rico', 'United States Virgin Islands',\
                             'Guam','Commonwealth of the Northern Mariana Islands','American Samoa']:
            pop = hydroPotential[statename]
            # calling colormap with value between 0 and 1 returns
            # rgba value.  Invert color range (hot colors are high
            # population), take sqrt root to spread out colors more.
            colors[statename] = cmap(1.-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        statenames.append(statename)
    # cycle through state names, color each one.
    ax = plt.gca() # get current axes instance
    for nshape,seg in enumerate(m.states):
        # skip DC and Puerto Rico.
        if statenames[nshape] not in ['District of Columbia','Puerto Rico', 'United States Virgin Islands',\
                             'Guam','Commonwealth of the Northern Mariana Islands','American Samoa']:
            # Offset Alaska and Hawaii to the lower-left corner. 
            if statenames[nshape] == 'Alaska':
            # Alaska is too big. Scale it down to 35% first, then transate it. 
                seg1 = list(map(lambda x : (0.35 * x[0] + 1100000, 0.35 * x[1]-1300000), seg))
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg1,facecolor=color,edgecolor='black',linewidth = 0.7)
                ax.add_patch(poly)
            if statenames[nshape] == 'Hawaii':
                seg1 = list(map(lambda x: (x[0] + 5000000, x[1]-1400000), seg))
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg1,facecolor=color,edgecolor='black',linewidth = 0.7)
                ax.add_patch(poly)
            else:   
                color = rgb2hex(colors[statenames[nshape]]) 
                poly = Polygon(seg,facecolor=color,edgecolor=color)
                ax.add_patch(poly)

    # Create a colorbar
    sm = plt.cm.ScalarMappable(cmap='Blues' , norm=plt.Normalize(vmin=0, vmax=35000))
    sm._A = []

    cbar = fig.colorbar(sm)
    cbar.set_label('GWH', rotation=270)
    plt.style.use('seaborn-whitegrid')
    plt.title('Technical Potential for Hydropower in the US, 2012',fontsize = 20, fontweight='bold')
    my_dpi=200
    
    plt.savefig('plots/HydroPotentialMap.png', figsize=(1500/my_dpi, 1200/my_dpi), dpi=my_dpi)
    
    plt.show()

def GetEIAData1():
    eia_temp = pd.read_csv('Plot_Data/eiadata/10.01/Jan-Dec 1973.csv')
    new_df = pd.DataFrame(columns=list(range(1973, 2020)), dtype='float64')
    new_df = new_df.fillna(0)

    for year in range(1973, 2020):
        try:
            eia_temp = pd.read_csv('Plot_Data/eiadata/10.01/Jan-Dec ' + str(year) + '.csv')
        except:
            eia_temp = pd.read_csv('Plot_Data/eiadata/10.01/Jan-Jan ' + str(year) + '.csv')
        eia_temp['sum'] = (eia_temp.sum(axis=1))
        new_df[year] = eia_temp['sum']
    new_df.index = (eia_temp['Unnamed: 0'])
    new_df.index.names = ['Source']
    final = new_df.T
    final = final.iloc[0:-1]
    return final

def PlotRenewUSA(final=None):
    '''
    '''
    
    my_dpi=100


    fig, ax = plt.subplots(figsize=(1000/my_dpi, 640/my_dpi), dpi=my_dpi)
    ax.plot(final.index, final.iloc[::, [6, 7, 8, 9]]['Hydroelectric Power'], marker='', color='xkcd:azure', linewidth=2, alpha=0.9)
    ax.plot(final.index, final.iloc[::, [6, 7, 8, 9]]['Geothermal'], marker='', color='xkcd:rusty red', linewidth=2, alpha=0.9)
    ax.plot(final.index, final.iloc[::, [6, 7, 8, 9]]['Solar'], marker='', color='xkcd:golden yellow', linewidth=2, alpha=0.9)
    ax.plot(final.index, final.iloc[::, [6, 7, 8, 9]]['Wind'], marker='', color='xkcd:dark grey', linewidth=2, alpha=0.9)
    plt.grid(b=True)
    ax.legend(['Hydroelectric Power', 'Geothermal', 'Solar', 'Wind'], frameon=True)
    ax.set_title('Renewable Energy Consumption in the USA', fontdict={'fontsize': 20, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("Year " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.set_ylabel("Consumption (Trillion BTUs) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    plt.style.use('seaborn-whitegrid')
    fig.savefig('plots/NationalConsumption.png', bbox_inches='tight')
    
def GetEIAData2():
    '''
    '''
    
    montemp6 = pd.read_csv('Plot_Data/eiadata/10.02C/Jan-Dec 1973.csv')
    montemp6 = montemp6.set_index('Unnamed: 0')
    montemp6.index.name = 'Source'

    for year in range(1974, 2020):
        try:
            temp = pd.read_csv('Plot_Data/eiadata/10.02C/Jan-Dec ' + str(year) + '.csv')
        except:
            temp = pd.read_csv('Plot_Data/eiadata/10.02C/Jan-Jan ' + str(year) + '.csv')

        temp = temp.set_index('Unnamed: 0')
        temp.index.name = 'Source'
        montemp6 = pd.concat([montemp6, temp], axis=1)
    montemp6 = montemp6.T
    return montemp6

def GetEIAData3(montemp6=None):
    '''
    
    '''
    
    noofyears = 2019-2008+1
    curr = montemp6.loc['Jan 2008':].iloc[::, [0, 1, 2, 3]]
    # curr
    months = ([i.split()[0] for i in list(curr.index)[0:12]])
    monthwise = pd.DataFrame(columns=curr.columns, index=months, dtype='float64')
    monthwise = monthwise.fillna(0)
    for num, i in enumerate(curr.index):
        monthwise.iloc[num%12] += curr.iloc[num].values
    monthwise = monthwise/noofyears
    return monthwise

def PlotMonthwiseUSA(monthwise=None):
    '''
    
    '''
    
    my_dpi=200
    plt.style.use('seaborn-whitegrid')

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(1500/my_dpi, 1000/my_dpi), dpi=my_dpi, sharex=True, frameon=True)

    ax[0][0].plot(list(monthwise.index), monthwise.iloc[::, 0], color='xkcd:azure', linewidth=2, alpha=0.7)
    ax[0][1].plot(list(monthwise.index), monthwise.iloc[::, 1], marker='', color='xkcd:rusty red', linewidth=2, alpha=0.7)
    ax[1][0].plot(list(monthwise.index), monthwise.iloc[::, 2], marker='', color='xkcd:golden yellow', linewidth=2, alpha=0.7)
    ax[1][1].plot(list(monthwise.index), monthwise.iloc[::, 3], marker='', color='xkcd:green', linewidth=2, alpha=0.7)

    plt.grid(b=True)

    ax[0][0].legend(['Hydroelectric'], frameon=True, fontsize=7)
    ax[0][1].legend(['Geothermal'], frameon=True, fontsize=7)
    ax[1][0].legend(['Solar'], frameon=True, fontsize=7)
    ax[1][1].legend(['Wind'], frameon=True, fontsize=7)

    fig.text(0.5, 0.04, "Month " + r'$\rightarrow$', ha='center', va='center', fontdict={'fontsize': 8, 'fontweight': 12})
    fig.text(0.06, 0.47, "Average Consumption (Trillion BTUs) ", va='center', rotation='vertical', fontdict={'fontsize': 10, 'fontweight': 12})

    plt.rcParams['xtick.labelsize']=8

    ax[0][0].spines['bottom'].set_color('0.5')
    ax[0][1].spines['bottom'].set_color('0.5')
    ax[1][0].spines['bottom'].set_color('0.5')
    ax[1][1].spines['bottom'].set_color('0.5')

    ax[0][0].spines['top'].set_color('0.5')
    ax[0][1].spines['top'].set_color('0.5')
    ax[1][0].spines['top'].set_color('0.5')
    ax[1][1].spines['top'].set_color('0.5')

    ax[0][0].spines['right'].set_color('0.5')
    ax[0][1].spines['right'].set_color('0.5')
    ax[1][0].spines['right'].set_color('0.5')
    ax[1][1].spines['right'].set_color('0.5')

    ax[0][0].spines['left'].set_color('0.5')
    ax[0][1].spines['left'].set_color('0.5')
    ax[1][0].spines['left'].set_color('0.5')
    ax[1][1].spines['left'].set_color('0.5')
    fig.savefig('plots/ElectricPowerMonthly.png', bbox_inches='tight')

def PlotElectricCon(montemp6=None):
    '''
    
    '''
    
    my_dpi=200
    # plt.style.use('seaborn-paper')
    # plt.style.use('ggplot')


    # plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(2000/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(montemp6.index[444::], montemp6.iloc[444::, [0, 1, 2, 3, 7]].iloc[::, 0], marker='', color='xkcd:azure', linewidth=2, alpha=0.7)
    ax.plot(montemp6.index[444::], montemp6.iloc[444::, [0, 1, 2, 3, 7]].iloc[::, 1], marker='', color='xkcd:rusty red', linewidth=2, alpha=0.7)
    ax.plot(montemp6.index[444::], montemp6.iloc[444::, [0, 1, 2, 3, 7]].iloc[::, 2], marker='', color='xkcd:golden yellow', linewidth=2, alpha=0.7)
    ax.plot(montemp6.index[444::], montemp6.iloc[444::, [0, 1, 2, 3, 7]].iloc[::, 3], marker='', color='xkcd:orange', linewidth=2, alpha=0.7)

    plt.grid(b=True)

    ax.legend(['Hydroelectric', 'Geothermal', 'Solar', 'Wind'], frameon=True, bbox_to_anchor=(0.485, 0.5, 0.5, 0.5), fontsize=7)   
    ax.set_title('Electric Power Sector: Renewable Energy Consumption', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("Month, Year " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', rotation=60, labelsize=4, width=3)
    ax.set_ylabel("Consumption (Trillion BTUs) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/ElectricPower.png', bbox_inches='tight')
    
def PlotSolarCon():
    '''
    
    '''
    
    montemp8 = pd.read_csv('Plot_Data/eiadata/10.05/Jan-Dec 1973.csv')
    montemp8 = montemp8.set_index('Unnamed: 0')
    montemp8.index.name = 'Source'

    for year in range(1974, 2020):
        try:
            temp = pd.read_csv('Plot_Data/eiadata/10.05/Jan-Dec ' + str(year) + '.csv')
        except:
            temp = pd.read_csv('Plot_Data/eiadata/10.05/Jan-Jan ' + str(year) + '.csv')

        temp = temp.set_index('Unnamed: 0')
        temp.index.name = 'Source'
        montemp8 = pd.concat([montemp8, temp], axis=1)
    montemp8 = montemp8.T
    montemp8

    my_dpi=200

    fig, ax = plt.subplots(figsize=(2000/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(montemp8.index[444::], montemp8.iloc[444::, [1, 3, 4, 5]].iloc[::, 0], marker='', color='xkcd:azure', linewidth=2, alpha=0.7)
    ax.plot(montemp8.index[444::], montemp8.iloc[444::, [1, 3, 4, 5]].iloc[::, 1], marker='', color='xkcd:rusty red', linewidth=2, alpha=0.7)
    ax.plot(montemp8.index[444::], montemp8.iloc[444::, [1, 3, 4, 5]].iloc[::, 2], marker='', color='xkcd:golden yellow', linewidth=2, alpha=0.7)
    ax.plot(montemp8.index[444::], montemp8.iloc[444::, [1, 3, 4, 5]].iloc[::, 3], marker='', color='xkcd:orange', linewidth=2, alpha=0.7)

    plt.grid(b=True)

    ax.legend(['Heat', 'Residential Electricity', 'Commercial Electricity', 'Industrial Electricity'], frameon=True)
    ax.set_title('Solar Energy Consumption', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("Month, Year " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', rotation=60, labelsize=4, width=3)
    ax.set_ylabel("Consumption (Trillion BTUs) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/SolarConsum.png', bbox_inches='tight')
    
def PlotSolarGen():
    '''
    
    '''
    
    montemp10 = pd.read_csv('Plot_Data/eiadata/10.06/Jan-Dec 1973.csv')
    montemp10 = montemp10.set_index('Unnamed: 0')
    montemp10.index.name = 'Source'

    for year in range(1974, 2020):
        try:
            temp = pd.read_csv('Plot_Data/eiadata/10.06/Jan-Dec ' + str(year) + '.csv')
        except:
            temp = pd.read_csv('Plot_Data/eiadata/10.06/Jan-Jan ' + str(year) + '.csv')

        temp = temp.set_index('Unnamed: 0')
        temp.index.name = 'Source'
        montemp10 = pd.concat([montemp10, temp], axis=1)
    montemp10 = montemp10.T
    montemp10

    montemp11 = pd.DataFrame(columns=range(1973, 2019), index=montemp10.columns)
    for num, i in enumerate(range(1973, 2019)):
        yearstats = (montemp10[0:-1][(num*12):((num+1)*12)]).sum(axis=0)
        montemp11[i]=yearstats
    montemp11 = montemp11.T

    my_dpi=200

    fig, ax = plt.subplots(figsize=(2000/my_dpi, 1000/my_dpi), dpi=my_dpi)

    ax.plot(montemp11.index[::], montemp11.iloc[::, [1, 2, 3]].iloc[::, 0], marker='', color='xkcd:azure', linewidth=2, alpha=0.7)
    ax.plot(montemp11.index[::], montemp11.iloc[::, [1, 2, 3]].iloc[::, 1], marker='', color='xkcd:rusty red', linewidth=2, alpha=0.7)
    ax.plot(montemp11.index[::], montemp11.iloc[::, [1, 2, 3]].iloc[::, 2], marker='', color='xkcd:golden yellow', linewidth=2, alpha=0.7)
    plt.grid(b=True)
    ax.legend(['Residential', 'Commercial', 'Industrial'], frameon=True)
    ax.set_title('Distributed Solar Generation', fontdict={'fontsize': 15, 'fontweight': 12}, color='xkcd:black')
    ax.set_xlabel("Year " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    ax.tick_params(axis='x', labelsize=12, width=3)
    ax.set_ylabel("Generation (Million KWh) " + r'$\rightarrow$', fontdict={'fontsize': 12, 'fontweight': 12})
    fig.savefig('plots/DistSolarGenAnnual.png', bbox_inches='tight')
    
def PlotWindProduction():
    '''
    
    '''
    
    ActualEne = pd.read_csv('Plot_Data/Wind_ActualEne_AllStates.csv')
    ActualEne = ActualEne.set_index('State Code')
    years = [int(float(i)) for i in list(ActualEne.columns)]
    ActualEne.columns = years
    ActualEne.columns.name = 'Year'
    # ActualEne[2017]

    df = ActualEne

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.2, 'rgb(208,251,193)'],
        [0.4, 'rgb(181,249,157)'],
        [0.6, 'rgb(124,243,84)'],
        [0.8, 'rgb(69,226,16)'],
        [1.0, 'rgb(53,177,12)']
    ]

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' MWh',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=800000
                 )]

    for i in range(2002, 2019):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' MWh'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Actual Wind Energy Production (MWh)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, layout=layout)
    iplot(fig, filename='Plots/Wind Actual Energy', image_height=1080, image_width=1920)
    
def PlotWindPotential():
    '''
    
    '''
    
    PotEne = pd.read_csv('Plot_Data/Wind_Potential_AllStates.csv')
    PotEne = PotEne.set_index('State Code')
    years = [int(float(i)) for i in list(PotEne.columns)]
    PotEne.columns = years
    PotEne.columns.name = 'Year'
    # PotEne

    df = PotEne

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.2, 'rgb(208,251,193)'],
        [0.4, 'rgb(181,249,157)'],
        [0.6, 'rgb(124,243,84)'],
        [0.8, 'rgb(69,226,16)'],
        [1.0, 'rgb(53,177,12)']
    ]

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' MWh',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=1400000
                 )]

    for i in range(2002, 2019):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' MWh'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Maximum Wind Energy Potential (MWh)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, layout=layout)
    iplot(fig, filename='Plots/Wind Max Potential', image_height=1080, image_width=1920)
    
def PlotWindPercentPotential():
    '''
    
    '''
    
    Percent = pd.read_csv('Plot_Data/Wind_Percent_AllStates.csv')
    Percent = Percent.set_index('State Code')
    years = [int(float(i)) for i in list(Percent.columns)]
    Percent.columns = years
    Percent.columns.name = 'Year'
    # Percent

    df = Percent

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.2, 'rgb(208,251,193)'],
        [0.4, 'rgb(181,249,157)'],
        [0.6, 'rgb(124,243,84)'],
        [0.8, 'rgb(69,226,16)'],
        [1.0, 'rgb(53,177,12)']
    ]

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' %',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=100
                 )]

    for i in range(2002, 2019):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' %'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Wind Energy Potential Achieved (%)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, layout=layout)
    iplot(fig, filename='Plots/Wind Percent Potential', image_height=1080, image_width=1920)
    
def PlotSolarProd():
    '''
    
    '''
    
    ActualEne = pd.read_csv('Plot_Data/ActualSolarPotential.csv')
    ActualEne = ActualEne.T
    ActualEne.columns = ActualEne.iloc[0]
    ActualEne = ActualEne.drop('Unnamed: 0', axis=0)
    ActualEne.index.name = 'State Code'
    ActualEne.columns.name = 'Year'
    ActualEne=ActualEne/1000
    # ActualEne

    df = ActualEne

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.1, 'rgb(251,253,174)'],
        [0.2, 'rgb(249,252,135)'],
        [0.3, 'rgb(247,251,68)'],
        [0.4, 'rgb(241,248,5)'],
        [0.5, 'rgb(253,240,0)'],
        [0.6, 'rgb(238, 238, 4)'],
        [0.7, 'rgb(236, 205, 81)'],
        [0.8, 'rgb(235, 185, 82)'],
        [0.9, 'rgb(231, 112, 14)'],
        [1.0, 'rgb(188, 81, 1)']
    ]

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' MWh',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=25000
                 )]

    for i in range(2002, 2017):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' MWh'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Actual Solar Energy Production (MWh)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, 
               layout=layout)

    iplot(fig, filename='Plots/Solar Energy Actual Potential')
    
def PlotSolarPotential():
    '''
    
    '''
    
    MaxPot = pd.read_csv('Plot_Data/MaximumSolarPotential.csv')
    MaxPot = MaxPot.T
    MaxPot.columns = MaxPot.iloc[0]
    MaxPot = MaxPot.drop('Unnamed: 0', axis=0)
    MaxPot.index.name = 'State Code'
    MaxPot.columns.name = 'Year'
    MaxPot=MaxPot
    # MaxPot.values.max()

    df = MaxPot

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.1, 'rgb(251,253,174)'],
        [0.2, 'rgb(249,252,135)'],
        [0.3, 'rgb(247,251,68)'],
        [0.4, 'rgb(241,248,5)'],
        [0.5, 'rgb(253,240,0)'],
        [0.6, 'rgb(238, 238, 4)'],
        [0.7, 'rgb(236, 205, 81)'],
        [0.8, 'rgb(235, 185, 82)'],
        [0.9, 'rgb(231, 112, 14)'],
        [1.0, 'rgb(188, 81, 1)']
    ]

    # df['text'] = 'Achieved Energy: ' + df[1999]
    # + ' Dairy ' + df['dairy'] + '<br>' + \
    #     'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
    #     'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' MWh',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=26407633584.310554
                 )]

    for i in range(2002, 2017):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' MWh'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Maximum Solar Energy Potential (MWh)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, 
               layout=layout)

    iplot(fig, filename='Solar Energy Max Potential')
    
def PlotSolarPercentPotential():
    '''
    
    '''
    
    PercPot = pd.read_csv('Plot_Data/PercentSolarPotential.csv')
    PercPot = PercPot.T
    PercPot.columns = PercPot.iloc[0]
    PercPot = PercPot.drop('Unnamed: 0', axis=0)
    PercPot.index.name = 'State Code'
    PercPot.columns.name = 'Year'
    PercPot = round(PercPot, 4)
    # PercPot

    df = PercPot

    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [
        [0.0, 'rgb(242,240,247)'],
        [0.1, 'rgb(251,253,174)'],
        [0.2, 'rgb(249,252,135)'],
        [0.3, 'rgb(247,251,68)'],
        [0.4, 'rgb(241,248,5)'],
        [0.5, 'rgb(253,240,0)'],
        [0.6, 'rgb(238, 238, 4)'],
        [0.7, 'rgb(236, 205, 81)'],
        [0.8, 'rgb(235, 185, 82)'],
        [0.9, 'rgb(231, 112, 14)'],
        [1.0, 'rgb(188, 81, 1)']
    ]

    data = [dict(type='choropleth',
                 locations = df.index.astype(str),
                 z=df[2001].astype(float),
                 locationmode='USA-states',
                 colorscale = scl,
                 text = df[2001] + ' %',
                 hoverinfo = 'text+location',
                 autocolorscale = False,
                 marker= dict(line=dict(color='rgb(255,255,255)', width = 1)),
                 zauto=False,
                 zmax=0.16
                 )]

    for i in range(2002, 2017):
        data.append(data[0].copy())
        data[-1]['z'] = df[i].astype(float)
        data[-1]['text'] = df[i] + ' %'

    steps = []
    for i in range(len(data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data)],
                    label='Year : {}'.format(i + 2001))
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0,
                    pad={"t": 1},
                    steps=steps)]

    layout = dict(geo=dict(scope='usa',
                           projection={'type': 'albers usa'}),
                  sliders=sliders,
                  title = dict(text="<b>Solar Energy Potential Achieved (%)</b>",
                               font=dict(family='Overpass',
                                         size=30,
                                         color='#7f7f7f'
                                        )
                              )
                 )

    fig = dict(data=data, 
               layout=layout)

    iplot(fig, filename='Solar Energy Percent Potential')