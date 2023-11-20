import numpy as np 
import matplotlib.pyplot as plt 

from ExerciseTwoAnomDiffusion import *


'''
levy walk 
'''

def LevyWalk(T,alpha):
    # both times and positions start at 0
    positions = [0]
    times = [(random.random())**(-1/(3-alpha)) ]

    constVelocity = 1

    # while times[-1]<T:
    for iteration in range(T):

        if times[-1] >= T: 
            break

        dT = (random.uniform(1e-10, 1))**(-1/(3-alpha))  
        times.append(times[iteration] + dT)
        positions.append(positions[iteration] + constVelocity * np.random.uniform(-1,1)*dT)

    positions, timeArr = Regularize(positions,times,T)

    # positions = Normalize(positions)

    return positions


# alphaList = [1, 2]

# for alpha in alphaList: 
#     position = LevyWalk(200, alpha)
#     plt.plot(position, label = 'alpha='+str(alpha))
#     plt.legend()
# plt.title('1D Trajectory, Levy Walk')
# plt.xlabel('Time [s]')
# plt.ylabel('x')
# plt.show()



def TwoDimLevyWalk(T,alpha):
    times = [0]
    xPositions = [0]
    yPositions = [0]
    constVelocity = 1
    for iteration in range(T): 

        if times[-1] >= T: 
            break 

        dT = (random.random())**(-1/(3-alpha))          # Flight time distribution
        times.append(times[-1] + dT)
        theta = random.random()*2*np.pi
        xPositions.append(xPositions[-1] + constVelocity * np.cos(theta)*dT)               # Particle moves randomly in 2D
        yPositions.append(yPositions[-1] + constVelocity * np.sin(theta)*dT)               # Particle moves randomly in 2D
    xPositions, timeArray = Regularize(xPositions,times,T)
    yPositions, timeArray = Regularize(yPositions,times,T)
    xPositions = Normalize(xPositions)
    yPositions = Normalize(yPositions)
    return(xPositions,yPositions)





# for alpha in alphaList: 
#     position2D = TwoDimLevyWalk(500, alpha)
#     x2D = position2D[0]
#     y2D = position2D[1]

#     x2D = Normalize(x2D)
#     y2D = Normalize(y2D)

#     plt.plot(x2D, y2D, label = 'alpha=' + str(alpha))
# plt.title('2D Trajectory, Levy Walk')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()




'''
Now, for the MSD
'''
numIterations = 10000

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
# timeList = [10, 100, 1000, 5000]
# timeList = [1,2,3,4,5,6,7,8,9,10]
eMsdList = []
tMsdList = []

for time in timeList: 
    
    print(time)
    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = LevyWalk(time, 1)
        # print(position[0] - position[-1])
        diff = position[0] - position[-1]
        eMsd += diff**2

    print(eMsd)

    eMsdList.append(eMsd / numIterations)


    # tmsd

    tMsd = 0
    positionTMsd = LevyWalk(10000, 1)
    count = 0

    for i in range(10000-time):
        # print(i)
        tempDistance = (positionTMsd[i] - positionTMsd[i + time-1])**2

        tMsd += tempDistance
        count += 1

    tMsdList.append(tMsd / count)



plt.plot(timeList, eMsdList, label = 'EMSD')
plt.plot(timeList, tMsdList, label = 'TMSD')
plt.legend()
plt.title('MSD, Levy Walk, alpha = 1')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time [s]')
plt.ylabel('MSD')
plt.show()
