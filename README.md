# Technical Potential of Renewable Energy
### Swapnil Aggarwal   |   Bolun Yan   |   Yiwen Xia   |   Yiqing Hua

## Introduction

Our project aims at quantifying and analyzing the potential of renewable energy in the U.S.
Also, identifying and categorizing the key sources, consumers and barriers to realize those measured potentials

## Dataset

The dataset will be scraped and extracted from multiple sources:
-	https://www.nrel.gov: The National Renewable Energy Lab is a national lab under the Department of Energy and provides the primary source for the data. In terms of the problem, the dataset should provide state-wise key metrics related to the current utility (Power, Energy, Area, No. of sites, etc), and energy potential metrics of almost all kinds of renewables, such as Solar, Wind (Onshore and offshore), Biopower (Solid and Gaseous), Geothermal and Hydropower.
-	Furthermore, the key states identified in the above sub-problem can further be broken down using statewide energy data. As an example, following are some of the sources for reliable state-wise data:
-	State-wise Data on Wind Energy: https://windexchange.energy.gov/
-	US Energy Information and Administration: https://www.eia.gov/
- http://www.wikipedia.org: All basic energy data for USA

Our team utilizes the data science techniques we learned in class to make a general analysis about the potential of renewable energy in the U.S. The same can be used to quantify and realize key metrics of renewables. For example, identifying states with the maximum use of renewables, classifying states with maximum realizable potential according to each source of renewables and classifying states with the maximum and minimum urban/rural consumption. Also, other energy-specific factors such as maximum or minimum power, energy, land consumption would be measured for comprehensive analysis.

The project finds widespread real world application in the current scenario of the climate crisis. A data-based approach to study renewables will most definitely result in a more sustainable use of renewable energy sources. The findings can help our government systematically plan and implement policies so that the renewable energy production can be maximized.

## Project Steps
- Scraping, extracting and cleaning up data
- Categorization and identification of key metrics
- Data visualization of the obtained metrics

## Steps to Run

### Modules used
#### Scraping and Structuring

- numpy
- pandas
- geopandas
- scipy
- urllib
- selenium
- bs4 (BeautifulSoup)
- math
- zipfile
- io
- os
- copy
- itertools
- ast
- time

#### Visualizations
- plotly
- matplotlib
- basemap
- imageio

(A sample of all the instructions below is present in <b>SampleOutput.pdf</b>) 

### import renewable
- #### Import the renewable.py

### renewable.getWikiTables()
- #### Scrapes the wikipedia for generation data and some auxillary data, from links in Wikilinks/Wikilinks.txt, along with Solar generation data and saves files in folder 'Plot_Data/WikiTables', with subfolders as the Wiki-Page names. Prints out the pathnames of saved files.

### renewable.get_data_generation_1999_2019()
- #### Scrapes Wikipedia for generation data, saves it in 'Plot_Data/energy_consumpton_USA.csv' and returns the dataframe as well.

### renewable.get_data_hydro_2004_2018()
- #### Scrapes Wikipedia for hydroelectric production data and saves it in 'Plot_Data/hydro_power_usa.csv'.

### renewable.get_data_hydro_production()
- #### Scrapes Wikipedia for hydroelectric production data for states of US and stores it in 'Plot_Data/state_hydro_production.csv'.

### renewable.get_data_hydro_potential()
- #### Example data function for Hydro Potential Graph. Stores the data in 'Plot_Data/hydro_potentials.csv'.

### renewable.scrape_wind_data_from_wiki()
- #### Scrapes the wind generation data from wikipedia and stores it in 'Plot_Data/wind_wiki.csv'.

### renewable.scrapeEIA()
- #### Scrapes the EIA website using Selenium and chromedriver.exe (present in the repo) for 6 tables for data from 1973-2019 and stores it tablewise and yearwise in 'Plot_Data/eiadata/' folder.

### renewable.MakeCSPDataForSolar()
- #### Utilizes combined solar data from public Solar dataset (shapefile downloaded from NSRDB website, presrnt in 'Potential/Solar/nsrdb_v3_0_1_1998_2016_dni.shp') and year-wise public Solar datasets (16 CSV files, downloaded from  NSRDB website, present in 'Potential/Solar/NSRDB-YearWise') in order to calculate Commercial Solar Production potential over the years. Saves the files as 'Potential/Solar/ActualPotential.csv', 'Potential/Solar/MaximumPotential.csv' and 'Potential/Solar/PercentPotential.csv'.

### renewable.CalcWindPotential()
- #### Utilizes combined wind-energy data from windexchange and calculates the wind energy potential over the years in the US. Saves the calculated data in 'Potential/Wind/Wind_ActualEne_AllStates.csv', 'Potential/Wind/Wind_Potential_AllStates.csv' and 'Potential/Wind/Wind_Percent_AllStates.csv'.

## Plots

### In order to generate plots, run the notebook Plots_Notebook.ipynb. The notebook automatically imports 'renewable.py' and 'plot_functions.py'. All the plots are generated and saved in 'plots/' folder.
