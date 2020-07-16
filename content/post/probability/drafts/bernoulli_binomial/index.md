---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Introduction to Probability - Discrete Random Distributions - Bernoulli and Binomial Distributions"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning"]
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
 preview_only: false

# Projects (optional).

# Associate this post with one or more of your projects.

# Simply enter your project's folder or file name without extension.

# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.

# Otherwise, set `projects = []`.

projects: []
---

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

Consider the experiment of flipping a fair coin and landing a head. In this case, p=0.5, since there is 50% chance of getting a head and 1-p=0.5 or 50% of not getting a head (tail).

## Binomial distribution

## Summary

## Further Reading