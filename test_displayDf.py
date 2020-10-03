import pytest
import pandas as pd
from .displayDf import displayDf

data = pd.read_csv("../pge-electrical-gas-and-weather/final.csv",index_col=0)

def test_good_freq():
    assert displayDf(data,freq='d') == None
    assert displayDf(data,freq='m') == None
    assert displayDf(data,freq='y') == None

def test_bad_freq():
    with pytest.raises(ValueError):
        displayDf(data,freq='p')
        displayDf(data,freq='A')
        displayDf(data,freq='i')


# def test_freqMonth():
#     assert displayDf(data,freq='m') == None

# def test_freqYear():
#     assert displayDf(data,freq='y') == None

# def test_always_fails():
#     assert False

#%%
# import pandas as pd
# data = pd.read_csv("../pge-electrical-gas-and-weather/final.csv",index_col=0)
# data