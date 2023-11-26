# from Chapter9Ex3 import *
import numpy as np



def PhoreticInteraction(R1, rCutoff, x1, y1, x2, y2, v0): 

    # calculate distance between particles
    distance = np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

    if distance >= rCutoff: 
        # velocity is zero then 
        return 0, 0

    if distance == 0: 
        # print('distance is zero.')
        return 0, 0

    v0 = v0 * 100
    fraction = distance/R1

    # print('fraction:', 1/fraction**2, 'v0: ', v0)
    # print('and: ', v0 * (1/fraction)**2)

    # calculate the respective velocities, assume that radii do not differ
    vParticle = v0 * (1/fraction)**2
    
    # vParticle2 = v0 * R2**2 / distance**2

    # calculate angle between vectors 
    phi = (x1 * x2 + y1 * y2) / (np.sqrt(x1**2 + y1**2) * np.sqrt(x2**2 + y2**2))

    vX = vParticle * np.cos(phi)
    vY = vParticle * np.sin(phi)

    # print('PHORETIC INTERACION HAPPENED. velocities: ', vX, vY)
    # print('and vParticle ', vParticle)
    # print('and phi: ', phi)
    # print('and test: ', fraction)

    return vX, vY







    
