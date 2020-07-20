# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% imports

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22, 'figure.autolayout': True, 'figure.figsize': (15,5)})
factorial = np.math.factorial
SEED = 999

np.random.seed(SEED)
#%% Uniform distribution
'''
What is the probability of getting a 2 in a die roll?
'''

# Empty list to hold the ratio of 2s in each set of drawings
p = []

nr_trials = np.logspace(1,3,100)
for i in nr_trials:
    N = int(i) # number of drawings
    # generate N uniform random number between 1 and 6 (7 is exclusive)
    uniform_samples = np.random.randint(1, 7, size = N)
    # count the number of 2s we got
    count = np.sum(uniform_samples == 2)
    pval = count/N # ratio (tends to probability)
    p.append(pval)
    
    
fig1 = plt.figure()
plt.plot(nr_trials,p,'o-')
plt.plot(nr_trials,[1/6]*len(nr_trials),'--r')
plt.grid()
plt.xlim(nr_trials[0],nr_trials[-1])
plt.xlabel('Number of drawings')
plt.ylabel('p(X=2)')
plt.title(f'Theoretical p(X=2) = {1/6:.3f}')

#%% Bernoulli distribution
'''
Consider getting either a 1 or a 2 in a die roll as sucess, while any
other number as a failure. This can be modeled as Bernoulli distribution
with $theta$ as p(X=success) and $1-\theta$ as p(X=fail)
'''

# Theoreticallly we know that each number in the roll of a die comes
# from the uniform distribution so getting either 1 or 2 should be
# p(X=sucess) =p(X=1) + p(X=2), where $X \in {1,2,3,4,5,6}$

theoryBernoulli = 1/6 + 1/6
print(f'Theoretical probability = {theoryBernoulli :.3f}')

# create a list to hold the probabilities
p = []

nr_trials = np.logspace(1,3,100)
# Perform an experiment drawing uniform numbers and counting the amount of
# 1 or 2 and dividing the count by the number of drawings
for i in nr_trials :
    N = int(i)
    uniform_samples = np.random.randint(1, 7, size = N)
    count = np.isin(uniform_samples,[1,2])
    pval = sum(count)/N
    p.append(pval)
    

fig2 = plt.figure()
plt.plot(nr_trials,p,'o-')
plt.plot(nr_trials,[theoryBernoulli]*len(nr_trials),'--r')
plt.grid()
plt.xlim(nr_trials[0],nr_trials[-1])
plt.xlabel('Number of drawings')
plt.ylabel('p(X=success)')
plt.title(f'Theoretical p(X=sucess) = {theoryBernoulli:.3f}')
#%% Binomial distribution
'''
Say we toss a coin 3 times, what is the probability of getting a head
all of the times?
n = 3
k = 3
theta = 0.5
'''
n = 3
k = 3
theta = 0.5
# calculate p(k=3) by the analytic formula
theoryBinomial = factorial(n)/(factorial(n-k)*factorial(k))*theta**k*(1-theta)**(n-k)

# calculate p(k=3) using numpy for an experiment
numpylBinomial = sum(np.random.binomial(n,theta,int(2e5))==3)/int(2e5)

print(theoryBinomial)
print(numpylBinomial)

#%% save figures

fig1.savefig('uniform.png')
fig2.savefig('bernoulli.png')