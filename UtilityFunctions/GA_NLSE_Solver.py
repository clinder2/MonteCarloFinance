# Genetic algorithm to solve nonlinear systems of equ. for capital allocation
# chromosome is fraction s.t. 0<f<1
from kellyFitness import fitness
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def GA(popSize, numPlays, generations):
    chromPop = np.random.rand(numPlays+1, popSize)
    #chromPop = [[np.random.rand() for _ in range(0, popSize)] for _ in range(0, numPlays+1)] # add extra play for unallocated capital
    for t in range(0, popSize):
        temp = 0
        for row in range(0,numPlays+1):
            if (chromPop[row][t] < 0):
                chromPop[row][t] = -1 * chromPop[row][t]
            temp = temp + chromPop[row][t]
        for row in range(0, numPlays+1):
            chromPop[row][t] /= temp
    # GA PARAMETERS
    elitism = 0.1
    pm = 0.1 # prob. mutation
    orelax = 1.4 # over relaxation factor for mating
    epsilon = 0.07 # mutation range
    evect = np.full((numPlays+1, popSize), epsilon)
    bestFitness = 0
    stats = [.5,.1,.2,.4,.4,.2]
    gammas = [3,1]
    lambdas = [1,3]
    data = fitness(popSize, chromPop, 20, stats, gammas, lambdas)
    bestFitness = max(data["F"])
    BEST = []
    for i in range(0, generations):
        data = fitness(popSize, chromPop, 20, stats, gammas, lambdas)
        fit = list(data["F"])
        sorted = np.argsort(fit)[::-1]
        ordered = [[0]*popSize for j in range(numPlays + 1)]
        index = 0
        for s in sorted:
            for j in range(0, numPlays+1):
                ordered[j][index] = chromPop[j][s]
            index = index + 1
        if data["F"][sorted[0]] > bestFitness:
            bestFitness = data["F"][sorted[0]]
            histories = data["history"]
            Temp = []
            for j in range(0, len(histories)):
                Temp.append(histories[j][sorted[0]])
            BEST.append(Temp)
        """ for j in range(0, popSize):
            Temp = []
            histories = data["history"]
            for t in range(0, len(histories)):
                Temp.append(histories[t][j])
            BEST.append(Temp) """
        newPop = [[0]*popSize for j in range(numPlays + 1)]
        elite = int(elitism * popSize)
        """ for col in range(0, popSize):
            print(col)
            for row in range(0, numPlays+1):
                print(chromPop[row][col]) """
        ## MUTATION
        r = np.random.normal(.5, .5, popSize)
        r2 = np.ones(popSize)
        for j in range(0, len(r)):
            if r[j] >= pm:
                r2[j] = 0
        r = r2 # mutate indices s.t. r[i] = 1
        a = chromPop - evect
        a[a<0] = 0
        b = chromPop + evect
        b[b>1] = 1
        mutations = np.zeros((numPlays+1, popSize))
        for row in range(0, numPlays+1):
            mutations[row] = r * (a[row] + (b[row]-a[row])*[np.random.rand() for _ in range(0, popSize)])
        for row in range(0, numPlays+1):
            chromPop[row] -= chromPop[row] * r
        chromPop += mutations
        ## MATING (crossover)
        permPop = chromPop.copy() # make random permutation
        for col in range(0, popSize):
            k = col + (popSize - col) * np.random.rand()
            k = int(k)
            temp = permPop[:,col].copy()
            permPop[:,col] = permPop[:,k]
            permPop[:,k] = temp
        nextGen = chromPop + orelax*(permPop - chromPop)*np.random.rand(numPlays+1, popSize)
        chromPop = nextGen
        #chromPop = chromPop / np.sum(chromPop, axis=1)[:,np.newaxis]
        for t in range(0, popSize):
            temp = sum(chromPop[:,t])
            chromPop[:,t] /= temp
        # Preserve elites
        for j in range(0, elite):
            for s in range(0, numPlays + 1):
                newPop[s][j] = ordered[s][j]
        # Randomly select from modified population
        indicies = []
        for t in range(0, popSize):
            indicies.append(t)
        r = random.sample(indicies, popSize - elite)
        t = elite
        for j in r:
            for s in range(0, numPlays + 1):
                newPop[s][t] = chromPop[s][j]
            t = t + 1
        chromPop = newPop
        for t in range(0, popSize):
            temp = 0
            for row in range(0,numPlays+1):
                if chromPop[row][t] < 0:
                    chromPop[row][t] = -1 * chromPop[row][t]
                temp = temp + chromPop[row][t]
            for row in range(0, numPlays+1):
                chromPop[row][t] /= temp
        print("fitness: " + str(bestFitness))
        """ for t in range(0, popSize):
            print(chromPop[:,t])
        for t in range(0, popSize):
            print(nextGen[:][t] - chromPop[:][t]) """
    return BEST

if __name__ == "__main__":
    popSize = 10
    BEST = GA(popSize, 2, 10)
    time = []
    for ind in range(1, 21):
        time.append(ind)
    for best in BEST:
        plt.plot(time, best)
    plt.show()