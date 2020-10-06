# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

%matplotlib inline

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
    x_dates = tmp_df['DATE'].dt.strftime('%m-%d')

    barchart = sns.barplot(data = tmp_df, x = x_dates, y = "usage".upper(), ax=ax
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
dtf.DATE = pd.to_datetime(dtf.DATE)
dtf = dtf.set_index('DATE')

# print(dtf.index.year.unique()[0])

def displayDf(dtf, freq='y', Y=None, M=None):

# TODO:
# The code below needs to be replaced with .loc to filter the dataframe
# and then use group to split the dataframe into different frequencies.
# However, this works for now as my first implementation

    months = ['jan','feb','mar',
            'apr','may','jun',
            'jul','aug','sep',
            'oct','nov','dec']

    years = dtf.index.year.unique()
    
    if not re.search("^(m|y)", freq.lower()):  # Check to see if either d m y were passed
        raise ValueError("freq must be 'm' or 'y'")        

    found_month = [] 
    found_year = []

    if( M is not None):
        for month in M.split():
            if month.lower() in months:
                found_month.append(month.lower())
    
    if( Y is not None):
        for year in Y.split():
            if int(year) in years:
                found_year.append(int(year))


    # Split dataframe
    g = dtf.groupby(pd.Grouper(freq=freq.upper()))
    dfs = [[time_stamp,group] for time_stamp,group in g]

    dtToPlot = pd.DataFrame()
    for df in dfs:
        if(freq == 'y'): # plot all the years
            if(found_year):
                if(df[0].year in found_year):
                    plotData(df[1],title=f'Year {df[0].year}')
            else:
                plotData(df[1],title=f'Year {df[0].year}')
        elif(freq == 'm'):
            dtfmonth = df[0].month_name().lower()[0:3]
            if(found_month and not found_year): # print month from all years
                if(dtfmonth in found_month):
                    plotData(df[1],title=f"{dtfmonth.upper()} {df[0].year} ")
            if(found_month and found_year): # print month from specific year
                if ((dtfmonth in found_month) and (df[0].year in found_year)):
                    plotData(df[1],title=f"{dtfmonth.upper()} {df[0].year} ")
            if(Y is None and M is None):
                plotData(df[1],title=f"{dtfmonth.upper()} {df[0].year} ")

# displayDf(dtf)
# displayDf(dtf, freq='m')
# displayDf(dtf,M='Jan Sep')
# displayDf(dtf,freq='m',M='may',Y='2015')
# displayDf(dtf,freq='m',Y='2015 2017', M='may')