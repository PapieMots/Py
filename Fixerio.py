# Import relevant libraries
import requests
import time
import datetime
import json

# Pull CCY Exchange Rates from Fixer.io
exchangerates = requests.get('http://data.fixer.io/api/latest?access_key=6a8d1e5aa588adfd134cea51f24d3dd6')
exchangerates_json = exchangerates.json()
rates = exchangerates_json['rates']

# debug
print("Printing price information")
print(rates)
