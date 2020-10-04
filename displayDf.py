# import numpy as np
# import matplotlib.pyplot as plt
import re


def displayDf(dtf, freq=None, cost=False):
    #  Todo
    # - Check the show argument
    if not re.search("^(d|m|y)", freq.lower()):  # Check to see if either d m y were passed
        raise ValueError("freq must be days, month or year")        



# %%
# import re
# freq = 'Y'
# if not re.search("^(d|m|y)", freq.lower()): # Check to see if either d m y were passed
#     print("sorry") 

import pandas as pd

dtf = pd.read_csv('data.csv', index_col=0)
dtf.date = pd.to_datetime(dtf.date)
dtf.dtypes
dtf = dtf.set_index('date')

tmp = pd.DataFrame()
# dtf.head()
tmp['usage'] = (dtf['electrical_usage'].groupby(pd.Grouper(freq='M')).mean())
tmp['temp'] = (dtf['max_temp'].groupby(pd.Grouper(freq='M')).mean())
tmp.set_index()
tmp.head()