import numpy as np 
import matplotlib.pyplot as plt 
import random

import seaborn as sns

from Chapter13One import *




# # I defect, other cooperates
# T = 1
# # both cooperate
# R = 1.5
# # both defect 
# P = 0   
# # I cooperate, other defects  
# S = 0.9

NUMBEROFROUNDS = 7

MUTATIONPROB = 0

L = 30




def LatticeOfPrisoners(timeSteps, l, numberOfRounds, mutationProb): 

    # create lxl array with random integers between 0 and N 
    # lattice = np.random.choice([0, numberOfRounds], (l, l))
    # lattice = np.zeros((l,l))

    # lattice = np.full((l+1,l+1), numberOfRounds) - 1
    lattice = np.ones((l, l))* numberOfRounds
    lattice[int(l/2), int(l/2)] = 0

    # newLattice = np.full((l,l), numberOfRounds)
    # newLattice[int(l/2), int(l/2)] = 0

    newLattice = lattice.copy()


    for timeStep in range(timeSteps): 
        lattice = newLattice.copy()

        # iterate over lattice 
        for i in range(l): 

            for j in range(l): 

                neighbours = []
                yearsList = []
                bestValue = 0
                bestIndices = []
                chosenIndex = 0


                # boundary conditions: 
                if i == 0:

                    if j == 0: 
                        neighbours = [lattice[i+1, j], lattice[i, j+1]]

                    elif j == l-1:
                        neighbours = [lattice[i+1, j], lattice[i, j-1]]

                    else: 
                        neighbours = [lattice[i+1, j], lattice[i, j+1], lattice[i, j-1]]
                        
                elif i == l-1: 

                    if j == 0: 
                        neighbours = [lattice[i-1, j], lattice[i, j+1]]

                    elif j == l-1: 
                        neighbours = [lattice[i-1, j], lattice[i, j-1]]

                    else: 
                        neighbours = [lattice[i-1, j], lattice[i, j+1], lattice[i, j-1]]
                
                else: 

                    if j == 0: 
                        neighbours = [lattice[i-1, j], lattice[i+1, j], lattice[i, j+1]]

                    elif j == l-1: 
                        neighbours = [lattice[i-1, j], lattice[i+1, j], lattice[i, j-1]]

                    else: 
                        neighbours = [lattice[i-1, j], lattice[i+1, j], lattice[i, j+1], lattice[i, j-1]]


                yearsList = []

                for neighbour in neighbours: 
                    yearsList.append(PrisonersDilemma(numberOfRounds, lattice[i, j], neighbour)[1])



                bestValue = min(yearsList)

                if PrisonersDilemma(numberOfRounds, lattice[i, j], lattice[i, j])[0] <= bestValue:
                    # print(i, j, 'better in round', timeStep)
                    newLattice[i, j] = lattice[i, j]
                else: 

                    bestIndices = [i for i, value in enumerate(yearsList) if value == bestValue]

                    chosenIndex = random.choice(bestIndices)

                    # update this value 
                    newLattice[i, j] = neighbours[chosenIndex]
                    

                randomNumber = random.random()

                # mutation
                if randomNumber < mutationProb: 
                    newLattice[i, j] = random.choice([0, numberOfRounds])

            # print(newLattice)
    



    return newLattice


# def MainAlg(timeSteps): 

#     for timeStep in range(timeSteps): 

TIME = 20

lattice = LatticeOfPrisoners(TIME, L, NUMBEROFROUNDS, MUTATIONPROB)


print(T, R, P, S)

# PLOT

ax = sns.heatmap(lattice, cmap='viridis', annot=False)
plt.title('Prisoners Dilemma on a lattice, t = ' + str(TIME))
plt.xlabel('x')
plt.ylabel('y')
plt.show()