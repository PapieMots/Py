import requests
 
# ticker = requests.get('https://api.cryptowat.ch/assets')
# btc = requests.get('https://api.cryptowat.ch/assets/btc')
# btcpairs = requests.get('https://api.cryptowat.ch/pairs')
# btcusd = requests.get('https://api.cryptowat.ch/pairs/btcusd')
 
# Luno BTCZAR Price Checker
lunobtc = requests.get('https://api.cryptowat.ch/markets/luno/btczar/price')
lunobtc_json = lunobtc.json()
lunoprice = lunobtc_json['result']
 
# Bistamp BTCEUR Price Checker
bitstampbtc = requests.get('https://api.cryptowat.ch/markets/bitstamp/btceur/price')
bitstampbtc_json = bitstampbtc.json()
bitstampprice = bitstampbtc_json['result']
 
# Pull EURZAR Exchange Rate from ECB
exchangerates = requests.get('https://api.exchangeratesapi.io/latest')
exchangerates_json = exchangerates.json()
rates = exchangerates_json['rates']

# Calculate Implied Exchange Rate
impliedexrate = lunoprice['price'] / bitstampprice['price']
 
# Calculate potential arbitrage gap currently
arbgap = (1-rates['ZAR']/impliedexrate)*100

# User input for amount of ZAR in bank deposit
zar_balance = input("Please enter amount of ZAR avaialable for trade: ")

# Print Results
print("Luno BTCZAR price is",lunoprice['price'])
print("Bitstamp BTCEUR price is",bitstampprice['price'])
print("Implied EURZAR exchange rate =",impliedexrate)
print("Actual EURZAR exchange rate =",rates['ZAR'])
print("Potential arbitrage gap, less fees =",arbgap)
print()
print("ZAR available",zar_balance)