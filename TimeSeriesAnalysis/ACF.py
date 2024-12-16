import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
import yfinance as yf

stocks = ["NVDA"]
start = '2020-01-01'
data = yf.download(stocks, start = start)['Adj Close']
#benchmark = yf.download('^OEX', start=start)['Adj Close']

#stock_data = pd.Series(data[:,0])
stock_diff = data.diff()
ans = AutoReg(data, lags=[1,2,3]).fit()
print(ans.aic)
print(ans.hqic)
print(ans.bic)

""" t = np.linspace(-5*np.pi, 5*np.pi, num=100)
s = pd.Series(.7*np.random.rand(100)+.3*np.sin(t))
s = []
for i in range(0, 101):
    s.append(i) """

rand_walk = [1, 1]
rand = np.random.normal(0, .1, 100)
for i in range(0, 100):
    rand_walk.append(rand_walk[len(rand_walk)-1] + rand[i])
""" x = pd.plotting.autocorrelation_plot(s)
x.plot() """
series = pd.Series(rand_walk)
diff = series.diff()
#x = pd.plotting.autocorrelation_plot(stock_diff)
#x.plot()
#x2 = plot_acf(stock_diff.dropna(), lags=np.arange(len(stock_diff)-1))
#plt.plot(stock_diff)
ARMA = ARIMA(stock_diff, order=(2,0,2)).fit()
print(ARMA.params)
forecast = ARMA.forecast(steps=40)
""" fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax = ARMA.resid.plot(ax=ax) """
x3 = plot_acf(ARMA.resid.dropna(), lags=np.arange(len(ARMA.resid)-1))
#plt.plot(forecast)
plt.show()