import numpy as np 
import matplotlib.pyplot as plt 
import random

'''
finished
'''


def SimulateStateOneParticle(numberOfSteps, eB, stopWhenRightStateReached): 
    '''

    eB is given in units kB * T 

    '''
    z = 2 + np.exp(-eB)

    dictionary = {
        'left' : np.exp(-eB) / z,
        'middle' : 1 / z , 
        'right' : np.exp(-eB) / z
    }

    # initial condition
    particleState = 'left'

    # histogram
    dataToPlot = [0]

    for iStep in range(numberOfSteps): 

        # print('current particle state: ', particleState)

        randomNumber = random.random()

        if particleState == 'left':
            if randomNumber < dictionary['left']:
                particleState = 'middle'
                dataToPlot.append(1)
            else: 
                dataToPlot.append(0)

        elif particleState == 'middle': 
            if randomNumber < dictionary['middle']: 

                randomNumberLeftRight = random.random()

                if randomNumberLeftRight < 0.5: 
                    particleState = 'right'
                    dataToPlot.append(2)
                else: 
                    particleState = 'left'
                    dataToPlot.append(0)
            else: 
                dataToPlot.append(1)


        elif particleState == 'right':
            if randomNumber < dictionary['right']:
                particleState = 'middle'
                dataToPlot.append(1)
            else: 
                dataToPlot.append(2)

        if particleState == 'right' and stopWhenRightStateReached:
            print('number of iterations: ', iStep) 
            return iStep


    # check if equilibrium reached 
    countLeft = dataToPlot.count(0)
    countRight = dataToPlot.count(2)

    print(abs(countLeft - countRight))

    if abs(countLeft - countRight) < numberOfSteps/100: 
        print('equilibrium reached!')
    else: 
        print('equilibrium not reached.')

    if not stopWhenRightStateReached: 
        # plotting
        plt.hist(dataToPlot, bins=5, edgecolor='black')  # 'bins' is the number of bins or bars in the histogram
        # plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Kramer Transitions, ' + str(numberOfSteps) + ' steps' + ', energy: ' + str(eB) + 'kB * T')
        plt.xlim(0,2)
        x_labels = ['left', 'middle', 'right']
        plt.xticks(range(0, 3), x_labels)
        plt.show()



# SimulateStateOneParticle(10000, 2, False)
# exit()

'''
vary Eb
'''



def VaryEB(upperLimit):
    '''
    aranges a list between 0 and upperlimit in units of kB * T
    '''
    # eBList = np.arange(0,upperLimit)
    eBList = [0,5,10]
    for value in eBList: 
        SimulateStateOneParticle(100000, value, False)


# VaryEB(10)
# exit()

def CheckTransitionSteps(numberTransitionSteps): 

    avg = 0

    for iStep in range(numberTransitionSteps): 


        tempNumberOfSteps = SimulateStateOneParticle(1000, 2, True)

        avg += tempNumberOfSteps
    
    avgStoppingSteps = avg/numberTransitionSteps

    return avgStoppingSteps

avgStoppingSteps = CheckTransitionSteps(100)

print(avgStoppingSteps)

