import numpy as np
import matplotlib.pyplot as plt 

from ExerciseTwoAnomDiffusion import *

'''
scaled brownian motion 
'''


def SBM(T,alpha):
    import numpy as np
    from scipy.special import erfcinv
    t = np.arange(np.ceil(T**alpha))**(1/alpha)               # Take the power (alpha) of time
    x = np.cumsum(np.random.randn(int(np.ceil(T**alpha))))    # Regular Brownian motion
    x = regularize(x,t,T)
    return(x)

alphaList = [0.5, 1, 2]


# plot

# for alpha in alphaList: 
#     position = SBM(200, alpha)
#     position = Normalize(position)
#     plt.plot(position, label = 'alpha='+str(alpha))
#     plt.legend()
# plt.show()


def SBM_2D(T,alpha):
    import numpy as np
    from scipy.special import erfcinv
    t = np.arange(np.ceil(T**alpha))**(1/alpha)               # Take the power (alpha) of time
    x = np.cumsum(np.random.randn(int(np.ceil(T**alpha))))    # Regular Brownian motion
    y = np.cumsum(np.random.randn(int(np.ceil(T**alpha))))    # Regular Brownian motion
    x = regularize(x,t,T)
    y = regularize(y,t,T)
    return(x,y)




# plot

# for alpha in alphaList: 
#     position2D = SBM_2D(500, alpha)
#     x2D = position2D[0]
#     y2D = position2D[1]

#     x2D = Normalize(x2D)
#     y2D = Normalize(y2D)

#     plt.plot(x2D, y2D, label = 'alpha=' + str(alpha))
# plt.legend()
# plt.show()


'''
Now, for the MSD calculation

HIER NOCHMAL!!!!!

'''

numIterations = 100

timeList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

eMsdList = []
tMsdList = []

for time in timeList: 
    
    
    # calculate msd for every timestep
    eMsd = 0
    for iIteration in range(numIterations): 
        position = SBM(time, 1.5)
        eMsd += (position[0] - position[-1])**2

    eMsdList.append(eMsd)


    # tmsd

    tMsd = 0
    positionTMsd = SBM(1000, 1.5)

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





