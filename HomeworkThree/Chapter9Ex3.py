import numpy as np 
import matplotlib.pyplot as plt


def HardSphereCorrection(R, x1, y1, x2, y2): 
    '''
    x1, y1 are the coordinates of particle 1
    x2, y2 are the coordinates of particle 2

    returns new coordinates for particle i 
    '''


    # check if they overlap

    distance = np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

    if distance >= 2*R: 
        print('No correction has to be made.')
        return x1, y1, x2, y2
    
    difference = 2*R - distance

    # factor = (x1 - x2) / (y1 - y2)


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
    print(2*R)


    return x1New, y1New, x2New, y2New


x1, y1, x2, y2 = HardSphereCorrection(5, 4, 0, 8, 0)


plt.scatter([4, 8], [0, 0], label = 'before')
plt.scatter([x1, x2], [y1, y2], label = 'after')
plt.legend()
plt.show()



'''
Do we have to put their initial positions randomly??

Is my approach correct??

How are we supposed to visualize this??? Animation??
'''

def CheckBoundaryConditions(x, y, xMin, xMax, yMin, yMax): 
    '''
    if we're not inside the allowed region, set the values to the boundary values 
    '''
    if x > xMax: 
        x = xMax
    elif x < xMin: 
        x = xMin
    if y > yMax: 
        y = yMax
    elif y < yMin: 
        y = yMin

    return x, y

def SimulateManyParticles(numberOfParticles, totalTime, R): 


    # create matrix for trajectories of all particles 
    xTrajectories = np.zeros((numberOfParticles, totalTime))
    yTrajectories = np.zeros((numberOfParticles, totalTime))

    phi           = np.zeros((numberOfParticles, totalTime))

    for timeStep in range(1, totalTime): 

        # create trajectory for this particle 
        for particleNo in range(numberOfParticles):

            # calculate phi
            phi[particleNo, timeStep]           = phi[particleNo, timeStep-1] 

            # calculate the x
            x = xTrajectories[particleNo, timeStep-1]

            # calculate the y
            y = yTrajectories[particleNo, timeStep-1]


            x, y = CheckBoundaryConditions(x, y)

            xTrajectories[particleNo, timeStep] = x
        
            yTrajectories[particleNo, timeStep] = y

        
        # TWO FOR LOOPS????? not good 

        for particle in range(numberOfParticles): 
            x = xTrajectories[particle, timeStep]
            y = yTrajectories[particle, timeStep]

            for otherParticle in range(numberOfParticles): 
                if particle == otherParticle: 
                    continue

                xOther = xTrajectories[particle, timeStep]
                yOther = yTrajectories[particle, timeStep]


                x, y, xOther, yOther = HardSphereCorrection(R, x, y, xOther, yOther)

            # here, one can check the boundary conditions again!! I don't know if necessary 

        



        

