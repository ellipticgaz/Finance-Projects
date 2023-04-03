import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

# Access asset data from Yahoo Finance
ms1 = input("Enter ticker symbol: ")
ms = yf.download(ms1)

# Calculate the log daily return
ms['LogReturn'] = np.log(ms['Close']).diff()

# Calculate the probability that the stock price will drop over 5% in a day
mu = ms['LogReturn'].mean()
sigma = ms['LogReturn'].std(ddof=1)
prob_return1 = norm.cdf(-0.05, mu, sigma)
print('The probability of a 5% drop in a day is', prob_return1)

# Calculate the probability that the stock price will drop over 10% in a day
prob_return2 = norm.cdf(-0.1, mu, sigma)
print('The probability of a 10% drop in a day is', prob_return2)

# Calculate the probability the stock will drop over 40% in 220 days (1 trading year)
mu220 = 220 * mu
sigma220 = np.sqrt(220) * sigma
prob_return3 = norm.cdf(-0.4, mu220, sigma220)
print('The probability of a 40% drop in 1 year is', prob_return3)

# Calculate the probability the stock will drop over 20% in 220 days
prob_return4 = norm.cdf(-0.2, mu220, sigma220)
print('The probability of a 20% drop in 1 year is', prob_return4)

# Calculate Value at Risk (VaR)
VaR = norm.ppf(0.05, mu, sigma)
print('Single day value at risk is', VaR)

# Calculate quantiles of return
# 5% quantile
print('5% quantile is', norm.ppf(0.05, mu, sigma))
# 25% quantile
q25 = norm.ppf(0.25, mu, sigma)
print('25% quantile is', q25)
# 75% quantile
q75 = norm.ppf(0.75, mu, sigma)
print('75% quantile is', q75)
# 95% quantile
print('95% quantile is', norm.ppf(0.95, mu, sigma))