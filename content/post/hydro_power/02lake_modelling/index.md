---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Modelling, Simulation and Control of Hydro-Power System - Part 2"
subtitle: "Theoretical model of the lakes"
summary: "In this series I will show the entire process of developing a model, performing simulations and the use of different control techniques for decision support in flood management systems."
authors: []
tags: ["Flood Forecasting", "Model Predictive Control"]
categories: ["Flood Management"]
date: 2021-02-10T10:01:00
lastmod: 2021-02-19T10:01:00
featured: false
draft: false

# Featured image

# To use, add an image named `featured.jpg/png` to your page's folder.

# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.

image:
 caption: "Image by <a href='https://pixabay.com/users/russmac-756431/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=929406'>Russ McElroy</a> from <a href='https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=929406'>Pixabay</a>"
 focal_point: "Smart"
 preview_only: false

# Projects (optional).

# Associate this post with one or more of your projects.

# Simply enter your project's folder or file name without extension.

# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.

# Otherwise, set `projects = []`.

projects: ["Modelling, Simulation and Control of Hydro-power system"]
---

## Overview

In the previous post of this series (see [here](/post/hydro_power/01system_description)), I showed an overview of the system we intend to model and investigate. In this post I will show how to develop a simple yet effective mathematical representation of the series of lakes in the hydro-power system.

The main use of these lakes is to work as a battery, i.e energy storage. At times when energy is at low demand, water can be pumped from the river to the lakes and stored there as potential energy. When there is a greater demand and only the level of water from the river can not provide enough energy, water can flow from the lakes to the river through turbines, using its kinetic energy to generate extra energy. Notice that this process is, in a real-world case, not 100% efficient. This means that more energy is needed to pump the water from the river to the lakes, then can be extracted by turbining from the lakes to the river. Yet, it can be a useful technique to keep the balance in energy generation, and also to redirect volume of water when its excess can cause floods downstream.

Without further delay, let's start the modeling process.

## Mathematical representation of the lakes

The water stored in the lake changes according the inflow and outflow rates. As the volume of water decreases, the level also decreases. In essence the mass conservation is the basic equation to describe the lakes:

$$
\frac{dm}{dt} = w_{in}(t) - w_{out}(t)
$$

Where $m$ is the mass of water (kg), $t$ is the time (s), $w_{in}$ is the mass inflow rate (kg/s) and $w_{in}$ is the mass outflow rate (kg/s). The above equation can be rewritten as:

$$
\frac{d(\rho hA)}{dt} = \rho q_{in}(t) - \rho q_{out}(t)
$$

Where $\rho$ is the density of water, $h$ is the water level and $A$ is the cross-section area of the lake. Since any liquid can be reasonably considered incompressible (no change of volume with pressure), the density $\rho$ can be considered constant, and thus cancelled out. The cross-section area $A$ may be constant (like a cube) or it may be a function of the water level. For better generalization. let's say $A = A(h)$, thus the final equation is:

$$
\frac{d(h A(h))}{dt} = q_{in}(t) - q_{out}(t)
$$

The above equation is an ordinary differential equation, relating the rate of change of volume ($h A(h)$) with the inlet and outlet flow rates. It can be solved using numerical integration, if all the other variables ($q_i$) are known

## Power generated/consumed by pumps and turbines

The power $p$ generated/consumed by pumps and turbines is directly proportional to the flow rate $q$ and the difference in water height $H$ upstream and downstream. The following equations describe this relation in a simple form:
$$
H = h_{up} - h_{down}
$$

$$
p = K \cdot q \cdot H
$$

Where $K$ is constant of proportionality, which can be referred as the pump/turbine coefficient (positive for turbines and negative for pumps).

## Pipes and valves

The connection between lake 1 and 2 is made through a valve. The discharge through this element can in general be modelled by a non-linear relationship with the difference in height upstream and downstream $H$ as:

$$
q = -\text{sign}(H)\cdot A \cdot \sqrt{2g|H|}
$$

Where $A$ is the duct section.

## Analytical solution of lake storage with sinusoidal inflow and constant outflow (pump)

It is always useful to have some analytical solution of ODE problems to compare how good are numerical solutions obtained in a later step. Coming back to the mass conservation:

$$
\frac{d(h A(h))}{dt} = q_{in}(t) - q_{out}(t)
$$

Let's consider a very simple lake in the form of a cube. Thus, the cross section area is constant.

$$
A \neq A(t)
$$

The equation simplifies to:

$$
\frac{dh}{dt} = \frac{q_{in}(t) - q_{out}(t)}{A}
$$

