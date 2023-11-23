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
    
    # print('Hard sphere Correction had to be applied at x1, y1 =', x1, y1, ' and x2, y2 =', x2, y2)

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

    # print(np.sqrt( (x1New - x2New)**2 + (y1New - y2New)**2 ))


    return x1New, y1New, x2New, y2New


x1, y1, x2, y2 = HardSphereCorrection(5, 4, 3, 8, 0)


plt.scatter([4, 8], [3, 0], label = 'before')
plt.scatter([x1, x2], [y1, y2], label = 'after')

plt.title('Demonstration of hard sphere correction, R = 5')

theta = np.linspace( 0 , 2 * np.pi , 150 )
 
 
a = 5 * np.cos( theta ) + 6
b = 5 * np.sin( theta ) + 1.5
 
plt.plot(a, b, color = 'black', label = 'Radius of Particle')

plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()

exit()



'''
Do we have to put their initial positions randomly??

Is my approach correct??

How are we supposed to visualize this??? Animation??
'''


def CheckBoundaryConditions(x, y): 
    '''
    if we're not inside the allowed region, set the values to the boundary values 
    '''
    if x >= XMAX: 
        x = XMIN
    elif x <= XMIN: 
        x = XMAX
    if y >= YMAX: 
        y = YMIN
    elif y <= YMIN: 
        y = YMAX

    return x, y




def SimulateManyParticles(numberOfParticles, R, dT, DT, numSteps, DR, velocity, v0): 


    # create matrix for trajectories of all particles 
    xTrajectories = np.zeros((numberOfParticles, numSteps))
    yTrajectories = np.zeros((numberOfParticles, numSteps))

    phi           = np.zeros((numberOfParticles, numSteps))

    # x and y component of velocity, but only!!! added velo due to pherotic interaction
    velocityArray = np.zeros((numberOfParticles, 2))

    # initialize random positions for particles 
    for particle in range(numberOfParticles):
    
        xTrajectories[particle, 0] = random.uniform(XMIN, XMAX)
        yTrajectories[particle, 0] = random.uniform(YMIN, YMAX)
        phi[particle, 0]           = random.random() * 2 * np.pi



    for timeStep in range(1, numSteps): 

        # FIRST: UPDATE THE POSITIONS OF ALL THE PARTICLES IN THIS PARTICULAR TIMESTEP!
        for particle in range(numberOfParticles):

            # calculate phi
            phi[particle, timeStep]           = phi[particle, timeStep-1] + dT * np.sqrt(2* DR) * np.random.normal(0, 1)

            # calculate the x
            xTrajectories[particle, timeStep] = xTrajectories[particle, timeStep-1] + dT * (velocity * np.cos(phi[particle, timeStep])) + dT * velocityArray[particle, 0] + np.sqrt(2*DT) * np.random.normal(0, 1)

            # calculate the y
            yTrajectories[particle, timeStep] = yTrajectories[particle, timeStep-1] + dT * (velocity * np.sin(phi[particle, timeStep])) + dT * velocityArray[particle, 1] + np.sqrt(2*DT) * np.random.normal(0, 1)

            velocityArray[particle, :] = 0
            # xTrajectories[particle, timeStep], yTrajectories[particle, timeStep] = CheckBoundaryConditions(xTrajectories[particle, timeStep], yTrajectories[particle, timeStep])

        
        # after we updated the positions for all particles at this timestep, we can check if some of these particles have to undergo corrections

        # set the phoretic velocities to zero again 
        # velocityArray = np.zeros((numberOfParticles, 2))


        # iterate over particles once more 
        for particle in range(numberOfParticles):

            for otherParticle in range(numberOfParticles): 
                
                # for the same particle, we do not have to do this
                if particle >= otherParticle: 
                    continue


                # hard sphere correction 
                xTrajectories[particle, timeStep], yTrajectories[particle, timeStep], xTrajectories[otherParticle, timeStep], yTrajectories[otherParticle, timeStep] = HardSphereCorrection(R, xTrajectories[particle, timeStep], yTrajectories[particle, timeStep], xTrajectories[otherParticle, timeStep], yTrajectories[otherParticle, timeStep])



                # check boundary conditions again 
                xTrajectories[particle,timeStep], yTrajectories[particle,timeStep] = CheckBoundaryConditions(xTrajectories[particle,timeStep], yTrajectories[particle,timeStep])
                xTrajectories[otherParticle,timeStep], yTrajectories[otherParticle,timeStep] = CheckBoundaryConditions(xTrajectories[otherParticle,timeStep], yTrajectories[otherParticle,timeStep])


                # PHORETIC INTERACTION 
                vX, vY = PhoreticInteraction(R, 5*R, xTrajectories[particle,timeStep], yTrajectories[particle,timeStep], xTrajectories[otherParticle,timeStep], yTrajectories[otherParticle,timeStep], v0)


                # now, when it comes to updating the velocities, we have to look at the coordinates 
                # right left velocity direction
                if xTrajectories[particle,timeStep] >= xTrajectories[otherParticle,timeStep]:
                    
                    velocityArray[particle, 0] -= vX
                    velocityArray[otherParticle, 0] += vX

                else: 
                    velocityArray[particle, 0] += vX
                    velocityArray[otherParticle, 0] -= vX

                # up down velocity direction
                if yTrajectories[particle,timeStep] >= yTrajectories[otherParticle,timeStep]: 
                
                    velocityArray[particle, 1] -= vY            
                    velocityArray[otherParticle, 1] += vY

                else: 
                    velocityArray[particle, 1] += vY            
                    velocityArray[otherParticle, 1] -= vY



    return xTrajectories, yTrajectories
        

R = 1e-3
XMIN = -50e-3
XMAX = 50e-3
YMIN = -50e-3
YMAX = 50e-3
NUMBEROFPARTICLES = 400
DT = 1e-7
DR = 1
VELOCITY = 3e-6
NUMSTEPS = 1000

# for phoretic interaction
V0 = 5000e-3


x, y = SimulateManyParticles(NUMBEROFPARTICLES, R, 0.001, DT, NUMSTEPS, DR, VELOCITY, V0) 



fig, ax = plt.subplots()

for i in range(NUMBEROFPARTICLES):
    ax.scatter(x[i, -1], y[i,-1], s = 20)

# # plot 1 particle trajectory 
# ax.plot(x[0, -100:-1], y[0,-100:-1])

# # ax.plot(x[0, :], y[0,:], label = 'particle '+ str(3))

# # ax.legend()
plt.title('Interaction where v0 =' + str(V0 * 10) + ' μm') 
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()

# exit()




# exit()
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
#     for particle in range(num_trajectories):
#         xCoord = x[particle, :frame]
#         yCoord = y[particle, :frame]
#         ax.plot(xCoord, yCoord, label=f'Trajectory {particle}')

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


    for i in range(NUMSTEPS): 
        # plt.clear()

        xList.append(x[0, i])
        yList.append(y[0, i])

        # plt.scatter(xList, yList)
        plt.plot(xList, yList)


        plt.pause(0.005)

    plt.title('One particle trajectory')
    plt.legend()
    plt.show


# AnimateTrajectory(x, y)
