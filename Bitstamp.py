# Import relevant libraries
import requests
import time
import datetime
import json
#from openpyxl import load_workbook
import mysql.connector as mariadb
from mysql.connector import errorcode

#########################
# Initiate DB connection
#########################

try:
    cnx = mariadb.connect(user='pythonuser', password='pythonuserpassword',
                              host='arbitrage.hopto.org',
                              database='arbitrage')
except mariadb.Error as err:
    if err.no == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Authentication Error")
    elif err.no == errorcode.ER_BAD_DB_ERROR:
        print("Non-existent DB")
    else:
        print(err)
else:
    # Set DB Cursor
    cursor = cnx.cursor()
    
    #####################################################################
    # Get tickers
    #####################################################################

    # BTCUSD
    res = requests.get("https://www.bitstamp.net/api/ticker/")
    res_string = res.content.decode() #convert byte object to str
    btcusd = json.loads(res_string) #convert str to dict

    #debug
    print(btcusd)

    # BTCEUR
    res = requests.get("https://www.bitstamp.net/api/v2/ticker/btceur")
    res_string = res.content.decode() #convert byte object to str
    btceur = json.loads(res_string) #convert str to dict

    #debug
    print(btceur)

    # parse BTCUSD
    for key,value in btcusd.items():
        if key == 'timestamp':
           bitstamp_btcusd_timestamp_epoch = value
          #TO-DO:epoch time conversion for writing to xls
        if key == 'volume':
           bitstamp_btcusd_volume = value
        if key == 'bid':
           bitstamp_btcusd_bidprice = value
    bitstamp_btcusd_currency = 'bitcoin'
    bitstamp_btcusd_pair = 'btcusd'
    cursor.execute("INSERT INTO bitstamp (id,currency,pair,price,volume) VALUES (%s,%s,%s,%s,%s)", (bitstamp_btcusd_timestamp_epoch,bitstamp_btcusd_currency,bitstamp_btcusd_pair,bitstamp_btcusd_bidprice,bitstamp_btcusd_volume))
    
    
    # parse BTCEUR
    for key,value in btceur.items():
        if key == 'timestamp':
           bitstamp_btceur_timestamp_epoch = value
          #TO-DO:epoch time conversion for writing to xls
        if key == 'volume':
           bitstamp_btceur_volume = value
        if key == 'bid':
           bitstamp_btceur_bidprice = value
    bitstamp_btceur_currency = 'bitcoin'
    bitstamp_btceur_pair = 'btceur'
    cursor.execute("INSERT INTO bitstamp (id,currency,pair,price,volume) VALUES (%s,%s,%s,%s,%s)", (bitstamp_btceur_timestamp_epoch,bitstamp_btceur_currency,bitstamp_btceur_pair,bitstamp_btceur_bidprice,bitstamp_btceur_volume))
    
    cnx.commit()
    cursor.close()
    cnx.close() 
