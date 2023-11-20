import numpy as np
import matplotlib.pyplot as plt 

from ExerciseTwoAnomDiffusion import *

'''
scaled brownian motion 


2 do: 
regularize umschreiben, 
CTRW umschreiben 
SBM umschreiben 
LW umschreiben


'''


def ScaledBrownianMotion(T,alpha):

    # range for time is T, scale it by **alpha, so that we can show them in the same plot 
    timeRange = np.ceil(T**alpha)
    timeRange = int(timeRange)

    randomPositions = np.random.randn(timeRange)

    times = np.arange(timeRange)**(1/alpha) 

    positions = np.cumsum(randomPositions)

    positions, timeArr = Regularize(positions,times,T)
    return positions

alphaList = [0.5, 1, 2]


# plot

for alpha in alphaList: 
    position = ScaledBrownianMotion(200, alpha)
    position = Normalize(position)
    plt.plot(position, label = 'alpha='+str(alpha))
    plt.title('1D Trajectory of Scaled Brownian Motion')
    plt.xlabel('Time [s]')
    plt.ylabel('x')
    plt.legend()
plt.show()


def TwoDimensionalSBM(T,alpha):

    # create range for the time to be in 
    timeRange = np.ceil(T**alpha)
    timeRange = int(timeRange)

    # create list of Positions
    randomPositionsX = np.random.randn(timeRange)
    randomPositionsY = np.random.randn(timeRange)

    # create list of times in the timeFrame
    times = np.arange(timeRange)**(1/alpha) 

    # assemble positions to trajectories 
    xPositions = np.cumsum(randomPositionsX)  
    yPositions = np.cumsum(randomPositionsY)   
    xPositions, timeArr = Regularize(xPositions,times,T)
    yPositions, timeArr = Regularize(yPositions,times,T)
    return xPositions, yPositions




# plot

for alpha in alphaList: 
    position2D = TwoDimensionalSBM(500, alpha)
    x2D = position2D[0]
    y2D = position2D[1]

    x2D = Normalize(x2D)
    y2D = Normalize(y2D)

    plt.plot(x2D, y2D, label = 'alpha=' + str(alpha))


plt.title('2D Trajectory, Scaled Brownian Motion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


'''
Now, for the MSD calculation

works, for alpha = 1, they're the same. 

'''

numIterations = 100

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

eMsdList = []
tMsdList = []

for time in timeList: 
    
    print(time)

    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = ScaledBrownianMotion(time, 1.5)
        eMsd += (position[0] - position[-1])**2

    eMsdList.append(eMsd / numIterations)


    # tmsd

    tMsd = 0
    positionTMsd = ScaledBrownianMotion(10000, 1.5)

    count = 0

    for i in range(10000-time):
        # print(i)
        tempDistance = (positionTMsd[i] - positionTMsd[i + time-1])**2

        tMsd += tempDistance
        count += 1

    tMsdList.append(tMsd / count)



plt.plot(timeList, eMsdList, label = 'EMSD')
plt.plot(timeList, tMsdList, label = 'TMSD')
plt.title('MSD for alpha = 1.5, Scaled Brownian Motion')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Time [s]')
plt.ylabel('MSD [m]')

plt.show()





