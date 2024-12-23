import numpy as np
import pandas as pd
import yfinance as yf
from SACOV import SampleAC
from statsmodels.tsa.arima.model import ARIMA

def DL(G, y, series):
    series = pd.Series(series)
    var = series.var()
    ans = []
    phi00 = 0
    n = len(G)
    phi_prev = np.zeros(n)
    G /= var
    for i in range(1, n):
        phi_i = np.zeros(n)
        num = 0
        den = 0
        for k in range(1, i):
            num = num + phi_prev[i-1][k] * G[i - k][0]
            den = den + phi_prev[i-1][k] * G[k][0]
        num = G[i][0] - num
        den = 1 - den
        phi_nn = num/den
        for k in range(1, i):
            phi_i[k] = phi_prev[i-1][k] - phi_nn * phi_prev[i-1][i-k]
        phi_i[i] = phi_nn
        phi_prev = np.vstack((phi_prev, phi_i))
    return phi_prev

if __name__ == "__main__":
    stocks = ["AAPL"]
    start = '2024-10-01'
    data = yf.download(stocks, start = start)['Adj Close']
    data = data["AAPL"].values
    G = np.zeros((10, 10))
    y = []
    var = pd.Series(data).var()
    for i in range(0, 10):
        temp = SampleAC(data, i)
        y.append(temp)
        if i == 0:
            for j in range(0, 10):
                G[j][j] = temp
        else:
            for j in range(0, 10-i):
                G[j][i] = temp
                G[i][j] = temp
                i = i + 1
    #print(G)
    ans = DL(G, y, data)
    print(ans[9])
    for i in range(0, 10):
        print(y[i]/var)
        print(np.dot(G[i], ans[9]))
    #ARMA = ARIMA(data, order=(9,0,0)).fit()
    #print(ARMA.params)