# Genetic algorithm to solve nonlinear systems of equ. for capital allocation
# chromosome is fraction s.t. 0<f<1
from kellyFitness import fitness
import numpy as np
import math

def GA(popSize, numPlays, generations):
    chromPop = np.random.rand(numPlays+1, popSize)
    #chromPop = [[np.random.rand() for _ in range(0, popSize)] for _ in range(0, numPlays+1)] # add extra play for unallocated capital
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
    stats = [.7,.1,.2,.4,.4,.2]
    gammas = [1,1]
    lambdas = [1,1]
    #data = fitness(popSize, chromPop, 10, stats, gammas, lambdas)
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
        permPop = chromPop.copy()
        for col in range(0, popSize):
            k = col + (popSize - col) * np.random.rand()
            k = int(k)
            temp = permPop[:,col].copy()
            permPop[:,col] = permPop[:,k]
            permPop[:,k] = temp
        nextGen = chromPop + orelax*(permPop - chromPop)*np.random.rand(numPlays+1, popSize)
        for t in range(0, popSize):
            temp = sum(chromPop[:,t])
            chromPop[:,t] /= temp
        for t in range(0, popSize):
            print(chromPop[:,t])
        for t in range(0, popSize):
            print(nextGen[:,t] - chromPop[:,t])

GA(10, 2, 1)