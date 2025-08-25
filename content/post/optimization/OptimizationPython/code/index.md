---
title: Using Python for Process Optimization
summary: "In this post I will show how to use Python to solve optimization problems."
authors: []
date: 2018-08-04T12:00:00
lastmod: 2018-08-04T12:00:00
tags: ["Python", "Process Optimization", "Numpy", "Scipy"]
categories: ["Optimization"]
featured: false
draft: false

image:
 caption: "Process Optimization"
 focal_point: "Smart"
 preview_only: false
---


![Python logo](./img/python-logo.png)

Hello!

In the last post I demonstrated how to use MS Excel software and its Solver tool to find the optimal operating point in a process.

In this post, we will use the free **Python** programming language to solve the same problem. The use of **Python** in the academic and industrial environment has grown immensely, mainly due to the continuous development of new tools that increase its potential of application in several areas.

<!-- more -->

For this optimization problem, the Numpy and Scipy libraries are used, which contain functions that make Python very similar to Matlab and Scilab for problem solving in engineering, mathematics, physics, and many other areas.

I'm not going to present a Python tutorial in this post, just the same application for the same problem solution that was presented in the last post I made.

Recalling, the problem is to maximize profit in the solvent extraction process by manipulating some system variables. The definition of the process can be found [here]({{< relref "post/optimization/OptimizationExcel/index.md" >}}), under Example 1.2. This problem can be divided into two parts:

- the equation to be maximized (profit)

- system constraints (mass balances, energy, equilibria, and all conservative equations)

First we will import the necessary libraries and define the system variables:


```python
import numpy as np
import scipy.optimize

# Problem variables
F = 1.0*10**4    # kg-water / h
x0 = 0.02       # kg-solute / kg-water
s = 7.0*10**-4   # kg-solvent / kg-water
m = 4.0         # kg-water / kg solvent
Ps = 0.4        # USD / kg-solute
Px = 0.01       # USD / kg-solvent.
```

 The equation to be maximized can be defined in a function, here called "problem" (we use the problem variables as global variables):


```python
def problem(x):

    W1 = x[0] # mass flow rate
    W2 = x[1] # mass flow rate
    W_1 = x[2] # mass flow rate
    W_2 = x[3] # mass flow rate
    x1 = x[4]  # liquid molar composition
    y1 = x[5]  # gas molar composition
    x2 = x[6]  # liquid molar composition
    y2 = x[7]  # gas molar composition

    # Income
    R = Ps*(W_1*y1+W_2*y2)
    
    # Cost
    C = Px*(W1+W2)
    
    # Profit (negative for minimization)
    L = -(R-C)
    
    return L
```

This function has as input the manipulated variables of the problem, and the output and the variable L, which constitutes profit. In this case we establish the profit as negative because by default a minimization will be done. For this is worth the relation:

max x = -min x

Finally, we define constraints of the problem in a function called here cons:


```python
def cons(x):

    W1 = x[0]
    W2 = x[1]
    W_1 = x[2]
    W_2 = x[3]
    x1 = x[4]
    y1 = x[5]
    x2 = x[6]
    y2 = x[7]

    cons = np.zeros(6)

    # Solute mass balance
    cons[0] = F*x0-W_1*y1-F*x1
    cons[1] = F*x1-W_2*y2-F*x2

    # Solvent mass balance
    cons[2] = W1-W_1-s*F
    cons[3] = W2+s*F-W_2-s*F

    # Equilibrium relations
    cons[4] = y1-m*x1
    cons[5] = y2-m*x2

    return cons
```

Again, the function has as input the manipulated system variables, and as output the cons variable, which has six values, all must be zero. This is determined by creating the following dictionary in Python:

```python
cons = [{'type': 'eq', 'fun': constraints}]
```


Now, just set the initial value of the manipulated variables (like zero for all) and call the "Solver" function in the scipy.optimize.minimize function as follows:


```python
xi = np.zeros(8)
x = scipy.optimize.minimize(problem, xi, constraints={'type':'eq','fun':cons})


print('Optimization Result \n')
print('W1 = {:.3f}'.format(x.x[0]))
print('W2 = {:.3f}'.format(x.x[1]))
print('W_1 = {:.3f}'.format(x.x[2]))
print('W_2 = {:.3f}'.format(x.x[3]))
print('x1 = {:.3f}'.format(x.x[4]))
print('y1 = {:.3f}'.format(x.x[5]))
print('x2 = {:.3f}'.format(x.x[6]))
print('y2 = {:.3f}'.format(x.x[7]))
```
```
Out[]:
    Optimization Result 
    
    W1 = 1190.455
    W2 = 1184.538
    W_1 = 1183.455
    W_2 = 1184.538
    x1 = 0.014
    y1 = 0.054
    x2 = 0.009
    y2 = 0.037
```

You can compare these values with those obtained in Excel and you will see that they are very similar, if not the same. The same principle applied here can be used for the most diverse optimization problems.

Download the Jupyter notebook <a href="./code/20180804optimizationPython.ipynb" download>here</a>

Download the Python code<a href="./code/20180804optimizationPython.py" download>here</a>

Until the next post!
