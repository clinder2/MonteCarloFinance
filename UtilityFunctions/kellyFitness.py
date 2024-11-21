# utility function to evaluate chromosome fitness from random walk sim of asset allocation play
import numpy as np
import math

def fitness(popSize, pop):
    F = np.ones(popSize)
    N = 1 # iterations of kelly game
    for i in range(1, N+1):
        w = F * pop
        print(w)
fitness(3, [2,2,2])