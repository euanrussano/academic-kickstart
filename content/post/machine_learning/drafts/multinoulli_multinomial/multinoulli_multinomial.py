'''
## Python Example

Consider 
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22, 'figure.autolayout': True, 'figure.figsize': (15,5)})
# set seed for reproductibility
np.random.seed(999) 

#%% Multinoulli example

n = 12                      # number of trials (games in one tourment)
pvals = [0.4, 0.35, 0.25]   # probabilities on a single trial
 

sizes =[] # number of tournments played
p = []    # a list to hold ratios (converge to prob) that player 1 wins 7 times, player 2 wins 2 times and 3 ties

for size in np.logspace(2,4):
    # the line below is where we actually generate discrete random variables according the multinomial distribution
    outcomes = np.random.multinomial(n, pvals, size=int(size))
    
    # let's count the ratio of the expected outcome over all the outcomes - this will lastly converge to the probability
    prob = sum((outcomes[:,0]==7)&(outcomes[:,1]==2)&(outcomes[:,2]==3))/len(outcomes)
    
    p.append(prob)
    sizes.append(int(size))

# Plotting
fig1 = plt.figure()
plt.plot(sizes,p,'o-')
plt.plot(sizes,[0.0248]*len(sizes),'--r')
plt.grid()
plt.xlim(xmin=0)
plt.xlabel('Number of Drawings')
plt.ylabel('p(X=K)')
plt.title('Theoretical p(X=K) = 0.0248')

#%% save figures

fig1.savefig('multinomial.png')