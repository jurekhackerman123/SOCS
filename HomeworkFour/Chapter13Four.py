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

MUTATIONPROB = 0.01

L = 30



def PeriodicBoundaryConditions(array, row, col): 
    rows, cols = array.shape

    return array[row%rows, col%cols]



def LatticeOfPrisoners(timeSteps, l, numberOfRounds, mutationProb): 

    # create lxl array with random integers between 0 and N 
    lattice = np.random.randint(0, numberOfRounds, (l, l))
    # lattice = np.zeros((l,l))


    print(lattice)
    # lattice = np.full((l+1,l+1), numberOfRounds) - 1
    # lattice = np.ones((l, l))* numberOfRounds
    # lattice = np.zeros((l,l))

    # 
    # lattice[int(3*l/4), int(l/4)] = 0
    # lattice[int(l/4), int(3*l/4)] = 0
    # lattice[int(l/2), int(l/2)] = 0

    # lattice[int(l/2), int(l/2)] = numberOfRounds

    newLattice = lattice.copy()

    latticeListToPlot = []

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
                    newLattice[i, j] = random.randint(0, numberOfRounds)

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
                
        latticeListToPlot.append(lattice.copy())

    return lattice, latticeListToPlot


# def MainAlg(timeSteps): 

#     for timeStep in range(timeSteps): 

TIME = 20

lattice, latticeListToPlot = LatticeOfPrisoners(TIME, 30, NUMBEROFROUNDS, MUTATIONPROB)


print(T, R, P, S)

# PLOT

ax = sns.heatmap(lattice, cmap='viridis', annot=False)
plt.title('Prisoners Dilemma on a lattice, t = ' + str(TIME) + ', R = ' + str(R))
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# can (and should) also add the populationfraction plot here

pop0 = []
pop1 = []
pop2 = []
pop3 = []
pop4 = []
pop5 = []
pop6 = []


print('test: ', len(latticeListToPlot))

for latticeNo in range(len(latticeListToPlot)): 
    latticeOfInterest = latticeListToPlot[latticeNo]

    # print(latticeListToPlot[latticeNo] == latticeListToPlot[latticeNo + 1])

    integersToCount = [0,1,2,3,4,5,6]
    counts = [np.count_nonzero(latticeOfInterest == i) for i in integersToCount]

    pop0.append(counts[0] / sum(counts))
    pop1.append(counts[1] / sum(counts))
    pop2.append(counts[2] / sum(counts))
    pop3.append(counts[3] / sum(counts))
    pop4.append(counts[4] / sum(counts))
    pop5.append(counts[5] / sum(counts))
    pop6.append(counts[6] / sum(counts))

plt.plot(pop0, label = 'pop0')
plt.plot(pop1, label = 'pop1')
plt.plot(pop2, label = 'pop2')
plt.plot(pop3, label = 'pop3')
plt.plot(pop4, label = 'pop4')
plt.plot(pop5, label = 'pop5')
plt.plot(pop6, label = 'pop6')
plt.xlabel('Time')
plt.ylabel('Population Fraction')
plt.legend()
plt.show()

