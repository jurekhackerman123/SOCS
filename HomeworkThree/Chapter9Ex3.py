import numpy as np 
import matplotlib.pyplot as plt
from Chapter9Ex1 import *
from matplotlib.animation import FuncAnimation

from Chapter9Ex4 import *

import random 

def HardSphereCorrection(R, x1, y1, x2, y2): 
    '''
    x1, y1 are the coordinates of particle 1
    x2, y2 are the coordinates of particle 2

    returns new coordinates for particle i 
    '''


    # check if they overlap

    distance = np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

    if distance == 0:
        x1New = x1 + distance/2
        x2New = x2 + distance/2
        return x1New, y1, x2New, y2


    if distance >= 2*R: 
        return x1, y1, x2, y2
    
    print('Hard sphere Correction had to be applied at x1, y1 =', x1, y1, ' and x2, y2 =', x2, y2)

    difference = 2*R - distance

    # correct the positions 

    if x1 > x2: 
        x1New = x1 + ( abs(x1-x2) / distance ) * difference / 2
        x2New = x2 - ( abs(x2-x1) / distance ) * difference / 2
    else: 
        x1New = x1 - ( abs(x1-x2) / distance ) * difference / 2
        x2New = x2 + ( abs(x2-x1) / distance ) * difference / 2


    if y1 > y2: 
        y1New = y1 + ( abs(y1-y2) / distance ) * difference / 2
        y2New = y2 - ( abs(y2-y1) / distance ) * difference / 2
    else: 
        y1New = y1 - ( abs(y1-y2) / distance ) * difference / 2
        y2New = y2 + ( abs(y2-y1) / distance ) * difference / 2

    print(np.sqrt( (x1New - x2New)**2 + (y1New - y2New)**2 ))


    return x1New, y1New, x2New, y2New


# x1, y1, x2, y2 = HardSphereCorrection(5, 4, 0, 8, 0)


# plt.scatter([4, 8], [0, 0], label = 'before')
# plt.scatter([x1, x2], [y1, y2], label = 'after')
# plt.legend()
# plt.show()



'''
Do we have to put their initial positions randomly??

Is my approach correct??

How are we supposed to visualize this??? Animation??
'''


def CheckBoundaryConditions(x, y): 
    '''
    if we're not inside the allowed region, set the values to the boundary values 
    '''
    if x > XMAX: 
        x = XMAX
    elif x < XMIN: 
        x = XMIN
    if y > YMAX: 
        y = YMAX
    elif y < YMIN: 
        y = YMIN

    return x, y

