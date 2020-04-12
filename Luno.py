# Import relevant libraries
import requests
import time
import datetime
#from openpyxl import load_workbook
from luno_python.client import Client
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
    # Make connection to Luno server
    #####################################################################

    c = Client(api_key_id="cu8mryhtp5efk", api_key_secret="OmvIryVwHWYe9vaEqDLg4kJtXYXVFTLw8nwx-ng-x_Y")
    #c = Client(api_key_id="cu8mryhtp5efk", api_key_secret="1yW7o-KuwgkBfmRz_LBJFMeL8lzp070slIVLjrOqVaE")

    #####################################################################
    # Get tickers
    #####################################################################

    res = c.get_ticker("XBTZAR")

    #####################################################################
    # Get balances
    # - Commented the below out due to unhandled exceptions
    # - We will have to check this out when we begin actual trades
    #####################################################################

    #balance = c.get_balances()

    #####################################################################
    # Show balances
    #####################################################################

    # print(balance)
    print(res)       #Debug data

    # parse XBTZAR
    for key,value in res.items():
        if key == 'timestamp':
           luno_timestamp_epoch = value
           #TO-DO:epoch time conversion for writing to xls
        if key == 'rolling_24_hour_volume':
           luno_volume = value   
        if key == 'ask':
           luno_askprice = value
    luno_currency = 'bitcoin'
    luno_pair = 'btczar'
    cursor.execute("INSERT INTO luno (id,currency,pair,price,volume) VALUES (%s,%s,%s,%s,%s)", (luno_timestamp_epoch,luno_currency,luno_pair,luno_askprice,luno_volume))
    
    cnx.commit()
    cursor.close()
    cnx.close()


    # try:
    #    res = c.get_ticker(pair='XBTZAR')
    #    print(res)
    # except Exception as e:
    #   print (e)