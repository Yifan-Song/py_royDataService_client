# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

def main():
    df = dataApi.getFuturesData('RB', '2018-05-01', '2019-05-01', '1_w', 'tradingData')
    print(df.head())

main()