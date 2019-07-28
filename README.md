# py_royDataService_client
Roy Data Service Client
===================================
Client part is responsible for users to get data from the remote database. 

dataApi
-----------------------------------
	Functions for getting data 

To start:
-----------------------------------
    - Anaconda 3 64bit




Documents and Parameters
-----------------------------------
## Database and datatype
    uqer:
        tradingData(>=1min)
        tradingDataNight(>=1min)
        tradingDataDaily(>=1d)
        tradingDataCompare(>=1min)
        mainContract(>=1d)
        adjustForm(>=1d)
    fushare:
        memberVolume(>=1d)
        rollingYield(>=1d)    
        spotPrice(>=1d)  
    uqer_fundamental:
        hedgeData(>=1d)
        memberVolume(>=1d)
        registeredWarehouseReceipt(>=1d)     
    ctp:(not yet)
        tradingData(tick or >= 1s)
## Supported Frequency
    tick: tick(not yet)
    second: 1_s(not yet)
    minute: 1_min
    hour: 1_h
    day: 1_d
    week: 1_w
    month: 1_m
## Detailed Columns Specification
### tradingData/tradingDataNight(uqer)
#### Explaination
	Main contract trading data without adjusting, main contract is based on 3-day open interest and it do NOT change it backward.  
#### Columns
	CLEARINGDAY: Clearing day,  TDATE: Trade day,  CONTRACTID: Contract ID,   MARKET: Exchange Market,  bartime:  End time of a bar
	closeprice/openprice/highprice/lowprice/volume/value: OHLC and volume/amount,  vwap: Value weighted average price
	OPENINTS: Open Interest,  futures:  Futures Notation

### tradingDataCompare(uqer)
#### Explaination
    The form compares front month contract and next front month contract in close price and vwap. Actually front month contract means main contract and next front month contract means the contract with maximum open interest and expires later than the main contract. Some blank value may appear under the no-changing-back rule.	
#### Columns    
    bartime:  End time of a bar,  CLEARINGDAY: Clearing day,  CONTRACTID: Contract ID of the main contract,  CONTRACTID_nextfrontmonth: Contract ID of the next main contract,  closeprice_frontmonth: Close price of the main contract,  closeprice_nextfrontmonth: Close price of the next main contract
    vwap_frontmonth: Vwap of the main contract,  vwap_nextfrontmonth: Vwap of the next main contract

### mainContract(uqer)
#### Explaination
	Main contract information, consists 4 different types of main contract, 'modified' means do NOT change backward.
#### Columns    	
	contractObject: Futures Notation,  mainContract_oi:  Main Contract based on open interest(3day average),  mainContract_vol: Main Contract based on trading volume(3day average),  mainContract_oi_modified/mainContract_vol_modified: Modified means do not change backward.

### adjustForm(uqer)
#### Explaination
	Adjust form provides 4 different adjusting methods and their factors which could be used for adjusting the main contract trading data
#### Columns    	
	contractObject: Futures Notation,  mainContract_oi_modified: Selected main contract type
	adjust_af@-: Absolute adjust/first base, raw price - factor
	adjust_al@+: Absolute adjust/last base, raw price + factor
	adjust_rf@/: Relative adjust/first base, raw price / factor
	adjust_rl@*: Relative adjust/last base, raw price * factor

### memberVolume/rollingYield/spotPricez(fushare)
#### Explaination
	Fundamental information for futures in fushare source.
#### Columns    	
	https://github.com/LowinLi/fushare

### hedgeData/memberVolume/registeredWarehouseReceipt(uqer_fundamental)
#### Explaination
	Fundamental information for futures in uqer source.
#### Columns    	
	https://uqer.io/data/browse/105/105001/?page=1


Authors:
-----------------------------------
	Yifan Song (https://github.com/Yifan-Song): Networks and Servers
	Xiao Cheng (https://github.com/RoyCheng1997): DataEngines and data service
