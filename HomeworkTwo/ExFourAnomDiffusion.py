import numpy as np
import matplotlib.pyplot as plt

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


