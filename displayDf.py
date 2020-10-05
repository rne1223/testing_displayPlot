# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import re
import sys

def plotData(tmp_df):
    # modified code from https://stackoverflow.com/questions/51105648/ordering-and-formatting-dates-on-x-axis-in-seaborn-bar-plot
    # modified code from https://stackoverflow.com/questions/58991151/annotate-markers-values-on-seaborn-line-plot-sns

    ########
    # Barplot
    ########
    fig, ax = plt.subplots(figsize = (12,6))    
    tmp_df = tmp_df.reset_index()
    x_dates = tmp_df['date'].dt.strftime('%m-%d')

    # ax.set_xticklabels(labels=x_dates, rotation=45, ha='right');
    barchart = sns.barplot(data = tmp_df, x = x_dates, y = "electrical_usage", ax=ax, palette="Reds_d", label="electricity")

    ########
    # Line plot
    ########
    # max_num = math.floor(tmp_df.electrical_usage.max())
    # prev_val = 0
    # y_values = []

    # # For loop to add the temperature labels on the line graph
    # for index, value in tmp_df.max_temp.items():
    #     y = (value/100)*max_num # make sure that stays within the graph
    #     y_values.append(y) 
    #     ax.text(index,y,f'{value:1.0f}');  # display number temperature

    # linechart = sns.lineplot(x = x_dates, y = y_values, label="temperature")

def displayDf(dtf, freq='u', cost=False):

    #Todo
    #   Check the show argument
    #   Groupby dataframe depending on the frequency
        #   if freq == d    -- show days
        #       Split the dataframe by days.
        #       All days will be shown for their particular month  
        #
        #   if freq == m    -- show months 
        #       Split the dataframe by months.
        #       All months of the year will be represented in one chart 
        #
        #   if freq == y    -- show years 
        #       Split the dataframe by years.
        #       All years will be represented in one chart 
    #   Return a new dataframe with the wanted data
    #   Create a chart for that dataframe

    # check the frequencies to which split the dataframe
    if not re.search("^(m|y)", freq.lower()):  # Check to see if either d m y were passed
        raise ValueError("freq must be days, month or year")        

    # Split dataframe
    g = dtf.groupby(pd.Grouper(freq=freq.upper()))
    dfs = [group for _,group in g]

    for df in dfs:
        plotData(dfs)


# %%
# import math
import pandas as pd

def plotData(tmp_df, title='None'):
    # modified code from https://stackoverflow.com/questions/51105648/ordering-and-formatting-dates-on-x-axis-in-seaborn-bar-plot
    # modified code from https://stackoverflow.com/questions/58991151/annotate-markers-values-on-seaborn-line-plot-sns

    # TODO:
    # Change barchart colors; make it more red when is hotter
    # Make plot to be a certain high unless there is something bigger

    ########
    # Barplot
    ########
    fig, ax = plt.subplots(figsize = (12,6))    

    tmp_df = tmp_df.reset_index()
    x_dates = tmp_df['date'].dt.strftime('%m-%d')

    barchart = sns.barplot(data = tmp_df, x = x_dates, y = "electrical_usage", ax=ax
    ,palette="Reds_d", label="electricity")

    # Handling plot title

    if(len(x_dates) > 31):
        barchart.set(title='Days in a Year' if not title else title)
        barchart.set(xticklabels=[])
        barchart.set(xlabel=None)
    else:
        barchart.set(title='Days in a Month' if not title else title)
        ax.set_xticklabels(labels=x_dates, rotation=45, ha='right');

# %%
import pandas as pd
import re
from dateutil import parser
import sys

# Reading data, most likely this is going to go
dtf = pd.read_csv('data.csv', index_col=0)
dtf.date = pd.to_datetime(dtf.date)
dtf = dtf.set_index('date')

def displayDf(dtf, freq='y', filter=None):
    # TODO:
    # Be able to filter the year
    # Be able to filter the month

    if not re.search("^(m|y)", freq.lower()):  # Check to see if either d m y were passed
        raise ValueError("freq must be 'm' or 'y'")        

    try:
        date = parser.parse(filter)  # datetime.datetime(1999, 8, 28, 0, 0)
    except Exception as e:
        print('Filter error: ',e)
        return
    
    if( filter is not (None or '')):
        flen = len(filter) 
        if(flen == 3):
            filter = date.month
        elif (flen == 4):
            # filter a year from all the years
            pass
        elif (filter.find('/')):
            pass
            # filter a specific month in a year

    # print(date.year,date.month,date.day)

    # Split dataframe
    g = dtf.groupby(pd.Grouper(freq=freq.upper()))
    dfs = [[date,group] for date,group in g]

    for df in dfs:
        print( df[0].year, df[0].month)
        # plotData(df[1], title='Hello world')

# displayDf(dtf,freq='m')
# displayDf(dtf, freq='m')
displayDf(dtf,filter='')

# %%
from dateutil import parser
date = parser.parse("2014/0/01")  # datetime.datetime(1999, 8, 28, 0, 0)
date