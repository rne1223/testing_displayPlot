# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import re

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
import math
import pandas as pd

def plotData(tmp_df):
    # modified code from https://stackoverflow.com/questions/51105648/ordering-and-formatting-dates-on-x-axis-in-seaborn-bar-plot
    # modified code from https://stackoverflow.com/questions/58991151/annotate-markers-values-on-seaborn-line-plot-sns

    ########
    # Barplot
    ########
    fig, ax = plt.subplots(figsize = (12,6))    

    tmp_df = tmp_df.reset_index()
    x_dates = tmp_df['date'].dt.strftime('%m-%d')

    # if(len(x_dates) > 31):
        # print('lots of dates')
    #     ax.set_xticklabels(labels=x_dates, rotation=45, ha='right');

    barchart = sns.barplot(data = tmp_df, x = x_dates, y = "electrical_usage", ax=ax
    ,palette="Reds_d", label="electricity")

    if(len(x_dates) > 31):
        barchart.set(title='Days in a Year')

    barchart.set(xticklabels=[])
    barchart.set(xlabel=None)

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

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

dtf = pd.read_csv('data.csv', index_col=0)
dtf.date = pd.to_datetime(dtf.date)
dtf = dtf.set_index('date')


def displayDf(dtf, freq='y'):
    if not re.search("^(m|y)", freq.lower()):  # Check to see if either d m y were passed
        raise ValueError("freq must be days, month or year")        

    # Split dataframe
    g = dtf.groupby(pd.Grouper(freq=freq.upper()))
    dfs = [group for _,group in g]

    for df in dfs:
        plotData(df)

displayDf(dtf)
