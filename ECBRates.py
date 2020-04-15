# Import relevant libraries
import requests
import time
import datetime
import json

# Pull EURZAR Exchange Rate from ECB
exchangerates = requests.get('https://api.exchangeratesapi.io/latest')
exchangerates_json = exchangerates.json()
rates = exchangerates_json['rates']

# debug
print("Printing price information vertically")
print(rates)
