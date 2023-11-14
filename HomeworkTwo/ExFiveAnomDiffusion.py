import numpy as np 
import matplotlib.pyplot as plt 

from ExerciseTwoAnomDiffusion import *


'''
levy walk 
'''


def LW(T,alpha):
    import numpy as np
    x = []
    t = []
    x.append(0)
    t.append(0)
    V = 1
    while t[-1]<T:
        dt = (1-np.random.rand())**(-1/(3-alpha))          # Flight time distribution
        t.append(t[-1] + dt)
        x.append(x[-1] + V*np.random.choice([-1,1])*dt)    # Particle moves either right or left during flight
    x = regularize(x,t,T)
    x = Normalize(x)
    return(x)


# alphaList = [1, 2]

# for alpha in alphaList: 
#     position = LW(200, alpha)
#     # position = Normalize(position)
#     plt.plot(position, label = 'alpha='+str(alpha))
#     plt.legend()
# plt.show()



def LW_2D(T,alpha):
    import numpy as np
    t = []
    x = []
    y = []
    x.append(0)
    y.append(0)
    t.append(0)
    V = 1
    while t[-1]<T:
        dt = (1-np.random.rand())**(-1/(3-alpha))          # Flight time distribution
        t.append(t[-1] + dt)
        theta = np.random.rand()*2*np.pi
        x.append(x[-1] + V*np.cos(theta)*dt)               # Particle moves randomly in 2D
        y.append(y[-1] + V*np.sin(theta)*dt)               # Particle moves randomly in 2D
    x = regularize(x,t,T)
    y = regularize(y,t,T)
    x = Normalize(x)
    y = Normalize(y)
    return(x,y)





# for alpha in alphaList: 
#     position2D = LW_2D(500, alpha)
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
numIterations = 1000

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

eMsdList = []
tMsdList = []

for time in timeList: 
    
    
    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = LW(time, 1.5)
        eMsd += (position[0] - position[-1])**2

    eMsdList.append(eMsd)


    # tmsd

    tMsd = 0
    positionTMsd = LW(10000, 1.5)

    for i in range(10000-time):
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
