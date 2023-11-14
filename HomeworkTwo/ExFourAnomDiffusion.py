import numpy as np
import matplotlib.pyplot as plt


from ExerciseTwoAnomDiffusion import *


'''
continuous time random walk 
'''


def CTRW(T,alpha):
    import numpy as np
    t = []
    x = []
    x.append(0)
    t.append(0)
    while t[-1]<T:
        t.append(t[-1] + (1-np.random.rand())**(-1/alpha))  # Power-law distributed wait times 
        t.append(t[-1] + 1)                                 # The time step after the wait time 
        x.append(x[-1])                                     # Particle stays still during the wait time 
        x.append(x[-1] + np.random.randn())                 # Particle moves after the wait time 
    x = regularize(x,t,T)                                   # Regularize the traejctory
    return(x)


# alphaList = [0.5, 1]

# for alpha in alphaList: 
#     position = CTRW(200, alpha)
#     position = Normalize(position)
#     plt.plot(position, label = 'alpha='+str(alpha))
#     plt.legend()
# plt.show()




def CTRW_2D(T,alpha):
    import numpy as np
    t = []
    x = []
    y = []
    x.append(0)
    y.append(0)
    t.append(0)
    while t[-1]<T:
        t.append(t[-1] + (1-np.random.rand())**(-1/alpha))  # Power-law distributed wait times 
        t.append(t[-1] + 1)                                 # The time step after the wait time 
        x.append(x[-1])                                     # Particle stays still during the wait time 
        x.append(x[-1] + np.random.randn())                 # Particle moves after the wait time 
        y.append(x[-1])                                     # Particle stays still during the wait time 
        y.append(x[-1] + np.random.randn())                 # Particle moves after the wait time 
    x = regularize(x,t,T)
    y = regularize(y,t,T)
    return(x,y)



# for alpha in alphaList: 
#     position2D = CTRW_2D(500, alpha)
#     x2D = position2D[0]
#     y2D = position2D[1]

#     x2D = Normalize(x2D)
#     y2D = Normalize(y2D)

#     plt.plot(x2D, y2D, label = 'alpha=' + str(alpha))
# plt.legend()
# plt.show()



'''
Now, for the MSD
'''
numIterations = 100

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

eMsdList = []
tMsdList = []

for time in timeList: 
    
    
    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = CTRW(time, 1.5)
        eMsd += (position[0] - position[-1])**2

    eMsdList.append(eMsd)


    # tmsd

    tMsd = 0
    positionTMsd = CTRW(1000, 1.5)

    for i in range(1000-time):
        # print(i)
        tempDistance = (positionTMsd[i] - positionTMsd[i + time-1])**2

        tMsd += tempDistance

    tMsdList.append(tMsd)



plt.plot(timeList, eMsdList, label = 'EMSD')
plt.plot(timeList, tMsdList, label = 'TMSD')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.show()
