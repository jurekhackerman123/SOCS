def SBM(T,alpha):

    # range for time is T, scale it by **alpha, so that we can show them in the same plot 
    timeRange = np.ceil(T**alpha)

    # scale time by ** 1/alpha
    t = np.arange(timeRange)**(1/alpha)              

    # create position array 
    x = np.random.randn(T)
    x = np.arange(x)

    positionList = x

    for i in range(1, len(t)):
        positionList[i] = positionList[i-1] + x[i]

    # x = np.cumsum(np.random.randn(int(np.ceil(T**alpha)))) 
    x, timeArray = Regularize(x,t,T)
    return(x)