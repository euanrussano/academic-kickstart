---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Introduction to Probability - Discrete Random Variables"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning"]
categories: ["Basics of Machine Learning"]
date: 2020-07-11T18:22:20-03:00
lastmod: 2020-07-11T18:22:20-03:00
featured: false
draft: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Image from author"
  focal_point: "Smart"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

## Introduction

Hello! In this post we will go over the concept of discrete random variables in the context of Probability Theory. How is this concept relevant for fields such as Machine Learning and Artificial Intelligence? Actually understanding it is vital for Machine Learning, since it provides some insight on the **distribution** of discrete variables, such as categorical ones. These distributions can be translated to more or less the behavior of a variable, so it can be statistically estimated.

When we say discrete or continuous random variables, we are actually talking about the outcome $E$ of a random experiment. The set of outcomes can be discrete variables, such as rolls of a die ($E \in \{ 1,2,3,4,5,6\}$), or continuous, such as hours of study per day for an exam ($0 \leq E \leq 24$). Let's dive deeper on each concept!

Remember that the expression $p(X)$ shows the probability of event $X$ be true (occur). This event may be of any nature, such as "get a 2 on a roll of die", or "will it rain on Sunday?". By definition, $0 \leq p(X) \leq 1$, where $p(X) = 0$ means that the event will not happen, while $p(X) = 1$ means that the event will certainly occur. $p()$ is called a probability mass function or *pmf*.

The negative of $p(X)$ is written as $p\bar{(X)}$, i.e the probability that the event $X$ will NOT occur. By definition, as already shown in a previous post, the negative complements the value of $p(X)$. In other words,

$$
1=p(X)+p \bar{(X)}
$$

Which can be rewritten as,

$$
p\bar{(X)} = 1-p(X)
$$

Therefore, if an event X has probability $0.3$ or $33\%$ of occurring, it may not occur with $67\%$ probability.

## Discrete random variables

As a discrete variable, X is an event from a finite or countably finite set $\chi$. For instance, consider the set of possible outcomes in the roll of a die:

$$
\chi = \{ 1,2,3,4,5,6\}
$$

In this case there are 6 possible, **discrete** outcomes. Obtaining one outcome from the set $\chi$

means 1 out of 6, or $1/6 \approx 0.167$. Since each value is equally possible, the probability mass function for any value is $p(X)=0.167$. Notice that this satisfies the properties $0 \leq p(X) \leq 1$, as well as $\sum_{x \in \chi}p(X)=1$.

As an example, the Figure below illustrates the distribution of a single roll of die. Since all the probabilities $p(X)$ hold the same value, this is called an uniform distribution.



![discrete.png](C:\Users\eruss\Documents\website\academic-kickstart\content\post\probability\drafts\discrete_dist\discrete\discrete.png)

Figure 1 - The distribution of single roll of die, a discrete random set. All the discrete events in $\chi$ have the same $p(X)=1/6$, so this is a uniform distribution.

### Example:

A school competition involves a 5 boys and 5 girls. From those, a set of three was chosen to one activity, without knowing their gender. Let $X$ be the event where the number of selected girls are 3. What is the event set? What are the possible event sets? If one would randomly make a set of 3 students, what's the probability that this set would be formed by 3 girls?

**Solution:**

Consider that the boys are represented by letter $B$, such that the 5 boys are:

$$
B_1,B_2,B_3,B_4,B_5
$$

Similarly, the five girls, each represented by $G$ are:

$$
G_1,G_2,G_3,G_4,G_5
$$

If there are 3 selected girls:

$E=\{G_i,G_j,G_k\}$, where $i,j,k$ may take any value in the range [1.5] without replacement.. By combination theory, we have that the number of possible sets containing 3 girls, where it doesn't matter their order and there is no replacement is,

$$
C=\frac{n!}{(n-r)!r!}
$$

Where $n$ is the total number of individuals being considered, and $r$ is the size of the set. In the case above, $n=5$ girls and $r=3$ girls in a group

$$
C=\frac{5!}{(5-3)!3!}=10
$$

The possible event sets are:

$E=\{B_1,B_2,B_3\}$

$E=\{B_1,B_2,G_1\}$

$E=\{B_1,G_2,G_1\}$

$E=\{G_3,G_2,G_1\}$

And similar events with the combinations of all the boys and girls. The total number of possibilities can be calculated, as above, using combination theory,

$$
C=\frac{10!}{(10-3)!3!}=120
$$

Therefore, there are 120 different ways of combining the 5 boys and 5 girls.

Since the total number of events in $\chi$ is 120, and out of that there are 10 events in which there are 3 girls, the probability $p(X=3)$, where $X$ represents the number of girls in a group is:

$$
p(X=3)=\frac{10}{120}=1/12\approx 8.33\%
$$

For the sake of comparison, let's calculate the probability of picking a set containing 2 girls (and consequently 1 boy) out of the 120 possibilities. For that, first we obtain the total number of possible combinations of the 5 girls in sets with 2 girls.

$$
C=\frac{5!}{(5-2)!2!}=10
$$

Now, each set can be combined with one of the 5 boys, thus the total number of combination is $10*5=5$. Therefore, the probability is,

$$
p(X=2)=\frac{50}{120}=5/12\approx 42.00\%
$$

Calculating the value of $p(X)$ for the other possible events (e.g 1 girl per group or no girl per group), we obtain the following table, showing the probability distribution of the groups of students according the number of girls per group.

| X   | p(X) |
| --- | ---- |
| 0   | 1/12 |
| 1   | 5/12 |
| 2   | 5/12 |
| 3   | 1/12 |

The figure below illustrates this case, clearly revealing that this distribution differs from the uniform one, were all possible events have the same "chance" of occurring.



![student.png](C:\Users\eruss\Documents\website\academic-kickstart\content\post\probability\drafts\discrete_dist\student\student.png)

In the next post we will see some most common discrete distributions.

## Summary

A **discrete random variable** $X$ is a value draw from a finite, countable set $\chi$. This value is obtained from the set with a probability $p(X)$, which may be equal for any $X \in \chi$ (uniform distribution) or it may differ according the specific distribution function.

Discrete random variables are used in Machine Learning to describe discrete variables, such as **categorical** ones, or **integer** variables. Examples of such are:

- The numbers of bathrooms in a house;

- Weather condition (sunny, rainy, snowy, etc )

- Cancer diagnosis (Malignant, Benign)

## Further Reading

[Machine Learning - A Probabilistic Perspective](https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020)

[Definition of Discrete Random Variables - Hacker Earth](https://www.hackerearth.com/pt-br/practice/machine-learning/prerequisites-of-machine-learning/discrete-random-variables/tutorial/)

[Discrete Random Variables - Brilliant Wiki]([Discrete Random Variables - Definition | Brilliant Math &amp; Science Wiki](https://brilliant.org/wiki/discrete-random-variables-definition/))
