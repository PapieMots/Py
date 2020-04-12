# Import relevant libraries
import requests
import time
import datetime
import json
#from openpyxl import load_workbook

#####################################################################
# Get tickers
#####################################################################

# BTCZAR
res = requests.get("https://api.valr.com/v1/public/BTCZAR/marketsummary")
res_string = res.content.decode() #convert byte object to str
btczar = json.loads(res_string) #convert str to dict
print(btczar)

# parse BTCZAR
for key,value in btczar.items():
    if key == 'created':
       valr_btczar_timestamp = value
      #TO-DO:epoch time conversion for writing to xls
    if key == 'askPrice':
       valr_btczar_askprice = value