import numpy as np 
import matplotlib.pyplot as plt 

import seaborn as sns


'''
Simulate Prisoners Dilemma for a number of rounds and calculate the accumulated years in prison
'''


# global Variables 
N = 7
# I defect, other cooperates
T = 0
# both cooperate
R = 0.9
# both defect 
P = 1  
# I cooperate, other defects  
S = 1.5


def PrisonersDilemma(numberOfRounds, n, m): 

    playerN = np.ones(numberOfRounds)
    playerM = np.ones(numberOfRounds)

    for round in range(numberOfRounds):


        if round > n or (np.isin(0, playerM[:round])).any():
            # print('test')
            playerN[round] = 0


        if round > m or (np.isin(0, playerN[:round])).any():
            # print('test')
            playerM[round] = 0


        # if round <= n and not np.isin(0, playerM[:round]):
        #     print('test')
        #     playerN[round] = 1 


        # if round <= m and not np.isin(0, playerN[:round]):
        #     print('test')
        #     playerM[round] = 1 

    
    # actions have been created, calculate years in prison
    yearsInPrisonN = 0 
    yearsInPrisonM = 0

    for round in range(numberOfRounds): 

        if playerN[round] == 0: 
            if playerM[round] == 0: 
                yearsInPrisonN += P
                yearsInPrisonM += P
            elif playerM[round] == 1: 
                yearsInPrisonN += T
                yearsInPrisonM += S
        
        elif playerN[round] == 1: 

            if playerM[round] == 0: 
                yearsInPrisonN += S
                yearsInPrisonM += T
            elif playerM[round] == 1: 
                yearsInPrisonN += R
                yearsInPrisonM += R




    return yearsInPrisonN, yearsInPrisonM





# TEST
# print(PrisonersDilemma(N, N, N)[0])
# print(PrisonersDilemma(N, N, 0)[0])
# print(PrisonersDilemma(N, 0, N)[0])
# print(PrisonersDilemma(N, 0, 0)[0])





# first plot

# fix m = 4
# listOfYears = []

# m = 4

# for i in range(10): 
#     yearsInPrisonN, forget = PrisonersDilemma(10, i, 4)
#     print(yearsInPrisonN)
#     listOfYears.append(yearsInPrisonN)

# x = np.arange(0, len(listOfYears))
# plt.scatter(x, listOfYears)
# plt.title('Years in prison for player two playing strategy m=' + str(m))
# plt.xlabel('n')
# plt.ylabel('Years in prison')
# plt.axvline(m, color='red', linestyle='--', label='m = ' + str(m))
# plt.legend()

# plt.show()









# create plot m vs n 
# NUMBEROFROUNDS = 10

# lattice = np.zeros((NUMBEROFROUNDS, NUMBEROFROUNDS))

# for i in range(NUMBEROFROUNDS): 
#     for j in range(NUMBEROFROUNDS): 

#         lattice[i, j], forget = PrisonersDilemma(NUMBEROFROUNDS, i, j)



# Plot heatmap

# ax = sns.heatmap(lattice, cmap='viridis', annot=True, fmt=".2f", cbar_kws={'label': 'Color Scale'})
# 
# Show the plot
# ax.invert_yaxis()
# plt.xlabel('m')
# plt.ylabel('n')
# plt.plot([1,2,3,4,5,6,7,8,9, 10], [0,1,2,3,4,5,6,7,8, 9], linestyle='--', color = 'black')
# plt.show()



