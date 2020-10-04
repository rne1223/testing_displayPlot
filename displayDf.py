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