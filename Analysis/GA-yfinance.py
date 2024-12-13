import sys
#sys.path.insert(0, '/UtilityFunctions/GA_NLSE_Solver.py/')
#sys.path.append("/UtilityFunctions/GA_NLSE_Solver.py/")
import yfinance as yf
import seaborn as sea
import matplotlib.pyplot as plt

stocks = ["AAPL", "MS", "NVDA"]
start = '2020-01-01'
data = yf.download(stocks, start = start)['Adj Close']
benchmark = yf.download('^OEX', start=start)['Adj Close']

data.plot(figsize=(12,6))
plt.show()