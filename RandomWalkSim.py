import numpy as np
import math
from random import randint

days = 90
dt = 1/365 # time in years
T = days*dt
S0 = 20
X = 25 # strike price
r = .031 # risk free rate
sigma = .6 # volitility
trials = 2
value = 0
for i in range(1, trials):
    n = [np.random.normal(.5, .5, 1) for p in range(0, days)]
    S = S0
    for j in range(0, days):
        dS = S*(r*dt + sigma*math.sqrt(dt)*n[j])
        S = S + dS
    value = value + max(S-X, 0)
print(value)