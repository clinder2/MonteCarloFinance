# utility function to evaluate chromosome fitness from random walk sim of asset allocation play
import numpy as np
import math
import matplotlib.pyplot as plt

def fitness(popSize, pop, iterations, prob):
    history = []
    F = np.ones(popSize)
    N = iterations # iterations of kelly game
    for i in range(1, N+1):
        w = F * pop # wager
        #print(w)
        r = np.random.normal(.5, .5, popSize)
        r2 = np.ones(popSize)
        for i in range(0, popSize):
            if r[i] >= prob[0]:
                r2[i] = 0
        r = r2
        r = 2*r - 1
        w = r * w
        F = F + w
        history.append(F)
    ans = {'F': F, 'history': history}
    return ans
ans = fitness(1, [.05], 100, [.6])
F = ans["F"]
print(math.exp((1/100)*math.log10(F[0])))
#print(ans["history"])
time = []
for i in range(1, 101):
    time.append(i)
plt.plot(time, ans["history"])
plt.show()