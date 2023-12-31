import numpy as np
import matplotlib.pyplot as plt 
import random
'''
Finite difference method: 



'''

# these values work for No. 1 
DR = 0.5
DT = 0.2e-3
VELOCITY = 1e-3
dT = 0.01


def ActiveBrownianParticle(dT, numSteps, DT, DR, velocity): 

    xPosition   = np.zeros(numSteps)
    yPosition   = np.zeros(numSteps)

    phi         = np.zeros(numSteps)

    phi[0] = random.uniform(0, 2*np.pi)

    for iteration in range(1, numSteps): 

        # define phi first
        phi[iteration] = phi[iteration-1] + dT * np.sqrt(2* DR) * np.random.normal(0, 1)

        xPosition[iteration] = xPosition[iteration-1] + dT * (velocity * np.cos(phi[iteration]) + np.sqrt(2*DT) * np.random.normal(0, 1))

        yPosition[iteration] = yPosition[iteration-1] + dT * (velocity * np.sin(phi[iteration]) + np.sqrt(2*DT) * np.random.normal(0, 1))

        
    # print(phi)
    # print(np.random.normal(0,1))

    return xPosition, yPosition, phi


# Show on particle 2d trajectory 

x, y, phi = ActiveBrownianParticle(dT, 500, DT, DR, VELOCITY)

# plt.plot(x, y)
# plt.scatter(x[0], y[0], label = 'beginning', color='orange')
# plt.xlabel('x [m]')
# plt.ylabel('y [m]')
# plt.legend()
# plt.title('Active Brownian Particle')
# plt.show()

# exit()



def EMSD(numSteps, numIterations, dR, velocity):

    eMsd = 0

    for iteration in range(numIterations): 

        x, y, phi = ActiveBrownianParticle(dT, numSteps, DT, dR, velocity)

        tempDistance = ( x[0] - x[-1] )**2 + ( y[0] - y[-1] )**2 

        eMsd += tempDistance

    eMsd = eMsd / numIterations

    return eMsd



def TMSD(numSteps, displacementFactor, dR, velocity):

    x, y, phi = ActiveBrownianParticle(dT, numSteps, DT, dR, velocity)

    trajectoryLenght = len(x)

    displacementFactor -= 1

    tMSD = 0

    count = 0

    for i in range(trajectoryLenght - displacementFactor):


        tempDistance = (x[i] - x[i + displacementFactor])**2 + (y[i] - y[i + displacementFactor])**2

        tMSD += tempDistance

        count += 1

    tMSD = tMSD / count

    return tMSD   



def PlotMSDs():
    stepsList = [1,5,10,50,100,500,1000,5000]#,10000]

    # tMsdList = []
    # eMsdList = []

    velocityList = [0, 1e-3, 3e-3]

    for velocity in velocityList:

        eMsdList = []
        tMsdList = []

        for time in stepsList: 

            tempEMsd = EMSD(time, 1000, DR, velocity)

            tempTMsd = TMSD(10000, time, DR, velocity)


            eMsdList.append(tempEMsd)

            tMsdList.append(tempTMsd)
        

        plt.plot(stepsList, eMsdList)
        plt.scatter(stepsList, tMsdList, label = 'v = ' + str(velocity))


    plt.title('MSD for Active Brownian Particle')

    plt.xlabel('t [s]')
    plt.ylabel('MSD [m]')

    plt.legend()

    plt.xscale('log')
    plt.yscale('log')

    plt.show()

PlotMSDs()