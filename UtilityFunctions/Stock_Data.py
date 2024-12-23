import yfinance as yf
import seaborn as sea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from GA_Sharpe_FItness import GA
from sharpeFitness import fitness
from Backtesting import backtesting, monthly_backtesting

stocks = ["AAPL", "GOOG", "NVDA", "HD", "MSFT"]
start = '2024-01-01'
data = yf.download(stocks, start = start)['Adj Close']
benchmark = yf.download('^OEX', start=start)['Adj Close']

print(data['AAPL'].iloc[3:6])

""" allocation = GA(30, 5, 50, data)
print(allocation) """

""" data.plot(figsize=(12,6))
plt.show() """

monthly_backtesting(GA, data, benchmark, stocks)