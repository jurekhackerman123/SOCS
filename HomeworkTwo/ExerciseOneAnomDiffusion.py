import numpy as np
import matplotlib.pyplot as plt 

from scipy.constants import Boltzmann

'''
simulate the trajectories of a Brownian particle under three conditions: 
1. overdamped
2. intertial 
3. trapped 

'''


def OverdampedBrownian(numSteps, T, dT, gamma):

    arrayX = np.zeros(numSteps)
    arrayY = np.zeros(numSteps)

    arrayX[0] = 0
    arrayY[0] = 0

    for iCoord in range(1, numSteps):

        eta = np.sqrt(2*Boltzmann * T * dT / gamma)

        # mean of zero, variance of one 
        arrayX[iCoord] = arrayX[iCoord - 1] + eta * np.random.normal(0, 1)        
        arrayY[iCoord] = arrayY[iCoord - 1] + eta * np.random.normal(0, 1)

    
    return arrayX, arrayY

# testX, testY = OverdampedBrownian(100, 300, 1, 1e-10)



def InertialBrownian(numSteps, T, dT, gamma, m):

    arrayX = np.zeros(numSteps)
    arrayY = np.zeros(numSteps)

    arrayX[0] = 0
    arrayY[0] = 0

    for iCoord in range(1, numSteps):

        factorOne = (2 + dT * (gamma/m)) / (1 + dT * (gamma/m))
        factorTwo = 1 / (1 + dT * (gamma/m))
        factorThree = np.sqrt(2 * Boltzmann * T * gamma) / (m * (1 + dT * (gamma/m))) * (dT)**(3/2)

        arrayX[iCoord] = factorOne * arrayX[iCoord-1] - factorTwo * arrayX[iCoord-2] + factorThree * np.random.normal(0, 1)
        arrayY[iCoord] = factorOne * arrayY[iCoord-1] - factorTwo * arrayY[iCoord-2] + factorThree * np.random.normal(0, 1)

    return arrayX, arrayY



# testX, testY = InertialBrownian(100, 300, 1, 1e-10, 1e-14)



def TrappedBrownian(numSteps, T, dT, gamma, k): 

    arrayX = np.zeros(numSteps)
    arrayY = np.zeros(numSteps)

    arrayX[0] = 0
    arrayY[0] = 0

    for iCoord in range(1, numSteps): 

        factorOne = k/gamma * dT
        factorTwo = np.sqrt(2*Boltzmann * T * dT / gamma)

        arrayX[iCoord] = arrayX[iCoord - 1] - factorOne * arrayX[iCoord - 1] + factorTwo * np.random.normal(0, 1)        
        arrayY[iCoord] = arrayY[iCoord - 1] - factorOne * arrayY[iCoord - 1] + factorTwo * np.random.normal(0, 1)

    return arrayX, arrayY


# testX, testY = TrappedBrownian(10, 300, 1, 1, 1)

# plt.plot(testX, testY)
# plt.scatter(testX[0], testY[0])
# plt.show()


def EMSD(BrownianFunction, numSteps, iterations): 
    
    eMSD = 0 

    for iIteration in range(iterations):

        if BrownianFunction == 'overdamped': 
            arrayX, arrayY = OverdampedBrownian(numSteps, 300, 1, 1e-10)
        elif BrownianFunction == 'inertial': 
            arrayX, arrayY = InertialBrownian(numSteps, 300, 1, 1e-10, 1e-14)
        elif BrownianFunction == 'trapped': 
            arrayX, arrayY = TrappedBrownian(numSteps, 300, 1, 1, 1)

        tempDistance = ( arrayX[-1] - arrayX[0] ) **2 + ( arrayY[-1] - arrayY[0] )**2

        eMSD += tempDistance

    return eMSD

test = EMSD('overdamped', 100, 100)
print(test)


def TMSD(BrownianFunction, numSteps, numDisplacements):

    lenInterval = int(numSteps / numDisplacements)

    # print('leninterval: ', lenInterval)

    if BrownianFunction == 'overdamped': 
        arrayX, arrayY = OverdampedBrownian(numSteps, 300, 1, 1e-10)
    elif BrownianFunction == 'inertial': 
        arrayX, arrayY = InertialBrownian(numSteps, 300, 1, 1e-10, 1e-14)
    elif BrownianFunction == 'trapped': 
        arrayX, arrayY = TrappedBrownian(numSteps, 300, 1, 1, 1)
    else: 
        print('Error, no function given.')
        return


    tMSD = 0

    for i in range(numDisplacements):


        if i == (numDisplacements) - 1: 
            # choose last element in list insted of i+1st 
            tempDistance = (arrayX[i * lenInterval] - arrayX[-1])**2 + (arrayY[i * lenInterval] - arrayY[-1])**2
        
        else: 
            tempDistance = (arrayX[i * lenInterval] - arrayX[(i+1) * lenInterval])**2 + (arrayY[i * lenInterval] - arrayY[(i+1) * lenInterval])**2

        tMSD += tempDistance

    return tMSD



test = TMSD('overdamped', 100, 10)
print(test)

        
