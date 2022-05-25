# a simple script that prints out cryptocurrency price from binance
import requests
import time

BASE_URL = "https://api.binance.com/api/v3/ticker/price"
# https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
trading_pair = input("Enter trading pair: ")

while True:
    response = requests.get(
        f"https://api.binance.com/api/v3/ticker/price?symbol={trading_pair}").json()
    pair = response["symbol"]
    price = response["price"]
    time.sleep(2)
    print(f"Price: {price}")