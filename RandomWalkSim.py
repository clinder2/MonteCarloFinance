import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt

# Simple geometric random walk simulation of Black-Scholes formula

days = 90
dt = 1/365 # time in years
T = days*dt
S0 = 135
X = 140 # strike price
r = .0437 # risk free rate
sigma = .62 # volitility (NVDA)
trials = 1000
value = 0
prices = [trials]
for i in range(0, trials):
    n = [np.random.normal(0, 1, 1) for p in range(0, days)]
    S = S0
    for j in range(0, days):
        dS = S*(r*dt + sigma*math.sqrt(dt)*n[j])
        S = S + dS
        #print(dS)
    value = value + max(S-X, 0)
    S = S * 10
    S = np.round(S)
    S = S/10
    prices.append(S[0])
    print(str(i) + ", " + str(S))
print(value/trials)
print(math.exp(-1*r*T) * value/trials)
plt.hist(prices, bins=100)
plt.show()