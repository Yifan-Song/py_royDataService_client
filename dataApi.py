# -*- coding: utf-8 -*-
'''
Data API
    -- Data Functions would be defined here 
'''

import requests
import pandas as pd

PATH = "http://data.natapp1.cc"

def getFuturesData(futures, start, end, freq, datatype, token, database='uqer'):
    '''Get Futures Data'''
    print("Getting Data...")
    payload = {'futures': futures, 'start' : start, 'end' : end, 'freq' : freq, 'datatype' : datatype, 'database':database, 'token' : token}
    res = requests.get(PATH+"/data", params=payload)
    df = pd.DataFrame(eval(res.text))
    return df