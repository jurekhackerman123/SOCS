import numpy as np
import matplotlib.pyplot as plt 


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



def SBM_2D(T,alpha):
    import numpy as np
    from scipy.special import erfcinv
    t = np.arange(np.ceil(T**alpha))**(1/alpha)               # Take the power (alpha) of time
    x = np.cumsum(np.random.randn(int(np.ceil(T**alpha))))    # Regular Brownian motion
    y = np.cumsum(np.random.randn(int(np.ceil(T**alpha))))    # Regular Brownian motion
    x = regularize(x,t,T)
    y = regularize(y,t,T)
    return(x,y)


