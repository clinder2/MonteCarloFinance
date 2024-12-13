import yfinance as yf
import seaborn as sea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from GA_Sharpe_FItness import GA
from sharpeFitness import fitness
from Backtesting import backtesting

stocks = ["AAPL", "GOOG", "NVDA", "HD", "DIS"]
start = '2020-01-01'
data = yf.download(stocks, start = start)['Adj Close']
benchmark = yf.download('^OEX', start=start)['Adj Close']

""" allocation = GA(30, 5, 50, data)
print(allocation) """

""" data.plot(figsize=(12,6))
plt.show() """

backtesting(GA, data, benchmark, stocks)