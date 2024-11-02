import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt

days = 90
dt = 1/365 # time in years
T = days*dt
S0 = 20
X = 25 # strike price
r = .031 # risk free rate
sigma = .6 # volitility
trials = 1
value = 0
prices = [trials]
for i in range(0, trials):
    n = [np.random.normal(.5, .5, 1) for p in range(0, days)]
    S = S0
    for j in range(0, days):
        dS = S*(r*dt + sigma*math.sqrt(dt)*n[j])
        S = S + dS
        print(dS)
    value = value + max(S-X, 0)
    prices.append(value)
    print(str(i) + ", " + str(S))
print(value/trials)
print(math.exp(-1*r*T) * value/trials)
plt.hist(prices)
plt.show()