from Chapter9Ex3 import *


def PhoreticInteraction(R1, R2, rCutoff, x1, y1, x2, y2, v0): 

    # calculate distance between particles
    distance = np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

    if distance >= rCutoff: 
        # velocity is zero then 
        return 0

    # calculate the respective velocities, assume that radii do not differ
    vParticle1 = v0 * R1**2 / distance**2
    # vParticle2 = v0 * R2**2 / distance**2

    return vParticle1








    
