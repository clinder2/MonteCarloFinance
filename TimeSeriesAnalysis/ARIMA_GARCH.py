import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
import yfinance as yf

stocks = ["AAPL"]
start = '2020-01-01'
data = yf.download(stocks, start = start)['Adj Close']

data = np.log(data).diff()
data = data.dropna()
order = [0,0,0]
AIC = np.inf
fitFinal = ARIMA(data, order=(1,0,1)).fit()
for p in range(0, 4):
    for d in range(0, 2):
        for q in range(0, 4):
            fit = ARIMA(data, order=(p,d,q)).fit()
            if fit.aic < AIC:
                AIC = fit.aic
                order = [p,d,q]
                fitFinal = fit
print(AIC)
print(order)
plot_acf(fitFinal.resid.dropna(), lags=np.arange(len(fitFinal.resid)-1))
plot_acf(fitFinal.resid.dropna().pow(2), lags=np.arange(len(fitFinal.resid)-1))
#plt.plot(data)
plt.show()