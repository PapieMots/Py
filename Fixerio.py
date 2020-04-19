# Import relevant libraries
import requests
import time
import datetime
import json
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
    
    # Pull CCY Exchange Rates from Fixer.io
    exchangerates = requests.get('http://data.fixer.io/api/latest?access_key=6a8d1e5aa588adfd134cea51f24d3dd6')
    exchangerates_json = exchangerates.json()

    # Assign relevant values to variables
    Prices = exchangerates_json['rates']
    ZARPrice = Prices['ZAR']
    USDPrice = Prices['USD']
    GBPPrice = Prices['GBP'] 
    BaseCCY = exchangerates_json['base']

    # Debug printing
    print('ZAR Price :', ZARPrice)
    print('USD Price :', USDPrice)
    print('GBP Price: ', GBPPrice)
    print('Base  CCY:', BaseCCY)		

    # Write Test Value to Table -- ZAR
    cursor.execute("INSERT INTO fixerfx (baseccy,targetccy,rate) VALUES (BaseCCY,'ZAR',ZARPRice);")
    
    # Commit to DB  
    cnx.commit()
    cursor.close()
    cnx.close() 
