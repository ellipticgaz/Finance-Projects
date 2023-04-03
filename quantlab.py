# This program is a technical analysis tool.
# It gives a number of charts for the ticker symbol entered by the user.
# Charts are:
# Price with 20,50 & 200 daily moving averages.
# MACD
# RSI
# Stochastic RSI
# Volume


import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.momentum import StochasticOscillator

# Get ticker symbol from user
tickerSymbol = input("Enter the ticker symbol: ")

# Define start and end dates for the data
days = float(input("How many days of data do you want? "))
start_date = dt.datetime.now() - dt.timedelta(days)
end_date = dt.datetime.now()

# Get data from Yahoo Finance
tickerData = yf.Ticker(tickerSymbol)
df = tickerData.history(period='1d', start=start_date, end=end_date)

# Print the last 5 rows of data
# print(df.tail())

# Add 20-day 50-day and 200-day moving averages
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# Calculate MACD, RSI, and Stochastic RSI indicators
macd = MACD(df['Close']).macd()
signal = MACD(df['Close']).macd_signal()
rsi = RSIIndicator(df['Close']).rsi()
stoch = StochasticOscillator(df['High'], df['Low'], df['Close'], window=14, smooth_window=3).stoch()

# Plot the price and indicators
fig, axs = plt.subplots(5, sharex=True, figsize=(12,14))
axs[0].plot(df.index, df['Close'], label='Price')
axs[0].plot(df.index, df['MA20'], label='20-day MA')
axs[0].plot(df.index, df['MA50'], label='50-day MA')
axs[0].plot(df.index, df['MA200'], label='200-day MA')
axs[0].set_ylabel('Price')
axs[0].set_title('Price and Indicators of ' + tickerSymbol)
axs[0].legend()
axs[1].plot(df.index, macd, label='MACD')
axs[1].plot(df.index, signal, label='Signal')
axs[1].set_ylabel('MACD')
axs[1].legend()
axs[2].plot(df.index, rsi, label='RSI')
axs[2].set_ylabel('RSI')
axs[2].legend()
axs[3].plot(df.index, stoch, label='Stochastic RSI')
axs[3].set_ylabel('Stochastic RSI')
axs[3].legend()
axs[4].bar(df.index, df['Volume'])
axs[4].set_ylabel('Volume')

# Format x-axis tick labels
plt.xticks(rotation=45)

# Display the graph
plt.show()