Say the outlet is regulated by a pump, with a constant flow rate of $q_{out}$, and the inflow is a sinusoidal flow with the shape, provided by a pump.

$$
q_{in}(t) = A_{q} + B_{q}\sin\frac{\pi t}{C_{q}}
$$

$$
\frac{dh}{dt} = \frac{1}{A} \left[ A_{q} + B_{q}\sin\frac{\pi t}{C_{q}} - q_{out} \right]
$$

Call $A^{*} = A_{q}- q_{out}$

$$
\frac{dh}{dt} = \frac{1}{A} \left[ A^{*} + B_{q}\sin\frac{\pi t}{C_{q}} \right]
$$

Integrate it.

$$
\int dh = \frac{1}{A} \int \left(A^{*} + B_{q}\sin \left( \frac{\pi t}{C_{q}} \right)\right) dt
$$

$$
h = \frac{A^{*}t}{A} - \frac{B_{q} C}{A\pi} \cos \left( \frac{\pi t}{C_{q}} \right) + \text{Const}
$$

Which gives us the general solution to this problem. Now let's fix some numerical values for simulation.

+ $A = 1$

+ $q_{out} = 5$
+ $A_q = 5$
+ $B_q = 2$
+ $C_q=1$

$$
h = - \frac{2}{\pi} \cos \left( \pi t \right) + \text{Const}
$$

Apply initial condition $t = 0$, $h_0 = 0$

$$
\text{Const} = \frac{2}{\pi}
$$

The final analytical solution is,

$$
h = - \frac{2}{\pi} \cos \left( \pi t \right) + \frac{2}{\pi}
$$

The equation above is used to calculate the water level profile of the lake for any time $t \geq 0$, as shown in the Figure below.

{{< figure src="./analytical1/analytical1.png" title="Figure 1 - Water level profile for first case." >}}




### Another analytical solution, with variable cross-section

Let's perform a similar analysis, as the one shown above, but now using a lake which has a variable cross-section area. Say that the cross-section area follows the pattern below:

$$
A(h) = E h^2
$$

Where $E$ is a constant value. Let's perform the same analytic integration process that was done above.

$$
\frac{(E h^2)dh}{dt} = \frac{1}{A} \left[ A^{*} + B_q\sin\frac{\pi t}{C_q} \right]
$$

Integrate it.

$$
\int (E h^2)dh = \frac{1}{A} \int \left(A^{*} + B_q\sin \left( \frac{\pi t}{C_q} \right)\right) dt
$$

$$
h = \left[ \frac{3}{AE}A^{*}t - \frac{3}{AE}\frac{B_q C_q}{\pi} \cos \left( \frac{\pi t}{C_q} \right) + \text{Const} \right]^{\frac{1}{3}}
$$

Which gives us the general solution to this problem. Now let's fix some numerical values for simulation.
+ $A = 1$
+ $q_{out} = 5$
+ $A_q = 5$
+ $B_q = 2$
+ $C_q=1$
+ $E=1$

$$
h = \left[ \frac{3}{E}A^{*}t - \frac{3}{E}\frac{B_q C_q}{\pi} \cos \left( \frac{\pi t}{C_q} \right) + \text{Const} \right]^{\frac{1}{3}}
$$

Apply initial condition $t = 0$, $h_0 = 0$

$$
0 = \left[- \frac{3}{E}\frac{B_q C_q}{\pi} + \text{Const} \right]^{\frac{1}{3}}
$$

$$
(0)^3 = \left(\left[- \frac{3}{E}\frac{B_q C_q}{\pi} + \text{Const} \right]^{\frac{1}{3}}\right)^3
$$

$$
\frac{3}{E}\frac{B_q C_q}{\pi} = \text{Const}
$$

Therefore the specific solution is,
$$
h = \left[ \frac{3}{E}A^{*}t - \frac{3}{E}\frac{B_q C_q}{\pi} \cos \left( \frac{\pi t}{C_q} \right) + \frac{3}{E}\frac{B_q C_q}{\pi} \right]^{\frac{1}{3}}
$$


Substituting the values here we find that,
$$
\frac{3}{E}\frac{B_q C_q}{\pi} \approx 1.91
$$

The final analytical solution is,

$$
h = \left[ - 3\frac{2}{\pi} \cos \left(\pi t \right) + 1.91 \right]^{\frac{1}{3}}
$$

The equation above is used to calculate the water level profile of the lake for any time $t \geq 0$, as shown in the Figure below.

{{< figure src="./analytical2/analytical2.png" title="Figure 2 - Water level profile for second case." >}}

In the next post, we will see how to model the reaches using the De Saint Venant Equations. I see you in the next post.
