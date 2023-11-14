import numpy as np
import matplotlib.pyplot as plt 
import random

import seaborn as sns

from scipy.stats import linregress

CRITICALTEMPERATURE = 2.269

def InitializeLattice(size):

    lattice = np.zeros((size, size))

    for i in range(size): 
        for j in range(size): 
            randomValue = random.choice([-1, 1])
            lattice[i, j] = randomValue


    return lattice


def UpdateMonteCarloOneAtom(lattice, i, j, H, J, T): 
    spinCurrent = lattice[i, j]

    if i == 0: 
        if j == 0: 
            sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i+1, j] 
        elif j == 199: 
            sumOfNeighbouringSpins = lattice[i, j-1] + lattice[i+1, j]
        else: 
            sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i, j-1] + lattice[i+1, j]
    
    elif i == 199: 
        if j == 0: 
            sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i-1, j] 
        elif j == 199: 
            sumOfNeighbouringSpins = lattice[i, j-1] + lattice[i-1, j]
        else: 
            sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i, j-1] + lattice[i-1, j]
    
    elif j == 0: 
        sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i-1, j] + lattice[i+1, j]

    elif j == 199: 
        sumOfNeighbouringSpins = lattice[i, j-1] + lattice[i-1, j] + lattice[i+1, j]

    else: 
        sumOfNeighbouringSpins = lattice[i, j+1] + lattice[i, j-1] + lattice[i+1, j] + lattice[i-1, j] 


    eMinus = H + J * sumOfNeighbouringSpins
    ePlus =  -(H + J * sumOfNeighbouringSpins)

    # change the spin of the atom
    randomNumber = random.random()

    probPlus = np.exp(-ePlus / T) / ( np.exp(-ePlus / T) + np.exp(-eMinus / T) )

    if randomNumber < probPlus: 
        lattice[i, j] = 1
    else: 
        lattice[i, j] = -1

    
    return lattice



def UpdateLattice(numberOfSteps, H, J, T): 
    lattice = InitializeLattice(200)

    totalElements = 200*200
    elementsOfInterest = int(0.10 * totalElements)

    for iStep in range(numberOfSteps): 

        # Generate random indices without replacement
        randomIndices = np.random.choice(totalElements, elementsOfInterest, replace=False)

        # Now we have 10% of the data, and the indices of this data in the matrix
        rowIndices, colIndices = np.unravel_index(randomIndices, (200, 200))

        # for these indices, we now apply the montecarlo method 
        for iElement in range(elementsOfInterest): 
            lattice = UpdateMonteCarloOneAtom(lattice, rowIndices[iElement], colIndices[iElement], H, J, T)

    return lattice


'''
PLOTTING 2D MAP
'''

lattice = UpdateLattice(1000, 0.1, 1, 1)
sns.heatmap(lattice, cmap='YlGnBu', annot=False)
plt.title('Number of steps: ' + str(10000))
plt.show()



def CalculateMagnetization(lattice): 
    return 1 / 200**2 * np.sum(lattice)

def VariationMagnetization(): 
    '''
    this function varies the external magnetic field and thus measures the magnetization
    '''
    magnetizationList = []

    # this list was to show that after approx. 0.8, the graph is not linear anymore
    # hList = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6]
    hList = [0,0.2, 0.4, 0.6, 0.8]
    for hValue in hList: 
        tempLattice = UpdateLattice(100, hValue, 1, 5)
        magnetizationList.append(CalculateMagnetization(tempLattice))

    '''
    Plotting
    '''

    xData = np.array(hList)
    yData = np.array(magnetizationList)


    # use linregress from scipy to fit the line 
    slope, intercept, rValue, pValue, stdErr = linregress(xData, yData)

    # Calculate the fitted values
    fittedMagnetization = slope * xData + intercept

    # Print the slope and intercept of the line
    print(f"Magnetization found: {slope}")

    # Plot the original data and the fitted line
    plt.scatter(xData, yData)
    plt.plot(xData, fittedMagnetization, color='red')
    plt.xlabel('External Magnetic Field H')
    plt.ylabel('Magnetization m')
    plt.title(f"Magnetization: {np.round(slope, 2)}")
    plt.show()

    return magnetizationList

magnetizationList = VariationMagnetization()
