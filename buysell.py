# This program is an example of a buy/sell indicator.
# It can take up to 20 stock tickers as input.
# It then checks to see if these stocks meet certain technical parameters.
# It then gives a buy or sell output based on these indicators.
# Indicators are:
# Price above the 50 day moving average.
# 50 day moving average above the 200 day moving average.
# An increase in on-balance volume over the past 7 days.

import yfinance as yf
import pandas as pd

# Prompt user for up to 20 stock names
stocks = []
while len(stocks) < 20:
    stock = input("Enter a stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    stocks.append(stock)

# Loop through each stock
for stock in stocks:
    # Download historical data
    data = yf.download(stock, period="1y")
    
    # Calculate moving averages
    data["ma50"] = data["Close"].rolling(window=50).mean()
    data["ma200"] = data["Close"].rolling(window=200).mean()
    
    # Calculate on balance volume and its change over the past 7 days
    data["obv"] = (data["Close"] - data["Open"]) / (data["High"] - data["Low"]) * data["Volume"]
    data["obv_change"] = data["obv"].diff(7)
    
    # Check if conditions are met
    if data.iloc[-1]["Close"] > data.iloc[-1]["ma50"] and \
       data.iloc[-1]["ma50"] > data.iloc[-1]["ma200"] and \
       data.iloc[-8:]["obv_change"].mean() > 0:
        print(f"{stock}: Buy")
    else:
        print(f"{stock}: Sell")