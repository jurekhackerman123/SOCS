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



def PeriodicBoundaryConditions(array, row, col): 
    rows, cols = array.shape

    return array[row%rows, col%cols]



def LatticeOfPrisoners(timeSteps, l, numberOfRounds, mutationProb): 

    # create lxl array with random integers between 0 and N 
    # lattice = np.random.choice([0, numberOfRounds], (l, l))
    # lattice = np.zeros((l,l))

    # lattice = np.full((l+1,l+1), numberOfRounds) - 1
    lattice = np.ones((l, l))* numberOfRounds
    # lattice = np.zeros((l,l))

    # 
    # lattice[int(3*l/4), int(l/4)] = 0
    # lattice[int(l/4), int(3*l/4)] = 0
    # lattice[int(l/2), int(l/2)] = 0

    # lattice[int(2*l/3), int(l/3)] = 0
    # lattice[int(l/3), int(2*l/3)] = 0


    lattice[int(l/2), int(l/2)] = 0

    # cluster 
    # lattice[int(3/6 * l): int(2/3 * l), int(3/6 * l) : int(2/3 * l)] = 0

    newLattice = lattice.copy()


    for timeStep in range(timeSteps): 
        # lattice = newLattice.copy()

        # iterate over lattice 
        for i in range(l): 

            for j in range(l): 

                neighbours = [PeriodicBoundaryConditions(lattice, i-1, j), 
                              PeriodicBoundaryConditions(lattice, i+1, j), 
                              PeriodicBoundaryConditions(lattice, i, j+1), 
                              PeriodicBoundaryConditions(lattice, i, j-1)]


                yearsList = []

                for neighbour in neighbours: 
                    yearsList.append(PrisonersDilemma(numberOfRounds, lattice[i, j], neighbour)[0])

                newValue = 0

                for k in range(len(yearsList)):
                    newValue += yearsList[k]


                # bestValue = min(yearsList)

                # if PrisonersDilemma(numberOfRounds, lattice[i, j], lattice[i, j])[0] <= bestValue:
                #     # print(i, j, 'better in round', timeStep)
                #     newLattice[i, j] = lattice[i, j]
                # else: 

                #     bestIndices = [i for i, value in enumerate(yearsList) if value == bestValue]

                #     chosenIndex = random.choice(bestIndices)

                #     # update this value 
                #     newLattice[i, j] = neighbours[chosenIndex]
                    
                newLattice[i, j] = newValue

                # print('newvalueefkadfkjadbkjba:', newValue)
                # print('INDEX:::', i, j)


                randomNumber = random.random()

                # mutation
                if randomNumber < mutationProb: 
                    newLattice[i, j] = random.choice([0, numberOfRounds])

                # print(newLattice)
    
        # lattice = newLattice.copy()

        # # when lattice has been filled with corresponding values, iterate over the lattice again and update the values 
        for i in range(l):

            for j in range(l): 

                neighboursNew = [PeriodicBoundaryConditions(newLattice, i-1, j), 
                                PeriodicBoundaryConditions(newLattice, i+1, j), 
                                PeriodicBoundaryConditions(newLattice, i, j+1), 
                                PeriodicBoundaryConditions(newLattice, i, j-1)]

                neighboursOld = [PeriodicBoundaryConditions(lattice, i-1, j), 
                                PeriodicBoundaryConditions(lattice, i+1, j), 
                                PeriodicBoundaryConditions(lattice, i, j+1), 
                                PeriodicBoundaryConditions(lattice, i, j-1)]

                # if i == 2 and j == 1: 
                #     print(neighbours)

                bestValue = min(neighboursNew)

                bestIndices = [i for i, value in enumerate(neighboursNew) if value == bestValue]

                chosenIndex = random.choice(bestIndices)

                # for k in range(len(neighbours)): 
                #     if neighbours[k] < lattice[i, j]: 
                #         newLattice[i, j] = neighbours[k]

                if bestValue < newLattice[i, j]: 
                    lattice[i, j] = neighboursOld[chosenIndex]
                else: 
                    lattice[i, j] = lattice[i, j]


        # print(lattice)
                


    return lattice


# def MainAlg(timeSteps): 

#     for timeStep in range(timeSteps): 

TIME = 20

lattice = LatticeOfPrisoners(TIME, 30, NUMBEROFROUNDS, MUTATIONPROB)


print(T, R, P, S)

# PLOT

ax = sns.heatmap(lattice, cmap='viridis', annot=False)
plt.title('Prisoners Dilemma on a lattice, t = ' + str(TIME))
plt.xlabel('x')
plt.ylabel('y')
plt.show()