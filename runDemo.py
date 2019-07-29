# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

TOKEN = ''
def main():
    df = dataApi.getFuturesData('A', '2018-05-01', '2019-05-01', '1_w', datatype='memberVolume',database='fushare',token=TOKEN)
    print(df.head())

main()