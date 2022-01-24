---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Multinoulli and Multinomial Distributions with Examples in Python"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning"]
categories: ["Basics of Machine Learning"]
date: 2020-07-21T18:22:20-03:00
lastmod: 2020-07-21T18:22:20-03:00
featured: false
draft: false

# Featured image

# To use, add an image named `featured.jpg/png` to your page's folder.

# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.

image:
 caption: "Image by <a href='https://pixabay.com/users/Nachrichten_muc-25398/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=140340'>Nachrichten_muc</a> from <a href='https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=140340'>Pixabay</a>"
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

In the last post (see [here](../uni_bernoulli_binomial/)) I explained the following discrete distributions:
- Uniform
- Bernoulli
- Binomial

In this post, we continue on this same subject, but now on **Multinoulli** and **Multinomial** distributions. They generalize Bernoulli and Binomial, respectively, by enabling the random variables to have **categorial outcomes**, instead of binary ones. By categorial here, it means that instead of only having the possiblity of k=0 (failure, no, abscence, etc) or k=1 (success, yes, presence), it is possible to have multiple discrete values, such as $\\{0,1,2,3,4,5,6,...\\}$.

## Multinoulli Distribution

This distribution is also called **categorial distribution**, since it can be used to model events with K possible outcomes. Bernoulli distribution can be seen as  a specific case of Multinoulli, where the number of possible outcomes K is 2. 

In machine learning, the multinoullli can used to model the expected class of one sample into a set of K classes. For instance, one may want to predict to which specie $k$ in the set $K$ a flower belongs based on its attribute. Then species K follow a multinoulli distribution.

Consider the $p(x=k)$ the probability that the sample $x$ belongs to class k. Here $x$ could be the attributes of a flower in the example above, or one side of a die in the roll of it. If the set of classes is $K \in {1,2,3,4,...,K}$, then the probability of each outcome can be written as:

$p(x=1) = p_1$

$p(x=2) = p_2$

$p(x=3) = p_3$

...

$p(x=K) = p_K$

Naturally, the probabilities sum to 1.0 ($\sum_i^{K} p(x=i) = 1.0$).

Coming back to the example of flowers classification, say that for a sample $x$ the following probabilites where obtained for each of the 3 classes.

$p(x=1) = 0.1$

$p(x=2) = 0.3$

$p(x=3) = 0.6$

Clearly, $\sum_{i=1}^{3} p(x=i) = 1$ and one would say that the sample is most probable from class 3.

## Multinomial Distribution

The multinomial distribution describes repeated and independent Multinoulli trials. It is a generalization of he binomial distribution, where there may be K possible outcomes (instead of binary. 

As an example in machine learning and NLP (natural language processing), multinomial distribution models the counts of words in a document.

Similar to Multinoulli, we say that a sample x may take K possible outcomes, each one with prabability $p_K$, after n successive trials.

The probability (pmf) of a certain outcome can be modeled using the formula:

$$
p(X=k) = \frac{n!}{x_1!x_2!...x_k!}p_1^{x_1}\cdot p_2^{x_2}...p_k^{x_k}
$$

Where $n$ is the number of trials, $x_i$ is the number of times event $i$ occurs and $p_i$ is the probability of event $i$ at each independent trial.

As an example, consider a problem which can take 3 outcomes at each trial. The probability of obtaining one specific outcomes can be written as:

$$
p(X=k) = \frac{n!}{x_1!x_2!x_3!}p_1^{x_1}\cdot p_2^{x_2}\cdot p_3^{x_3}
$$

This can be used to model, for instance, the probability of one specific outcome on a chess tournment. Say that we want to determine what is the probability that, after 12 games, player 1 will have 7 wins, player 2 will have 2 wins and the remaining games will finish in draw. For that, suppose that the probability that Player 1 wins is 0.4, Player 2 is 0.35 and the tie has probability 0.25. Therefore we have,

|Variable|Value|
|---|---|
|n|12|
|x1|7|
|x2|2|
|x3|3|
|p1|0.4|
|p2|0.35|
|p3|0.25|

Replacing that in the formula shown above:

$$
p(X=k) = \frac{12!}{7!2!3!}0.4^{7}\cdot 0.35^{2}\cdot 0.25^{3} = 0.0248
$$

Therefore, the probability of this specific outcome in this chess tournment is approximately 2.5%.

## Python Example on Multinomial Distribution

Let's use Python to perform an experiment and simulate the example above, so that we can obtain the final probability, but without the use of Multinomial formula. This can be done using `numpy.random.multinomial(n, pvals, size=None)` function, where `n` is the number of trials, `pvals` is a list of the probabilities associated with each outcome in a trial, and `size` is the number of simulations to be done.

For the chess tournment we have `n=12` trials, `pvals = [0.4, 0.35 0.25]` as the vector (or list) or probabilities, and for `size` we may want to simulate different numbers here and visualize the convergence of the probability towards the "analytical" value.

```python
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
```

{{< figure src="./multinomial.png" title="Figure 1 - Experiment of Multinomial Distribution - Probability that player 1 wins 7 times, player 2 wins 2 times and there are 3 ties." >}}


## Summary

In this post you saw a bit of what is a **Multinoulli** or **Multinomial** distribution. It can be said that these distributions generalize the **Bernoulli** and **Binomial** distributions, making it possible to model random discrete variables with $K$ possible outcomes.

**Multinoulli** can be used to describe the outcome of one single random variable $x$, which may take $K$ outcomes.

On the other hand, **Multinomial** generalizes the multinoulli distribution, making it possible to model $n$ trials of random variable $x$, which can take $K$ outcomes.

As mentioned, these concepts have plenty applications in **Machine Learning**, specifically when discrete variables are employed such as in classification problems.

## Further reading

[Discrete Probability Distributions - Machine Learning Mastery](https://machinelearningmastery.com/discrete-probability-distributions-for-machine-learning/)

## API

[numpy.random.multinomial](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.multinomial.html)
