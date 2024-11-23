# utility function to evaluate chromosome fitness from random walk sim of asset allocation play
import numpy as np
import math
import matplotlib.pyplot as plt

# pop is an n x 3 array, each 3 tuple represents fA, fB, and fN (fN is fraction not allocated)
def fitness(popSize, pop, iterations, prob, gammas, lambdas):
    history = []
    F = np.ones(popSize)
    N = iterations # iterations of kelly game
    pA = prob[0]
    qA = prob[1]
    rA = prob[2]
    pB = prob[3]
    qB = prob[4]
    rB = prob[5]
    ww = pA*pB
    wl = (pA*qB) + ww
    wm = (pA*rB) + wl
    lw = (qA*pB) + wm
    ll = (qA*qB) + lw
    lm = (qA*rB) + ll
    mw = (rA*pB) + lm
    ml = (rA*qB) + mw
    mm = rA*rB        # ml < mm <= 1, else statement
    gamA = gammas[0]
    gamB = gammas[1]
    lamA = lambdas[0]
    lamB = lambdas[1]
    #print(str(ww) + ", " + str(wl) + ", " + str(wm) + ", " + str(lw) + ", " + str(ll) + ", " + str(lm) + ", " + 
    #      str(mw) + ", " + str(ml) + ", " + str(mm) + ", ")
    for i in range(1, N+1):
        r = np.random.normal(.5, .5, popSize)
        r2 = np.ones(popSize)
        for i in range(0, popSize):
            if r[i] <= ww:
                r2[i] = 1 + pop[i][0] * gamA + pop[i][1] * gamB
            elif r[i] > ww and r[i] <= wl:
                r2[i] = 1 + pop[i][0] * gamA - pop[i][1]
            elif r[i] > wl and r[i] <= wm:
                r2[i] = 1 + pop[i][0] * gamA - pop[i][1] * lamB
            elif r[i] > wm and r[i] <= lw:
                r2[i] = 1 - pop[i][0] + pop[i][1] * gamB
            elif r[i] > lw and r[i] <= ll:
                r2[i] = 1 - pop[i][0] - pop[i][1]
            elif r[i] > ll and r[i] <= lm:
                r2[i] = 1 - pop[i][0] - pop[i][1] * lamB
            elif r[i] > lm and r[i] <= mw:
                r2[i] = 1 - pop[i][0] * lamA + pop[i][1] * gamB
            elif r[i] > mw and r[i] <= ml:
                r2[i] = 1 - pop[i][0] * lamA - pop[i][1]
            else:
                r2[i] = 1 - pop[i][0] * lamA - pop[i][1] * lamB
        r = r2
        F = F * r
        history.append(F)
    ans = {'F': F, 'history': history}
    return ans

iter = 10
size = 20
initPop = [[np.random.rand() for _ in range(0, 3)] for _ in range(0, size)]
for i in range(0, size):
    norm = sum(initPop[i])
    for j in range(0, 3):
        initPop[i][j] /= norm
stats = [.7,.1,.2,.4,.4,.2]
gammas = [1,1]
lambdas = [1,1]
ans = fitness(size, initPop, iter, stats, gammas, lambdas)
F = ans["F"]
for i in range(0, len(F)):
    print(math.exp((1/10)*math.log10(F[i])))
#print(ans["history"])
time = []
for i in range(1, size+1):
    time.append(i)
for i in range(0, iter):
    plt.plot(time, ans["history"][i])
plt.show()