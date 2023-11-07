import numpy as np 
import matplotlib.pyplot as plt 

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
    return(x)

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
    return(x,y)
