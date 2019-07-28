# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

def main():
    df = dataApi.getFuturesData('A', '2018-05-01', '2019-05-01', '1_w', 'memberVolume','fushare')
    print(df.head())

main()