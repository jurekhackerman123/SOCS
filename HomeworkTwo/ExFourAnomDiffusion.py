import numpy as np
import matplotlib.pyplot as plt


from ExerciseTwoAnomDiffusion import *


'''
continuous time random walk 
'''




def ContinuousTimeRandomWalk(T,alpha):
    times = [0]
    positions = [0]
    # while times[-1]<T:
    for iteration in range(0, 2*T, 2):

        if times[-1] >= T: 
            break

        times.append(times[iteration] + (random.random())**(-1/alpha)) 
        times.append(times[iteration + 1] + 1)     

        positions.append(positions[iteration])                                     
        positions.append(positions[iteration+1] + np.random.randn())   
      
    positions, timeArr = Regularize(positions,times,T)                               
    return positions





# alphaList = [0.5, 1]

# for alpha in alphaList: 
#     position = ContinuousTimeRandomWalk(200, alpha)
#     position = Normalize(position)
#     plt.plot(position, label = 'alpha='+str(alpha))
#     plt.legend()
# plt.title('1D Trajectory, Continuous Time Random Walk')
# plt.xlabel('Time [s]')
# plt.ylabel('x')
# plt.show()




def TwoDimensionalCTRW(T,alpha):
    times = [0]
    xPositions = [0]
    yPositions = [0]
    # while times[-1]<T:
    for iteration in range(0, 2*T, 2):

        if times[-1] >= T:
            break

        times.append(times[iteration] + (random.random())**(-1/alpha)) 
        times.append(times[iteration+1] + 1)   

        xPositions.append(xPositions[iteration])                                    
        xPositions.append(xPositions[iteration+1] + np.random.randn())  

        yPositions.append(yPositions[iteration])                                     
        yPositions.append(yPositions[iteration+1] + np.random.randn())    

    xPositions, timeArray = Regularize(xPositions,times,T)
    yPositions, timeArray = Regularize(yPositions,times,T)
    return xPositions, yPositions



# for alpha in alphaList: 
#     position2D = TwoDimensionalCTRW(500, alpha)
#     x2D = position2D[0]
#     y2D = position2D[1]

#     x2D = Normalize(x2D)
#     y2D = Normalize(y2D)

#     plt.plot(x2D, y2D, label = 'alpha=' + str(alpha))
# plt.title('2D Trajectory, Continuous Time Random Walk')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()





'''
Now, for the MSD
'''
numIterations = 1000

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

eMsdList = []
tMsdList = []

for time in timeList: 
    
    print(time)
    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = ContinuousTimeRandomWalk(time, 0.5)
        eMsd += (position[0] - position[-1])**2

    eMsdList.append(eMsd / numIterations)


    # tmsd

    tMsd = 0
    positionTMsd = ContinuousTimeRandomWalk(100000, 0.5)

    count = 0

    for i in range(100000-time):
        # print(i)
        tempDistance = (positionTMsd[i] - positionTMsd[i + time-1])**2

        tMsd += tempDistance

        count += 1

    tMsdList.append(tMsd / count )



plt.plot(timeList, eMsdList, label = 'EMSD')
plt.plot(timeList, tMsdList, label = 'TMSD')
plt.title('MSD for Continuous Time Random Walk, alpha = 0.5')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time [s]')
plt.ylabel('MSD [m]')

plt.show()
