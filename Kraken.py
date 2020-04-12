# Import relevant libraries
# Note: depency on pandas required at version 1.0.1 because 3.8.2 has a DLL import error
# see stackoverflow.com/questions/60767017/importerror-dll-load-failed-while-importing-aggregations-the-specifieed-module
import requests
import time
import datetime
import json
import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd
#from openpyxl import load_workbook

#####################################################################
# Get tickers
#####################################################################

pd.set_option('display.max_rows',None) #set pandas output to display full dataset


api = krakenex.API()
k = KrakenAPI(api)
pairs = k.get_tradable_asset_pairs()
print(type(pairs))
print(pairs)

pd.set_option('display.max_columns',None) #set pandas output to display full dataset
eurgbp = k.get_ticker_information("EURGBP")
print(eurgbp)
## BTCZAR
#res = requests.get("https://api.kraken.com/0/public/Assets?currency=ZUSDZJPY")
#res_string = res.content.decode() #convert byte object to str
#btczar = json.loads(res_string) #convert str to dict
#print(btczar)

# parse BTCZAR
#for key,value in btczar.items():
#    if key == 'created':
#       valr_btczar_timestamp = value
#      #TO-DO:epoch time conversion for writing to xls
#    if key == 'askPrice':
#       valr_btczar_askprice = value
       