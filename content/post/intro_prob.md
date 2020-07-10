---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Introduction to Probability Theory"
subtitle: ""
summary: ""
authors: []
tags: ["Probability", "Machine Learning"]
categories: ["Basics of Machine Learning"]
date: 2020-07-10T15:13:34-03:00
lastmod: 2020-07-10T15:13:34-03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

# Overview

It can be said that probability is one of the foundations of **machine learning**, together with linear algebra and calculus. In this post I would like to provide a basic description of what probability means in an intuitive sense, followed by some essential concepts in probability theory.

Probability is all about dealing with events which are not certain, they may happen or they may not happen. In some situations it is linked to terms such as luck, chance or risk. However, as a field of mathematics, probability is not a magical or obscure concept. On the contrary, it provides hte necessary tools to measure uncertainty of events and to investigate them based on reasoning.

# A simple example: Coin toss

Let's start this explanation with a simple example. Consider that you toss a coin. When the coin lands, will it show head or tails? Well we can not know for sure. What we know from the coin is that the number of possible events $E$ are 2: either we get tails or we get head. Here we bring in the assumption that there is no other event possible, like the coin will not land vertically, not facing any side. Another assumption we may take in such case is that both head or tails may be equally likely, that means the weight of the coin is homogenous so it does not favor a particular side.

When one toss the coin, what happens is 1 event, out of 2 possible events. Say that one toss the same coin 10 times, so out of $2 \cdot 10=20$ possible events, each time one gets $1*10=10$ event. So the probability (chance) that one gets a head, when he could get a head or tails equally likely, is $1/2 = 0.5$ or $50\%$. That's the probability of getting a head (or tails) when tossing a coin. We can also think that as, for every 100 throws, one will get *likely* 50 heads (or tails).

# Probability of an event

From the example described above, we can see that probability $P(X)$ for equally likely events can be stated as the number of times a certain event $X$ happens (where $X$ could be to get head in coin toss), divided by the total number of possible events. This will always be a value in the range between 0 and 1. If the event is impossible, then $P(X) = 0$. If the event is certain then $P(X) = 1$.

$$
P(X=x) = \frac{E}{S}
$$

Where $E$ is the collection of event(s) and $S$ is the number of all possible events.

As another example, consider the roll of a fair die. What is the probability that we get a 2? To find that we can write down the event $E$ space and the total events $S$ space.

$$
E = \{2\}
$$

$$
S = \{1,2,3,4,5,6\}
$$

Therefore, the value 2 is one event out of 6 possible events (including). Applying that in the calculation of $P(X=2)$ we get,

$$
P(X=2) = \frac{1}{6}=0.166
$$

The same probability (0.166 or 16.6%) applies to obtaining any other number from the roll of a fair die, since any number consists in 1 event out of 6. 

As you may have already noted, probability is often expressed as a fraction, a value between 0 and 1 or a percentage (between 0% or 100%).

The probability of an event **not** happening is called the *complement of the probability* and is stated as 1 minus its probability. For example, the probability of not obtaining a value of 2 in the roll of die is:

$$
P(X \neq 2) = 1 - P(X = 2) = 1 - 0.166 = 0.834
$$

In certain cases, the probability of an event is expressed in terms of the odds or chance of the event. Though it refers to the same idea, the way it is expressed differs a bit. Odds are expressed a ratio between wins (occurence) to losses (non-ocurrence). In that case, the odds or likelihood of obtaining a value of 2 in the roll of a die can be written as 1:5 for 1 win and 5 losses.

# Frequentist View x Bayesian View

To introduce the concept of probability in this article we have viewed it from a **Frequentist approach**. In this, probability is an indication of frequency of events after multiple runs. As an example, if a coin is tossed multiple times, it is expected to land tails about half of the time.

A different but less intuitive view of probability comes from the **Bayesian view**. In this, probability is understood as a measure of the uncertainty about an event, thus being related with information instead of repeated trials. Viewing from this standpoint, a coin will likely land heads or tails after a toss.

Bayesian view is more subjetive, relying sometimes in information obtained previously but also on certain assumptions and beliefs over a probability space. Still, is shows a clear advantage over the frequentist approach, since one can assign probabilities to very rare events that may not have been observed before, something which can not be done using frequentist approach.

# Summary

**Probability** is a mathematical concept used to quantify and measure uncertainy. It provides the formal rules tools to  determine the likelihood of an event based on the certain propositions.

An **event $E$** consists in the occurence which a probability is obtained. It is contained in a **sample space $S$**, which also hold all the possible events of the same problem. To obtain the probability of an event means to calculate its **probability function $P$**, a value which is in the range 0 to 1.

Though in this article we talked mostly about equally likely events, that's not always the case. In face, this is just one specific case among all possible **probability functions**. But we will see more about that

# Further reading

The following literature provides informatio dive deeper into this topic.

[Machine Learning - A Probabilistic Perspective](https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020)

Alex Smola and S.V.N. Vishwanathan (2008) Introduction to Machine Learning. Cambridge University Press

[Uncertainty - Wikipedia](https://en.wikipedia.org/wiki/Uncertainty)

[Probability - Wikipedia](https://en.wikipedia.org/wiki/Probability)

[Probability theory - Wikipedia](https://en.wikipedia.org/wiki/Probability_theory)