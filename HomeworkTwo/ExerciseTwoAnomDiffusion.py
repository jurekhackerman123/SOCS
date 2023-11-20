import numpy as np
import matplotlib.pyplot as plt 

from scipy.constants import Boltzmann
import random


'''
other approach to forming trajectory
'''

# def CreateRandomWalkRandomTimes(numSteps, T, gamma): 
#     '''
#     return x and t arrays 
#     '''

#     # is overdamped brownian from exercise before 
#     positionArray = np.zeros(numSteps)
#     timeArray = np.zeros(numSteps)


#     positionArray[0] = 0
#     timeArray[0] = 0

#     for iCoord in range(1, numSteps):

#         # choose random position 
#         randomNumber = random.random()
#         if randomNumber < 0.1: 
#             dT = random.uniform(20, 30)
#         else: 
#             dT = random.uniform(0.5, 4)

#         eta = np.sqrt(2*Boltzmann * T * (dT) / gamma)

#         # mean of zero, variance of one 
#         positionArray[iCoord] = positionArray[iCoord - 1] + eta * np.random.normal(0, 1)        
#         timeArray[iCoord] = timeArray[iCoord-1] + dT
    
#     return positionArray, timeArray




def BrownianMotionVaryingTime(T,alpha):
    # t = np.arange(T)                        # Take the power (alpha) of time

    # x as usual
    # create random positions with positions between -T and T 
    randomPositionsArray = np.random.randn(T)

    positionArray = np.cumsum(randomPositionsArray)       # Regular Brownian motion

    timeArray = np.zeros(T)

    # but for times, want dT to be irregular: 
    for iCoord in range(1, T):

        # choose random position 
        randomNumber = random.random()
        if randomNumber < 0.1: 
            dT = random.uniform(20, 30)
        else: 
            dT = random.uniform(0.5, 4)


        # # mean of zero, variance of one 
        # positionArray[iCoord] = positionArray[iCoord - 1] + eta * np.random.normal(0, 1)        
        timeArray[iCoord] = timeArray[iCoord-1] + dT


    return(positionArray, timeArray)



# positions, times = CreateRandomWalkRandomTimes(50, 300, 1e-7)
positions, times = BrownianMotionVaryingTime(50, 1)
# plt.title('Random walk with varying dT')
# plt.plot(times, positions, label = 'Random walk')

# plt.show()
# exit()



def Regularize(position, time, T):

    # to stop regularizing after the time the initial trajectory has passed 
    maxTime = int( time[-1] )

    newTime = np.arange(maxTime)
    newPosition = np.zeros(maxTime)

    for i in range(maxTime):
        # go through every element in t 
        iTime = newTime[i]


        indices = np.where(time > iTime)

        # first element in np.array is the one of interest 
        indexOfInterest = indices[0][0]


        if indexOfInterest == 0:
            tPrev = time[indexOfInterest]
            tNext = time[indexOfInterest]

            xPrev = position[indexOfInterest]
            xNext = position[indexOfInterest]

        else: 
            tPrev = time[indexOfInterest-1]
            tNext = time[indexOfInterest]

            xPrev = position[indexOfInterest-1]
            xNext = position[indexOfInterest]



        newPosition[i] = xPrev + ( xNext - xPrev ) / ( tNext - tPrev ) * (iTime - tPrev)

    return newPosition, newTime


# position, time = CreateRandomWalkRandomTimes(50, 300, 1e-7)
position, time = BrownianMotionVaryingTime(100, 1)
regularizedX, regularizedTime = Regularize(position, time, 300)

# plt.title('Regularized Trajectory')
# plt.plot(regularizedX)

# plt.show()


'''
Normalize
'''

def Normalize(positionList): 

    # calculate stdev 
    std = np.std(positionList)

    # set std to one
    newPositionList = positionList * (1/std)


    mean = np.mean(newPositionList)

    newPositionList = newPositionList - mean

    return newPositionList

    # for iStep in range(1, len(position)): 


normalizedPositions = Normalize(regularizedX)



# plt.scatter(time, position, marker='o', color = 'green')

# plt.scatter(regularizedTime, regularizedX, marker='*', color='orange', label = 'Regularized')
# plt.plot(time, position, '--', label = 'Trajectory')
# plt.plot(normalizedPositions, label = 'Normalized')
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('Regularized Trajectory')
# plt.legend()
# plt.show()


# plt.plot(regularizedX, label = 'Regularized')
# plt.plot(normalizedPositions, label = 'Normalized')
# plt.legend()
# plt.show()
