---
title: Tutorial":" Implement a Neural Network from Scratch with Python
date: 2019-08-21T01:00:00
lastmod: 2019-08-21T01:00:00
tags: ["Python", "Machine Learning", "Neural Network"]
categories: ["Machine Learning"]
draft: false

image:
 caption: "Neural Network"
 focal_point: "Smart"
 preview_only: false
---

In this tutorial, we will see how to write code to run a neural network model that can be used for regression or classification problems.
We will **NOT** use fancy libraries like Keras, Pytorch or Tensorflow. Instead the neural network will be implemented using only numpy for numerical computation and scipy for the training process.

<!-- more -->

The necessary libraries are:
- Numpy: for numerical computation;
- Scipy.optimize.minimize: to train the neural network;
- Scipy.stats.pearsonr: to test goodness of fit.

I will go over these libraries with a bit more detail later. First, import all the libraries mentioned above.


```python
import numpy as np
from scipy.optimize import minimize
from scipy.stats import pearsonr
```

The dataset used consists in a simple way, containing the following data, stored in *data.csv*:

| x_1 | x_2 | y   |
|---- | ----| --- |
| 1 | 0 | 1|
| 0 | 1 | 0|
| 1 | 1 | 0|
| 0 | 0 | 1|


```python
data = []
with open('data.csv','r') as f:
    f.readline()
    for line in f:
        line = [float(val) for val in line[:-1].split(',')]
        data.append(line)
data = np.array(data)
data
```



```
    array([[1., 0., 1.],
           [0., 1., 0.],
           [1., 1., 0.],
           [0., 0., 1.]])
```


Separate the columns, using the first two for the input `X`, while the last column is considered the output `y`.


```python
X = data[:,0:2]
y = data[:,2].reshape(-1,1)
print(X)
print(y)
```

```
    [[1. 0.]
	[0. 1.]
	 [1. 1.]
     [0. 0.]]
    [[1.]
     [0.]
     [0.]
     [1.]]
```  

## Structuring the Neural Network

The neural network consists in a mathematical model that mimics the human brain, through the concepts of connected nodes in a network, with a propagation of signal. Each neuron contains an activation function, which may vary depending on the problem and on the programmer. A very common function used due to its felixibility and capablity of generation is the sigmoid (or logistic) function, which can be written as:

$$
y = \frac{1}{1+e^{-w x}}
$$

Where $w$ are the weights (parameters) of the nerual network which should be optimized. The following function can be used in Python to define the sigmoid function.


```python
def sigmoid(w,x):
    # x - Nx2 input matrix
    # w - 2x1 parameter vector
    # output should be 4x1
    return 1/(1+np.exp(x.dot(w)))
```

The following cell is used to test the function above for correctnes fo the result. A dummy weight vector `w` is created for the purpose of this testing.


```python
# test sigmoid function
w = np.array([0.5,-0.5]).reshape(-1,1)
print(sigmoid(w,X))
```
```
    [[0.37754067]
     [0.62245933]
     [0.5       ]
     [0.5       ]]
```
    

We will implement the neural network using an Object-Oriented approach. This means we will write a class which will emulathe the model, and it will contain the functions to optimize its parameters and to test it, i.e perform predictions. Start by writing the class definition using the keyword `class` and the initialization function, contained in the `__init__()` function.


```python
class NeuralNetwork:
    def __init__(self,x,y,neurons):
        self.input = x
        self.obsOutput = y
        self.output = np.zeros((y.shape[0],1))
        self.inputWeights = np.random.rand(x.shape[1],neurons)
        self.outputWeights = np.random.rand(neurons,1)
```

The class `NeuralNetwork` contain the following properties, as specified above:
+ It stores the inputs in a property `input`
+ It stores the observed outputs (targets) in a property `y`
+ The shape of the targets is used to generate the output array, stored in `output` property. It is initialized with zeros.
+ The weights of the inputs are stored in `inputWeights`. It is initialized with random values, and its shape is properly configured using the input `x` array and the number of neurons `neurons`.
+ The weights of the hidden layer are stored in `outputWeights`. It is initialized with random values, and its shape is properly configured using the number of neurons `neurons`.

Let's test and see if the `NeuralNetwork` class is not throwing any errors up to this point.


```python
net = NeuralNetwork(X,y,2)
print(net.inputWeights)
print(net.outputWeights)
```

