# Genetic algorithm to solve nonlinear systems of equ. for capital allocation
# chromosome is fraction s.t. 0<f<1
import numpy as np
import math

def GA(popSize, numPlays, generations):
    chromPop = [[np.random.rand() for _ in range(0, popSize)] for _ in range(0, numPlays+1)] # add extra play for unallocated capital
    for t in range(0, popSize):
        temp = 0
        for row in range(0,numPlays+1):
            temp = temp + chromPop[row][t]
        for row in range(0, numPlays+1):
            chromPop[row][t] /= temp
    pm = 0.1 # prob. mutation
    orelax = 1.4 # over relaxation factor for mating
    epsilon = 0.07 # mutation range
    evect = np.full((numPlays+1, popSize), epsilon)
    bestFitness = 0
    for i in range(0, generations):
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
        for row in range(0, numPlays+1):
            index = 1
            if row % 2 == 0:
                while index < popSize:
                    temp = chromPop[row][index]
                    chromPop[row][index] = chromPop[row][index-1]
                    chromPop[row][index-1] = temp
                    index = index + 2
            else:
                index = 2
                while index < popSize:
                    temp = chromPop[row][index]
                    chromPop[row][index] = chromPop[row][index-1]
                    chromPop[row][index-1] = temp
                    index = index + 2
        for t in range(0, popSize):
            temp = sum(chromPop[:,t])
            chromPop[:,t] /= temp
        for t in range(0, popSize):
            print(chromPop[:,t])

GA(3, 2, 1)