# Import relevant libraries
import requests
import time
from luno_python.client import Client

# Make connection to Luno server
c = Client(api_key_id="cu8mryhtp5efk", api_key_secret="1yW7o-KuwgkBfmRz_LBJFMeL8lzp070slIVLjrOqVaE")

# Get tickers
res = c.get_ticker("XBTZAR")

# Get balances
balance = c.get_balances()

# Show balances
# print(balance)
print(res)

# try:
#    res = c.get_ticker(pair='XBTZAR')
#    print(res)
# except Exception as e:
#   print (e)