```
    [[0.90518084 0.71031147]
     [0.75555662 0.19589718]]
    [[0.00156605]
     [0.64047559]]
``` 

Notice that the values of weights, printed above, are simple generated randomly and do not hold any meaning up to this point.

We can obtain the output of the hidden layer by applying the `sigmoid` function to the input weights of the neural network and the input array, as shown below.


```python
# How to obtain the output of the hidden layer neurons
sigmoid(net.inputWeights,X)
```

```
    array([[0.287987  , 0.32953002],
           [0.31961175, 0.45118172],
           [0.15966303, 0.28777629],
           [0.5       , 0.5       ]])
```


To extend it, the output of the complete network is obtained by doing matrix multiplication of the `outputWeights` with the output of the hidden layer, shown above.


```python
# How to obtain the output of the output layer neuron (assuming linear)
sigmoid(net.inputWeights,X).dot(net.outputWeights)
```

```
    array([[0.21150694],
           [0.28947141],
           [0.18456373],
           [0.32102082]])
```


Let's make this code a bit more permanent, by writing a function `predict`, which we will use to generate the output of the neural network given an array of input. This function can be appended to the class `NeuralNetwork`, by using the `setattr` function of Python. Notice that this function work in the following way:

```python
'''
setattr(class_name,method_to_be_created,function_name)

class_name -> name of the class which the function will be appended to.
method_to_be_created -> a string defining the name of the method implemented in the class, so it can be called by
                        using class_name.method_name()
function_name -> a call to the function to be appended, in this case predict.
'''
```


```python
# Implementation of the prediction process of ANN
def predict(self,X):
    # hidden layer output HL
    self.HL =  sigmoid(self.inputWeights,X)
    # output layer (network output)
    self.OL = self.HL.dot(self.outputWeights)
    return self.OL

# give the method to the class Neural Network
setattr(NeuralNetwork,'predict',predict)
```

A very interesting fact is that, once the new method is appended to the class, every object previously created will already contain the method. We can test it by calling the `predict` method from the object `net` already created.


```python
net.predict(X)
```


```

    array([[0.21150694],
           [0.28947141],
           [0.18456373],
           [0.32102082]])
```


## Training the neural network

Here comes what I see as the most complex part to be implemented in the model, the training part. It consists in basic two main things:
+ cost function - a way of evaluating how good the model is with its current parameters;
+ optimization function - a way of reducing the cost by modifying the value of the parameters;

