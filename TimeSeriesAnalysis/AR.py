import numpy as np
import pandas as pd
from MLE import ridgeReg as RR
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima.model import ARIMA

def AR(p, data):
    data = np.array(data)
    TS = pd.Series(data.ravel())
    n = len(TS) - p
    y = np.zeros(n)
    X = np.zeros((n, p))
    for i in range(p, len(TS)):
        y[i-p] = TS[i]
        X[i-p,:] = TS.iloc[i-p:i]
    for j in range(0, p):
        X[:,j] -= np.sum(X[:,j])/n
    params = RR.rReg(X, y)
    return params

if __name__ == "__main__":
    stocks = ["AAPL"]
    start = '2024-12-01'
    data = yf.download(stocks, start = start)['Adj Close']
    data = np.log(data).diff().dropna()
    params = AR(3,data)
    r = np.random.normal(0, .01, len(data)-3)
    data = np.array(data)
    TS = pd.Series(data.ravel())
    sim = []
    sim.append(TS[0])
    sim.append(TS[1])
    sim.append(TS[2])
    for i in range(3, len(data)):
        sim.append(params[0] * sim[i-1] + params[1] * sim[i-2] + params[2] * sim[i-3] + 0*r[i-3])
        #sim.append(.9664 * sim[i-1] + -0.2389 * sim[i-2] + 0.1284 * sim[i-3] + 0*r[i-3])
    sim = pd.Series(sim)
    print(sim)
    print(TS)
    fitFinal = ARIMA(data, order=(3,0,0)).fit()
    print(params)
    print(fitFinal.summary())
    plt.plot(sim, color='red')
    plt.plot(TS)
    plt.show()