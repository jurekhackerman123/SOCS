import numpy as np 
import matplotlib.pyplot as plt 
import random

import seaborn as sns

from Chapter13One import *




# I defect, other cooperates
T = 0 
# both cooperate
R = 0.9
# both defect 
P = 1      
# I cooperate, other defects  
S = 1.5

NUMBEROFROUNDS = 7

MUTATIONPROB = 0

L = 30




def LatticeOfPrisoners(timeSteps, l, numberOfRounds, mutationProb): 

    # create lxl array with random integers between 0 and N 
    # lattice = np.random.choice([0, numberOfRounds], (l, l))
    # lattice = np.zeros((l,l))

    lattice = np.full((l,l), numberOfRounds)
    lattice[10, 10] = 0

    newLattice = np.full((l,l), numberOfRounds)
    newLattice[10, 10] = 0



    for timeStep in range(timeSteps): 
        lattice = newLattice.copy()

        # iterate over lattice 
        for i in range(l): 
            for j in range(l): 

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
                    yearsList.append(PrisonersDilemma(numberOfRounds, lattice[i, j], neighbour))

                bestValue = min(yearsList)

                bestIndices = [i for i, value in enumerate(yearsList) if value == bestValue]

                chosenIndex = random.choice(bestIndices)

                # update this value 
                newLattice[i, j] = neighbours[chosenIndex]
                    

                randomNumber = random.random()

                # mutation
                if randomNumber < mutationProb: 
                    newLattice[i, j] = random.choice([0, numberOfRounds])
    



    return newLattice


# def MainAlg(timeSteps): 

#     for timeStep in range(timeSteps): 

TIME = 1

lattice = LatticeOfPrisoners(TIME, 20, 10, MUTATIONPROB)
# print(np.shape(lattice))

print(lattice)

ax = sns.heatmap(lattice, cmap='viridis', annot=False)

plt.title('Prisoners Dilemma on a lattice, t = ' + str(TIME))

# Show the plot
# ax.invert_yaxis()
plt.xlabel('x')
plt.ylabel('y')
plt.show()