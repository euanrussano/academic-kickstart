---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Introduction to Probability - Conditional Probability and Bayes theorem"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning"]
categories: ["Basics of Machine Learning"]
date: 2020-07-25T19:26:20-03:00
lastmod: 2020-08-02T19:26:20-03:00
featured: false
draft: false

# Featured image

# To use, add an image named `featured.jpg/png` to your page's folder.

# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.

image:
 caption: ""
 focal_point: "Smart"
 preview_only: false

# Projects (optional).

# Associate this post with one or more of your projects.

# Simply enter your project's folder or file name without extension.

# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.

# Otherwise, set `projects = []`.

projects: []
---
## Overview

Machine Learning deals all the time with predicting a certain outcome, given a set of inputs, or features. The essence of this comes from conditional probability, which can be used to calculate the expectation of events which are dependent on other(s).

In this post, we will go over the essentials of conditional probability, its fundamental rules and the Bayes theorem.

## Conditional Probability

In real-world situations, events are rarely, if not never completely independent of others. In fact, most machine learning problems start from the premise that a certain outcome can be predicted based on the occurrence of other events. If $X$ and $Y$ are two events, $P(X|Y)$ indicates the probability of X given Y, that is, the probability of occurrence of X, given that Y has already taken place.

If $X$ and $Y$ are **independent**, then the probability of X is not affected by the occurrence of $Y$. Therefore, $P(X|Y) = P(X)$.

On the other hand, if $X$ and $Y$ are **disjoint** or mutually exclusive events, then one will not occur if the occur has already occurred. Thus, $P(X|Y) = 0$.

### Product Rule

This rule can be used to calculate the joint probability of X and Y, or the probability that **both** X and Y will take place. It can be stated as follows:

$$
P(X \cap Y) = P(X|Y)\cdot P(Y)
$$

Where:
- $P(Y)$ is the probability that Y happen.
- $P(X|Y)$ is the conditional probability of X w.r.t Y, thus the conditional probability of X.

This rule helps us to arrive to the following conclusions:
- If X is a subset of Y ($X \in Y$) then $P(X|Y)=\frac{P(X)}{P(Y)}$.
- If Y is a subset of X, then $P(X|Y) = 1$ .

### Chain Rule

The chain rule is a generalization of the product rule, which describes the joint probability of $n$ events $X_1, X_2, X_3,...X_n$. This joint probability can be calculated as:

$$
P(\Cap_{i=1,...,n} E_i) = P(E_n|\Cap_{i=1,...,n-1}E_i)\cdot P(\Cap_{i=1,....,n-1} E_i)
$$

## Bayes Theorem

The Bayes theorem, also called Bayes rule, consists in a combination of conditional probability with product and sum rules. It is stated as follows.

$$
p(Y|X) = \frac{P(X|Y)\cdot P(Y)}{P(X)}
$$

The sum rule is employed to calculate $P(X)$ as follows.

$$
P(X) = P(X \cap Y) + P(X \cap Y^c)
$$

## A Simple Exercise (adapted from [HackerEarth](https://www.hackerearth.com/pt-br/practice/machine-learning/prerequisites-of-machine-learning/bayes-rules-conditional-probability-chain-rule/tutorial/))

John will have an important event at work tomorrow and he can't be late for it. In regular days he goes to work by car and the probability that he will arrive on time, with no problems in the car, is $p_{ot}$. A problem in the car can show up with probability $p_{ct}$. In the case of a problem in the car, John needs to take a train and, out of $N$ trains, only $N_{ot}$ can take him to work on time. 

What are the chances that he arrives at work on time tomorrow?
Assume that:
$$
p_{ct} = 0.2
$$
$$
p_{ot} = 0.3
$$
$$
N = 10
$$
$$
N_{ot} = 2
$$

### Analytical Solution

Let's call: <br>
$X$ - reach work on time <br>
$Y$ - no car problem <br>

From the problem description, we have that $p_{ot}$ is the probability that he will arrive on time, given that he doesn't have car problems.
$$
p(X|Y) = p_{ot}
$$

Where $ct^c$ is the complementary of having car problems. In other words, the complementary probability of having car problems $p_{ct}$ is,
$$
p(Y^c)= p_{ct}
$$

From sum rule, we have that,
$$
p(X) = p(X \cap Y) + p(X \cap Y^c) \\
$$

Replacing each term according the product rule, we have,
$$
= p(X|Y)*p(Y) + p(X|Y^c)p(Y^c)
$$

$$
= p(X|Y)*(1-p(Y^c)) + \frac{N_{ot}}{N}p(Y)
$$

$$
= p(ot)*(1-p_{ct}) + \frac{N_{ot}}{N}p_{ct}
$$

Substituting the values we have:

$$
= 0.3*(1-0.2) + \frac{2}{10}0.2 = 0.28
$$

Therefore, there is 28% chance that John will arrive on time.

To illustrate, if he could take any $N$ train and still it would take him on time to work, the new final probability would be:

$$
= 0.3*(1-0.2) + \frac{10}{10}0.2 = 0.44
$$

Surely he would have much better chances of arriving on time.

### Solution in Python

We can try to estimate the probability found in the previous section, by doing an experiment in Python. This experiment consists on the following.
- Initialize the counter `ontime`, which indicates the number of times that John would arrive on time.
- Generate a random variable `car_problem`, uniformly distributed in [0,1] indicating if John had a car problem. If `car_problem < 0.2`, he had a car problem, otherwise he didn't.
- If he had a car problem, randomly generate a value `train` between 1 and $N$, indicating which train arrived. If `train` is 1 or 2, the right train arrived, and he will arrive on time. Sum 1 to `ontime`.
- If he didn't have a car problem, then generate a random variable `ontime_noproblem` which, if it is less then $p_{ot}$, sum 1 to `ontime`.
- Repeat the above steps $i$ times. At the end, calculate $Prob(X)$ as `ontime/i`

The following script performs the experiment described above, after the plot visualizes the convergence of the value obtained towards $Prob(X)$.

```python

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
```
{{< figure src="./experiment.png" title="Figure 1 - Experiment to estimate the probability of arriving on time." >}}

Notice here how the probability nicely approaches the theoretical values previously calculated (0.28).

## Summary

Through this post we went over the basics of **conditional probability** and **bayes theorem**.

**Conditional probability** is used to calculate the probability of an outcome X given that another event Y has already happened. The **product rule**  and **chain rule** can be used to obtain conditional probabilities from join ones.

**Bayes theorem** employs the concepts inherited from conditional probability, product rule and the sum rule to calculate the **conditional probability** of the outcome, given *a priori* knowledge of another event X.

## Further Reading

[Bayes' rules, Conditional probability, Chain rule - HackerEarth](https://www.hackerearth.com/pt-br/practice/machine-learning/prerequisites-of-machine-learning/bayes-rules-conditional-probability-chain-rule/tutorial/)

[Machine Learning - A Probabilistic Perspective](https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020)