To avoid growing too much the complexity of this exercise, we will use the [`minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) from the package `scipy.optimize`. This function will take as arguments the cost function, which we will implement, and the parameters.

The issue here is that the `minimize` function is build to take the parameters to be optimized as a single vector. However, you saw that in the structure of our neural network we have the neural networ as matrices stored in two properties: `inputWeights` and `outputWeights`. So we need to join them to (using [`np.concatenate()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html)) and them reshape it to one row, using [`np.reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html).

Also, after the optimization we have to get the optimum parameters and reshape them again to place back in `inputWeights` and `outputWeights`.

Again, we define the function and append it to the class `NeuralNetwork` using the `setattr` function.


```python
def fit(self):
    x0 = np.concatenate([net.inputWeights,net.outputWeights.T]).reshape(-1,)
    res = minimize(self.cost,x0)
    
    self.inputWeights = res.x.reshape(3,-1)[:-1,:]
    self.outputWeights = res.x.reshape(3,-1)[-1,:].reshape(-1,1)
    return res

setattr(NeuralNetwork,'fit',fit)
```

To calculate the **cost**, we need to define a way to define a value that will tell us how good the model is. Intuitively, we can think in terms of the **errors**. If errors are high, then the cost should be high. On the other hand, a low cost should indicate a low error. So let's start defining what is an error.
*The error consists in the absolute difference between the expected value (target) and the predicted value.*
This difference can be mathematically expressed as:

$$
(y_{obs} - y_{pred})
$$

Where $y_{obs}$ is the observed value and expected result, while $y_{pred}$ is the output of the neural network, the predicted result. Suppose that we have the following observations $y_{obs}$:

$$
y_{obs} = [1,-1,-1]
$$

And the corresponding predictions are:

$$
y_{obs} = [1,1,-3]
$$

Obtaining the errors

$$
(y_{obs} - y_{pred}) = [(1-1),(-1-(1)),(-1-(-3))] = [0,-2,2]
$$

We obtain a vector with 3 errors, each one corresponding to a pair expected/predicted value. But the cost needs to be a single value. Again, intuitively, we could think of obtaining a single error value by summing up all the errors. Doing that for the vector above produces,

$$
0 + (-2) + 2 = 0
$$

The sum of errors is 0! This result make it looks like there is no error, though we already know that there is differences between prediction and target. This can be corrected by squaring each value and them summing it up.

$$
0^2 + (-2)^2 + 2^2 = 8
$$

If this method, we avoid error cancellation, because any value will become positive. This metric is called the sum of squared errors (SSE), and can be expressed generically as:

$$
J = \sum (y_{obs} - y_{pred})^2
$$

If we desire to obtain an average squared error instead of the sum, we can divide the SSE by the number of points, thus obtaining the mean of squared errors (MSE), expressed as:

$$
J = \frac{1}{n}\sum (y_{obs} - y_{pred})^2
$$

For this exercise let's use the SSE as our cost. We define a function to calcualte that and append it to the class, as it was done with previous methods.


```python
def cost(self,x):
    self.inputWeights = x.reshape(3,-1)[:-1,:]
    self.outputWeights = x.reshape(3,-1)[-1,:].reshape(-1,1)
    
    ypred = self.predict(self.input)
    
    J = np.sum((self.obsOutput - ypred)**2)
    
    return J

setattr(NeuralNetwork,'cost',cost)
```

Test the cost by calling it once (remember to concatenate and reshape the weights so it works properly!)


```python
net.cost(np.concatenate([net.inputWeights,net.outputWeights.T]))
```



```
    1.2005915066240083
```


Now we can call the fit() method on the neural network to find the optimum parameters that will show the minimum error of the predictions and observations. This is done in the following code. Notice that the output shown is the result from the minimize function on scipy.optimize.


```python
net.fit()
```


```

          fun: 2.255136144862212e-09
     hess_inv: array([[ 4.14164529e+03,  7.06430001e+03,  1.78716005e+05,
             2.61958344e+05, -2.18298665e+04,  2.18235283e+04],
           [ 7.06430001e+03,  1.20546383e+04,  3.04875328e+05,
             4.46879826e+05, -3.72395856e+04,  3.72291055e+04],
           [ 1.78716005e+05,  3.04875328e+05,  7.71449754e+06,
             1.13077626e+07, -9.42327432e+05,  9.42039179e+05],
           [ 2.61958344e+05,  4.46879826e+05,  1.13077626e+07,
             1.65747049e+07, -1.38124557e+06,  1.38082329e+06],
           [-2.18298665e+04, -3.72395856e+04, -9.42327432e+05,
            -1.38124557e+06,  1.15106690e+05, -1.15070568e+05],
           [ 2.18235283e+04,  3.72291055e+04,  9.42039179e+05,
             1.38082329e+06, -1.15070568e+05,  1.15035689e+05]])
          jac: array([-2.44188025e-08, -3.92603844e-06, -5.85603566e-10, -3.89227306e-09,
            2.09829900e-06,  3.32048000e-06])
      message: 'Optimization terminated successfully.'
         nfev: 264
          nit: 32
         njev: 33
       status: 0
      success: True
            x: array([ 6.56030353e-01, -4.35259814e-03,  7.77890879e+00,  1.11330054e+01,
            1.36193289e-02,  1.98637937e+00])
```


To finish the exercise, let's generate a vector of predictions using the optimum parameters and compare it with the observations. We test how good this prediction is by using the pearson coefficient, also from scipy package.

Pearson coefficient (also known as R-squared) is a value that ranges from 0-1, where 1 is a perfect prediction (all the predictions match the targets), while 0 means that the predictions are as good as using the average target as a predictor (a quite poor model). Therefore our objective is to obtain a pearson coefficient as near to 1 as possible.

The pearsonr() function also returns a value which is the p-value. I will not enter into details about this statistical parameter here, but what is important to mention is that it should be as low as possible, ideally less than 0.05 or 0.01, so we can statistically accept the predictions.


```python
ypred = net.predict(X)
```


```python
pearsonr(y,ypred)
```



```
    (array([1.]), array([7.01427805e-12]))
```

<a href="./code/neuralNetworkScratch.ipynb" download>
  📥 Download the Jupyter notebook here
</a>

<a href="./code/neuralNetworkScratch.py" download>
  📥 Download the Python code here
</a>


See you next post!