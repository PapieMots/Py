# Import libraries
import requests
import date
import datetime
import json

# Pull exchange rate from ExchangeRatesApi
url = 'https://api.exchangeratesapi.io/latest'
exchangerate = requests.get(url, params={'base':'USD'})
exchangerate_json = exchangerate.json()

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

