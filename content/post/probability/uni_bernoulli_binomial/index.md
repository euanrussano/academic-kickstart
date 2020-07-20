---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Uniform, Bernoulli and Binomial Distributions with Examples in Python"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning", "Python"]
categories: ["Basics of Machine Learning"]
date: 2020-07-11T18:22:20-03:00
lastmod: 2020-07-11T18:22:20-03:00
featured: false
draft: false

# Featured image

# To use, add an image named `featured.jpg/png` to your page's folder.

# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.

image:
 caption: "Image from author"
 focal_point: "Smart"
 preview_only: true

# Projects (optional).

# Associate this post with one or more of your projects.

# Simply enter your project's folder or file name without extension.

# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.

# Otherwise, set `projects = []`.

projects: []
---
Hello! in this post you will learn about some common discrete distributions. Distribution can be related with the "behavior", of a variable, what is the probability associated with a certain event $E$ under a certain distribution $F$. For example, the roll of a die follows a Uniform distribution, since the chances that you get any number after a roll are the same (in the case of a die, $1/6$). Similarly, a fair coin has the same probability of landing on head or tail (50-50), so that's also uniform.

Coming back to the example of the die, instead of looking at the probability of get any value, what is the probability that I will get a 6, agains the probability of NOT getting a 6? In this case, we have $p(x|X=6) = 1/6$ but $p(x|X \neq 6)= 1 - 1/6 = 5/6$, and then the same problem is interpreted as a Binomial distribution.

Enough of introduction, let's get into the distributions. Here I will talk about Uniform, Bernoulli and Binomial. In another post I will talk about some other common discrete distributions.

## Uniform distribution

As already mentioned, when a random variable $X$ follows a uniform distribution ($X = \text{Uniform}(N)$), then any event $E$ will have the same probability. In this case, such probability $p(X)$ can be obtained by dividing 1 by the number of possible events $N$.

$$
p(X) = \frac{1}{N}
$$

In the experiment below, Python is used to simulate from 10 to 10'000 rolls of a die, and estimate the probability of getting one value, say 2. Through this experiment, one can see how the experimental probability approaches the theoretical one.

```python
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

```
{{< figure src="./uniform.png" title="Figure 1 - Experiment of Uniform Distribution - Probability of getting a 2 in the roll of a die." >}}

## Bernoulli distribution

Named after Jacob Bernoulli, these distributions can model cases where the event X can take a binary outcome, interpreted as 0 (no/ fail/ absence) or 1 (yes/ success/ presence). Examples of such are:

- Coin toss - $X \in \\{Head, Tail\\}$

- Gender of person - $X \in \\{ Male, Female\\}$

- Patient diagnosis - $X \in \\{ Sick, Healthy\\}$

- Exam result - $X \in \\{ Failure, Success\\}$

When the outcome of an experiment follows a Bernoulli distribution, it is called a *Bernoulli trial*.

A value p is attributed to the probability of an outcome equals to 1. Complementary, the probability of not having the outcome is 1-p. In summary:

$$
Ber(x|p)=\begin{cases} p & \text{if } x=1 \\\\
                     1-p & \text{if } x=0
          \end{cases}
$$

To examplify, consider that in a game you win if you roll a die and get 1 or a 2, and you lose for whatever other number. What is the probability of winning? We can simulate that with Python and confirm the formula above.

```python
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
```

{{< figure src="./bernoulli.png" title="Figure 1 - Experiment of Bernoulli Distribution - Probability of getting 1 or 2 in the roll of a die." >}}

## Binomial distribution

The binomial distribution is a generalization of the binomial one. It can be used to model a problem with $n$ events, with $k$ sucesses. For example, if I roll a die 10 times and let $X=k$ be the number of times we get a 2, where $X \in {0,1,...,n}$. In this case, $X$ has **binomial** distribution, which can be written as $X \~ \text{Bin}(n,\theta)$ where $theta$ is the probability of the sucess in one event.

The probability mass function can be written as:

$$
\text{Bin}(n,\theta) = C_k \theta^k (1-\theta)^{n-k}
$$

Where,

$$
C_k = \binom{n}{k} = \frac{n!}{(n-k)!k!}
$$

$C_k$ is also called the **binomial coefficient**, and the term $\binom{n}{k}$ reads "n choose k". The mean and variance of this distribution are:

$$
\text{mean}=\theta
$$

$$
\text{Var}=n\theta(1-\theta)
$$

In the following example, Python is used to simulate the problem of tossing a coin 3 times, and determining the probability of getting a head exactly 3 times (That means, every toss would land head). The Binomial variables $n$, $k$ and $\theta$ for this case are:

The number of events $n = 3$

The number of successes (head) $k = 3$

The probability of getting head in a single coin toss $\theta = 0.5$

In the code, the formula above is used to calculate the theoretical probability, while an experiment is performed using random number to estimate this probability.

```python
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
```
```
Out[]:
0.125
0.124735
```

## Summary

Through this post we went over three common discrete variable distributions:
- Uniform;
- Bernoulli
- Binomial

**Uniform distribution** is used to model events which has the **same probability** of occuring, such as coin toss, roll of a die, etc.

**Bernoulli distribution** describes events which have a binary outcome, i.e gives **sucess or failure** with a probability $\theta$.

**Binomail distribution** is a generalization of the Bernoulli, which model binary outcomes with multiple events, such as multiple rolls of a die or multiple coin toss.

## Further Reading

The following literature provides information to dive deeper into this topic.

[Machine Learning - A Probabilistic Perspective](https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020)

[Discrete Random Variables - Hacker Earth](https://www.hackerearth.com/en-us/practice/machine-learning/prerequisites-of-machine-learning/discrete-random-variables/tutorial/)

[Binomial distribution - Wikipedia](https://en.wikipedia.org/wiki/Binomial_distribution)

[Discrete probability for Machine Learning - Machine Learning Mastery](https://machinelearningmastery.com/discrete-probability-distributions-for-machine-learning/)