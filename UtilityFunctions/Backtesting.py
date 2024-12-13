import yfinance as yf
import seaborn as sea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from GA_Sharpe_FItness import GA
from sharpeFitness import fitness

def backtesting(GAlgorithm, data, benchmark, stocks):
    training = data.iloc[:int(len(data)/2)]
    testing = data.iloc[int(len(data)/2):]

    allocation = GAlgorithm(30, len(stocks), 30, training)
    portfolio_r = np.dot(testing.pct_change().dropna(), allocation[:len(stocks)])
    portfolio_cumalative_r = np.cumprod(1+portfolio_r)
    benchmark_r = benchmark.iloc[int(len(data)/2):].pct_change().dropna()
    benchmark_cumalative_r = np.cumprod(1 + benchmark_r)
    """ bench = [] # equal allocation for benchmark
    temp = 1/len(stocks)
    for i in range(0, len(stocks)):
        bench.append(temp)
    benchmark_r = np.dot(testing.pct_change().dropna(), bench)
    benchmark_cumalative_r = np.cumprod(1+benchmark_r)
 """
    #print(portfolio_r)
    #print(portfolio_cumalative_r)
    print(allocation)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(benchmark_cumalative_r.index, portfolio_cumalative_r, label="p")
    ax.plot(benchmark_cumalative_r, label="b")
    ax.legend()
    plt.show()

def monthly_backtesting(GAlgorithm, data, benchmark, stocks):
    training = data.iloc[:int(len(data)/2)]
    testing = data.iloc[int(len(data)/2):]