# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:55:07 2020

@author: eruss
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22, 'figure.autolayout': True, 'figure.figsize': (15,5)})
np.random.seed(999)

ontime = 0

prob = []
nr_points = []
for i in range(1, int(1e6)):
    car_problem = np.random.random() 

    # Will he have a car problem?
    if car_problem < 0.2:
        # if he has  a car problem, will he still arrive on time?
        train = np.random.choice(np.arange(1,11))
        if train <= 2:
            ontime += 1
    else: # no car problem
        ontime_noproblem = np.random.random()
        if ontime_noproblem < 0.3:
            ontime += 1
    
    if i%10 == 0:
        nr_points.append(i)
        prob.append(ontime/(i))
    
#plt.plot(prob)
plt.semilogx(nr_points, prob)
plt.ylim([0,0.3])
plt.grid(True, which='both')
plt.xlabel('# of Drawings')
plt.ylabel('P(X)')
plt.savefig('experiment.png')


