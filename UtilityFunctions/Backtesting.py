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
    window = 30
    portfolio_cumalative_r = []
    portfolio_v = []
    allocations = []
    count = 0
    #portfolio_v.iloc[0] = 1

    n = int(np.floor(len(training)/window))
    for i in range(0, n):
        curr_training = training.iloc[window*i:window*(i+1)]
        allocation = GAlgorithm(30, len(stocks), 30, curr_training)
        portfolio_r = np.dot(curr_training.pct_change().dropna(), allocation[:len(stocks)])
        #temp = np.cumprod(portfolio_v[len(portfolio_v)-1]+portfolio_r)
        #print(portfolio_v.iloc[i*n])
        #print(temp)
        #portfolio_cumalative_r.append(np.cumprod(1+portfolio_r))
        #portfolio_v = pd.concat([portfolio_v, pd.Series(temp)])
        for j in range(0, len(portfolio_r)):
            portfolio_v.append(portfolio_r[j])
        allocations.append(allocation)
        count = count + window
    #benchmark = benchmark.iloc[:int(len(portfolio_v))]
    print(allocations)
    benchmark_r = benchmark.iloc[:int((window-1)*n + 1)].pct_change().dropna()
    benchmark_cumalative_r = np.cumprod(1 + benchmark_r)
    portfolio_v = np.cumprod(1+np.array(portfolio_v))
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(benchmark_cumalative_r.index, portfolio_v, label="p")
    ax.plot(benchmark_cumalative_r, label="b")
    ax.legend()
    plt.show()