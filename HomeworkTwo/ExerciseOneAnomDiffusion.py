import numpy as np
import matplotlib.pyplot as plt 

from scipy.constants import Boltzmann

'''
simulate the trajectories of a Brownian particle under three conditions: 
1. overdamped
2. intertial 
3. trapped 

'''

M = 1.11 * 10**-14
T = 300
R = 10**-3
ETA = 0.001
GAMMA = 6 * np.pi * ETA * R

DT = 1


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

# testX, testY = OverdampedBrownian(1000, T, 0.1, GAMMA)



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





# testX, testY = InertialBrownian(1000, T, 1, GAMMA, M)



def TrappedBrownian(numSteps, T, dT, gamma, kX, kY): 

    arrayX = np.zeros(numSteps)
    arrayY = np.zeros(numSteps)

    arrayX[0] = 0
    arrayY[0] = 0

    for iCoord in range(1, numSteps): 

        factorOneX = kX/gamma * dT
        factorOneY = kY/gamma * dT
        factorTwo = np.sqrt(2*Boltzmann * T * dT / gamma)

        arrayX[iCoord] = arrayX[iCoord - 1] - factorOneX * arrayX[iCoord - 1] + factorTwo * np.random.normal(0, 1)        
        arrayY[iCoord] = arrayY[iCoord - 1] - factorOneY * arrayY[iCoord - 1] + factorTwo * np.random.normal(0, 1)

    return arrayX, arrayY

KX = 10**-5
KY = 0.25 * 10**-5
# testX, testY = TrappedBrownian(1000, T, 0.1, GAMMA, KX, KY)



# plt.plot(testX, testY)
# plt.scatter(testX[0], testY[0])
# plt.show()
# exit()

def EMSD(BrownianFunction, numSteps, iterations): 
    
    eMSD = 0 

    for iIteration in range(iterations):

        if BrownianFunction == 'overdamped': 
            arrayX, arrayY = OverdampedBrownian(numSteps, T, DT, GAMMA)
        elif BrownianFunction == 'inertial': 
            arrayX, arrayY = InertialBrownian(numSteps, T, DT, GAMMA, M)
        elif BrownianFunction == 'trapped': 
            arrayX, arrayY = TrappedBrownian(numSteps, T, DT, GAMMA, KX, KY)

        tempDistance = ( arrayX[-1] - arrayX[0] )**2 + ( arrayY[-1] - arrayY[0] )**2

        eMSD += tempDistance
    
    eMSD = eMSD/ (iterations * numSteps)

    return eMSD




def TMSD(BrownianFunction, numSteps, displacementFactor):

    # lenInterval = int(numSteps / numDisplacements)

    # print('leninterval: ', lenInterval)

    if BrownianFunction == 'overdamped': 
        arrayX, arrayY = OverdampedBrownian(numSteps, T, DT, GAMMA)
    elif BrownianFunction == 'inertial': 
        arrayX, arrayY = InertialBrownian(numSteps, T, DT, GAMMA, M)
    elif BrownianFunction == 'trapped': 
        arrayX, arrayY = TrappedBrownian(numSteps, T, DT, GAMMA, KX, KY)
    else: 
        print('Error, no function given.')
        return

    trajectoryLenght = len(arrayX)

    tMSD = 0

    print('DEBUDEBU')
    print(trajectoryLenght - displacementFactor)

    for i in range(trajectoryLenght - displacementFactor):


        tempDistance = (arrayX[i] - arrayX[i + displacementFactor])**2 + (arrayY[i] - arrayY[i + displacementFactor])**2

        tMSD += tempDistance

    tMSD = tMSD/((trajectoryLenght-displacementFactor) * displacementFactor)

    return tMSD


test = EMSD('overdamped', 10, 100000)
print(test)
test2 = TMSD('overdamped', 100000, 11)
print(test2)

        
