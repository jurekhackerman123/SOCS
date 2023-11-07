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


def regularize(x,t,T):
    m = np.diff(x)/np.diff(t)                             # Slopes of the different increments 
    t_r = np.arange(T)                                    # Regular times
    x_r = np.zeros(len(t_r))                              # Regularized position array 
    s = 0                                                 # Section number
    for i in range(len(t)-1):
        f = np.where(t_r < t[i+1])[0][-1]                 # Find the end of the segment that the values are to be assigned
        x_r[s:f+1] = x[i] + m[i] * (t_r[s:f+1]-t[i])      # Assign the values of the segment
        s = f+1                                           # Assign the beginning of the next segment 
    return(x_r)

position, time = CreateRandomWalkRandomTimes(50, 300, 1e-7)
regularizedX = regularize(position, time, 300)

plt.scatter(time, position, marker='o', color = 'green')

tTotal = np.arange(len(regularizedX))
plt.scatter(tTotal, regularizedX, marker='*', color='orange')
plt.plot(time, position, '--')
plt.show()
