import numpy as np
import matplotlib.pyplot as plt 

from scipy.constants import Boltzmann

'''
simulate the trajectories of a Brownian particle under three conditions: 
1. overdamped
2. intertial 
3. trapped 

Questions: 

what timeframe for number of steps? 
Do we have to recreate the plots? 
HOw do times and number of steps relate? 




'''

M = 1.11 * 10**-14
T = 300
R = 10**-3
ETA = 0.001
GAMMA = 6 * np.pi * ETA * R

DT = 10e-3


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

KX = 10**-6
KY = 0.25 * 10**-6
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
        else: 
            print('No valid function given.')
            return

        tempDistance = ( arrayX[-1] - arrayX[0] )**2 #+ ( arrayY[-1] - arrayY[0] )**2

        eMSD += tempDistance
    
    eMSD = eMSD/ (iterations)

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

    displacementFactor -= 1

    tMSD = 0

    count = 0

    for i in range(trajectoryLenght - displacementFactor):


        tempDistance = (arrayX[i] - arrayX[i + displacementFactor])**2 #+ (arrayY[i] - arrayY[i + displacementFactor])**2

        tMSD += tempDistance


        count += 1

    tMSD = tMSD/((count))

    return tMSD


stringOfInterest = 'trapped'

test = EMSD(stringOfInterest, 10, 1000)
print(test)
test2 = TMSD(stringOfInterest, 1000, 10)
print(test2)

# exit()

def GenerateMSDPlot(title): 
    stepsList = [10,20,30,40,50,60,70,80,90,100, 200, 300, 400, 500, 600, 700, 800, 900]
    # stepsList = [1, 5, 10, 50, 100, 500, 1000]
    # stepsList = np.arange(0,20)
    # stepsList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    # stepsList = [10,20,30,40,50,60,70,80,90,100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    # stepsList = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]

    xStepsList = np.log( np.array(stepsList))




    msdList = []
    tmsdList = []

    for step in range(len(stepsList)): 
        msdList.append(EMSD(title, stepsList[step], 1000))
        tmsdList.append(TMSD(title, 1000000, stepsList[step]))

    for i in msdList: 
        print(np.log(i))

    # plt.plot(xStepsList, stepsList, label = 'alpha = 1')

    stepsList = 10e-3*np.array(stepsList)

    plt.scatter(stepsList, msdList, label='emsd')
    plt.scatter(stepsList, tmsdList, label = 'tmsd', marker= '+')

    

    # plt.loglog(stepsList, msdList, label = 'msd')
    # plt.loglog(stepsList, tmsdList, label = 'tmsd')
    
    plt.title(title)
    plt.legend()

    plt.xscale('log')
    plt.yscale('log')
    
    plt.show()

GenerateMSDPlot(stringOfInterest)