def SimulateManyParticles(numberOfParticles, R, dT, DT, numSteps, DR, velocity, v0): 


    # create matrix for trajectories of all particles 
    xTrajectories = np.zeros((numberOfParticles, numSteps))
    yTrajectories = np.zeros((numberOfParticles, numSteps))

    phi           = np.zeros((numberOfParticles, numSteps))


    for particleNo in range(numberOfParticles):
    
        xTrajectories[particleNo, 0] = random.uniform(XMIN, XMAX)
        yTrajectories[particleNo, 0] = random.uniform(YMIN, YMAX)
        phi[particleNo, 0]           = random.random() * 2 * np.pi

        # create trajectory for this particle 
        for timeStep in range(1, numSteps): 

            # calculate phi
            phi[particleNo, timeStep]           = phi[particleNo, timeStep-1] + dT * np.sqrt(2* DR) * np.random.normal(0, 1)

            # calculate the x
            xTrajectories[particleNo, timeStep] = xTrajectories[particleNo, timeStep-1] + dT * (velocity * np.cos(phi[particleNo, timeStep]) + np.sqrt(2*DT) * np.random.normal(0, 1))

            # calculate the y
            yTrajectories[particleNo, timeStep] = yTrajectories[particleNo, timeStep-1] + dT * (velocity * np.sin(phi[particleNo, timeStep]) + np.sqrt(2*DT) * np.random.normal(0, 1))


            xTrajectories[particleNo, timeStep], yTrajectories[particleNo, timeStep] = CheckBoundaryConditions(xTrajectories[particleNo, timeStep], yTrajectories[particleNo, timeStep])

        
    # once the positions are updated, check the boundary conditions and hard sphere corrections 

    for particle in range(numberOfParticles): 

        # get current position of particles 
        xTrajectories[particle, -1]
        yTrajectories[particle, -1]

        for otherParticle in range(numberOfParticles): 
            if particle == otherParticle: 
                continue

            # get current positions of other particles 
            xOther = xTrajectories[otherParticle, -1]
            yOther = yTrajectories[otherParticle, -1]


            xTrajectories[particle, -1], yTrajectories[particle, -1], xTrajectories[otherParticle, -1], yTrajectories[otherParticle, -1] = HardSphereCorrection(R, x, y, xOther, yOther)


            # check boundary conditions again 
            xTrajectories[particle, -1], yTrajectories[particle, -1] = CheckBoundaryConditions(xTrajectories[particle, -1], yTrajectories[particle, -1])
            xTrajectories[otherParticle, -1], yTrajectories[otherParticle, -1] = CheckBoundaryConditions(xTrajectories[otherParticle, -1], yTrajectories[otherParticle, -1])


            # implement the velocities due tto phoretic interaction
            updatedVelocity = PhoreticInteraction(R, R, 5*R, xTrajectories[particle, -1], yTrajectories[particle, -1], xTrajectories[otherParticle, -1], yTrajectories[otherParticle, -1], v0)


            '''
            QUESTION: WHAT DO I THNE DO WITH THIS VELOCITY????
            '''


    return xTrajectories, yTrajectories
        

R = 1e-3
XMIN = -50e-3
XMAX = 50e-3
YMIN = -50e-3
YMAX = 50e-3
NUMBEROFPARTICLES = 10
DT = 1e-4
DR = 1
VELOCITY = 3e-3
NUMSTEPS = 1000

# for phoretic interaction
V0 = 20e-3


x, y = SimulateManyParticles(NUMBEROFPARTICLES, R, 0.01, DT, NUMSTEPS, DR, VELOCITY, V0) 



fig, ax = plt.subplots()

for i in range(NUMBEROFPARTICLES):
    ax.plot(x[i, :], y[i,:], label = 'particle '+ str(i))

# ax.plot(x[0, :], y[0,:], label = 'particle '+ str(3))

ax.legend()
plt.show()

# exit()




exit()
'''
Trying to animate this 
'''


# Step 2: Set up the figure and axis
# fig, ax = plt.subplots()
# # ax.set_xlim(0, 10)
# # ax.set_ylim(0, 10)

# # Step 3: Define the function to update the plot at each frame
# def update(frame):
#     ax.clear()  # Clear the previous frame

#     frame = int(frame)

#     # Step 4: Plot multiple trajectories (random for demonstration)
#     num_trajectories = 5
#     for particleNo in range(num_trajectories):
#         xCoord = x[particleNo, :frame]
#         yCoord = y[particleNo, :frame]
#         ax.plot(xCoord, yCoord, label=f'Trajectory {particleNo}')

#     # Customize plot appearance
#     # ax.set_xlim(0, 10)
#     # ax.set_ylim(0, 10)
#     # ax.legend()

# # Step 5: Use FuncAnimation to update the plot at each frame
# animation = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=50)

# # To display the animation, you can use plt.show()
# plt.show()



# exit()


def AnimateTrajectory(x, y): 


    xList = []
    yList = []

    x2List = []
    y2List = []


    for i in range(100): 
        plt.clear()

        xList.append(x[0, i])
        yList.append(y[0, i])

        # plt.scatter(xList, yList)
        plt.plot(xList, yList, label = 'particle 1')


        x2List.append(x[1, i])
        y2List.append(y[1, i])

        # plt.scatter(x2List, y2List)
        plt.plot(x2List, y2List, label = 'particle 2')


        plt.pause(0.05)

    plt.title('One particle trajectory')
    plt.legend()
    plt.show


AnimateTrajectory(x, y)
