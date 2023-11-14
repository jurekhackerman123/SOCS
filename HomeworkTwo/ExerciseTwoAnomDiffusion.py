import numpy as np
import matplotlib.pyplot as plt 

from scipy.constants import Boltzmann
import random


def CreateRandomWalkRandomTimes(numSteps, T, gamma): 
    '''
    return x and t arrays 
    '''

    # is overdamped brownian from exercise before 
    positionArray = np.zeros(numSteps)
    timeArray = np.zeros(numSteps)


    positionArray[0] = 0
    timeArray[0] = 0

    for iCoord in range(1, numSteps):

        # choose random position 
        randomNumber = random.random()
        if randomNumber < 0.1: 
            dT = random.uniform(20, 30)
        else: 
            dT = random.uniform(0.5, 4)

        eta = np.sqrt(2*Boltzmann * T * (dT) / gamma)

        # mean of zero, variance of one 
        positionArray[iCoord] = positionArray[iCoord - 1] + eta * np.random.normal(0, 1)        
        timeArray[iCoord] = timeArray[iCoord-1] + dT
    
    return positionArray, timeArray


positions, times = CreateRandomWalkRandomTimes(50, 300, 1e-7)

# plt.title('Random walk with varying dT')
# plt.plot(positions, label = 'Random walk')

# plt.show()



def regularize(x,t,T):
    m = np.diff(x)/np.diff(t)                             # Slopes of the different increments 
    t_r = np.arange(T)                                    # Regular times
    x_r = np.zeros(len(t_r))                              # Regularized position array 
    s = 0                                                 # Section number
    for i in range(len(t)-1):
        f = np.where(t_r < t[i+1])[0][-1]                 # Find the end of the segment that the values are to be assigned
        x_r[s:f+1] = x[i] + m[i] * (t_r[s:f+1]-t[i])      # Assign the values of the segment
        s = f+1                                           # Assign the beginning of the next segment 
    return(x_r, t_r)


def Regularize(position, time, T):
    newTime = np.arange(T)
    newPosition = np.zeros(T)

    for i in range(T):
        # go through every element in t 
        iTime = newTime[i]

        for j in range(len(time)):
            jTime = time[j]
            if jTime > iTime: 

                if j == 0:
                    tPrev = time[j]
                    tNext = jTime

                    xPrev = position[j]
                    xNext = position[j]

                    break
                
                # in the case that j == i -> tPrev
                tPrev = time[j-1]
                tNext = jTime

                xPrev = position[j-1]
                xNext = position[j]

                break



        newPosition[i] = xPrev + ( xNext - xPrev ) / ( tNext - tPrev ) * (iTime - tPrev)

    return newPosition, newTime
            



position, time = CreateRandomWalkRandomTimes(50, 300, 1e-7)
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

tTotal = np.arange(len(regularizedX))
plt.scatter(regularizedTime, regularizedX, marker='*', color='orange')
plt.plot(time, position, '--')
plt.show()


# plt.plot(regularizedX, label = 'Regularized')
# plt.plot(normalizedPositions, label = 'Normalized')
# plt.legend()
# plt.show()
