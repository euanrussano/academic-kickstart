---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Modelling, Simulation and Control of Hydro-Power System - Part 3"
subtitle: "Theoretical model of the reaches"
summary: "In this series I will show the entire process of developing a model, performing simulations and the use of different control techniques for decision support in flood management systems."
authors: []
tags: ["Flood Forecasting", "Model Predictive Control"]
categories: ["Flood Management"]
date: 2021-02-21T10:01:00
lastmod: 2021-02-21T10:01:00
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

# Table of Contents

+ [Part 1 - System description]({{<  relref "../01"  >}})
+ [Part 2 - Theoretical model of the lakes]({{<  relref "../02"  >}})
+ [Part 3 - Theoretical model of the reaches]({{<  relref "../03"  >}})
+ [Part 4 - Implementing the model of lakes using DAE approach with Python]({{<  relref "../04"  >}})
+ [Part 5 - Improving the DAE approach using OOP with Python]({{<  relref "../05"  >}})
+ [Part 6 - Packing the code in a python library]({{<  relref "../06"  >}})
+ [Part 7 - Model of lakes, ducts, pumps and turbines]({{<  relref "../07"  >}})

## Overview

In the previous post of this series (see [here](/post/hydro_power/02)), I showed how to develop a mathematical representation of the lake component in the hydro-power system. In this post I will present a one-dimensional mathematical model of the reaches.

As commented in a previous post, a reach is a section of a river, with more or less uniform geometry, such that it can be interpreted as one component in the complete model.

The state of the art way of modelling this dynamics is the De Saint Venant Equations. It consists in a pair of nonlinear partial differential equations (PDE) that represent one dimensional hydraulics. One equation describes the mass conservation while the other describes momentum conservation.

## Mass conservation of the reaches

Let's start by the mass conservation equation for the reach. As shown for the lake, the accumulation of mass $m$ increases with the mass entering the reach $w_{in}$ and decreases with the mass $w_{out}$ leaving it , such that:
$$
\frac{dm}{dt} = w_{in} - w_{out}
$$
Which can be rewritten in terms of volume $V$ and density of water $\rho$,
$$
\frac{d(\rho V)}{dt} = \rho q_{in} - \rho q_{out}
$$
Where $q$ is volumetric flow rate (e.g $m^3/s$). The liquid water can be considered an incompressible fluid, so the density is constant and can be taken out of the differential term. Additionally, the volume $V$ can be written in terms of the the reach geometry, which are the wetted area $A$ and the length of the reach $x$
$$
\frac{d(Ax)}{dt} = q_{in} - q_{out}
$$
The reach length $x$ does not depend on time and it can be taken out of the differential term.
$$
\frac{dA}{dt} = \frac{q_{in} - q_{out}}{x}
$$
For an infinitesimally small length of the reach, the above ordinary differential equation (ODE) is written as a PDE:
$$
\frac{\partial A}{\partial t} = -\frac{\partial q}{\partial x}
$$
Or the most known form of this equation, incorporating the possibility of a lateral inflow in the reach is,
$$
\frac{\partial A}{\partial t} + \frac{\partial q}{\partial x} = q_{lat}
$$
It's important to note here that the wetted area $A$ is dependent on the geometry of the reach and on the amount of water. By knowing the relation between this variable and the water level $h$, it's possible to calculate one from the other.

With the mass conservation well defined, let's move on to the momentum conservation.

## Momentum conservation of the reaches

According to Newton's second law, the time rate of change of the linear momentum of a system must be balanced by the sum of all external forces acting on/by the system. This property directly affects the velocity, since the momentum is by definition the product of mass and velocity of a system. It can be written as:
$$
\sum \overrightarrow{F} = \frac{\partial}{\partial t}\int_{CV}\rho \overrightarrow{v}dV+\int_{CV}\rho \overrightarrow{v}(\overrightarrow{v} \cdot \overrightarrow{n})dA
$$
The first term on the right-hand side of the above equation represents the time rate of change of momentum "stored" in the control volume CV, where $\overrightarrow(v)$ is the velocity of the system. The second term is the net outflow of momentum across the control surface.

The net outflow of momentum is given by the difference in moment outgoing and moment incoming in the control volume. The inflow is defined as:
$$
-\rho(Q+qdx)
$$
The inflow is translated into momentum by multiplying it with the velocity. A correction factor $\beta$ is normally also incorporated into the equation, due to non-uniform velocity distribution across the reach cross-section.
$$
\int_{inlet}\rho \overrightarrow{v}(\overrightarrow{v} \cdot \overrightarrow{n})dA =-\rho(\beta v Q+\beta v_x q dx)
$$
Where $v_x$ is the (averaged) lateral inflow. The factor $\beta$ is calculated as:
$$
\beta = \frac{1}{v^2A}\int \int v^2 dA
$$
As mentioned by [Gündüz, O.](https://kisi.deu.edu.tr/orhan.gunduz/english/courses/2_derivation_flow_equations.pdf), in most cases $1.01 \leq beta \leq 1.33$, where lower values are used for reaches with geometry that resembles a prism, and higher values for those like river valleys with floodplains.

The moment outflow is calculated from the mass outflow of the reach. Since it is known that this is a function of mass inflow, Taylor series expansion may be used, and the moment outflow is:
$$
\int_{outlet}\rho \overrightarrow{v}(\overrightarrow{v} \cdot \overrightarrow{n})dA = \rho(\beta v Q+\frac{\partial (\beta v Q)}{\partial x} dx)
$$
Putting moment inflow together with outflow we have:
$$
\int_{CV}\rho \overrightarrow{v}(\overrightarrow{v} \cdot \overrightarrow{n})dA = -\rho \left( \beta v_x Q- \frac{\partial (\beta v Q)}{\partial x} \right) dx
$$
Regarding the first term on the right-hand side of the momentum equation, it represents the time rate of change of momentum stored in the control volume . It is associated with the elemental lenth $x$, and can be written as:
$$
\frac{\partial}{\partial t}\int_{CV}\rho \overrightarrow{v}dV = \rho \frac{\partial Q}{\partial t}dx
$$
For the left-hand side of the momentum equation, the 5 forces that may act on it are:

- gravity force $F_g$ because of the weight of water.
- pressure force $F_p$ due to atmospheric and hydraulic pressure
- friction force $F_f$, due to water contact with the bottom and the sides of the reach.
- contraction/expansion force $F_e$, related to drastic changes in the reach cross-section.
- wind shear force $F_w$

### Gravity Force

Hydrostatic pressure is given by the column formed by water. 
$$
dm = \rho dV = \rho A dx
$$
The weight force $W$ is the mass multiplied by the gravity acceleration.
$$
W = gdm = \rho gAdx
$$
Where $g$ is the gravitational acceleration. For momentum , the relevant component of weight is the one in the direction of the flow, which we interpret here as the gravity force $F_g$.
$$
F_g = \rho g A dx \sin \theta
$$
Where $\theta$ is the inclination of the channel bed.

{{< figure src="./gravity_force.png" title="Figure 1 - Gravity Force." >}}

For small inclinations of the reach, it can be assumed that,
$$
\sin \theta \approx \tan \theta
$$
With that, the gravity force can be written as,
$$
F_g = \rho g A dx S_0
$$
Where $S_0$ is slope of the channel bed.

### Pressure Force

The pressure force $F_p$ results from a balance between the hydrostatic pressure exerted on each side of the control volume ($F_{pl}$ at the left and $F_{pr}$ at the right), as well as the pressure exerted by the banks $F_{pb}$, such that:

$$
F_p = F_{pl} - F_{pr} + F_{pb}
$$

It can be shown (I will skip the derivations here) that this expression can be expanded to:

$$
F_p = -\left( \rho g \frac{\partial y}{\partial x} A + \int_0^y \rho g (y-w) \frac{\partial b}{\partial w}dw \right)dx + \left( \int_0^y \rho g (y-w)\frac{\partial b}{\partial x}dw\right)dx
$$

Where $y-w$ is the depth that the element of water is immersed, which gives the hydrostatic pressure $\rho g (y-w)$, and $b$ is the width of the element across the reach.

Simplifying and rearranging, it can be seen that the resultant pressure force is expressed as:

$$
F_p = -\rho g \frac{\partial y}{\partial x}A dx
$$

### Friction Force

In any real reach with rough bottom and sides, mechanical energy is transformed into heat through shear stress $\tau$. For a steady uniform flow, the shear stress can be written as:

$$
\tau_0 = \rho g R S_f
$$

Where $R$ is the hydraulic radius.

$$
R = A/P
$$

Where $P$ is the wetted perimeter and $S_f$ is the friction slope. This last one comes from Manning Equation, and defined as,

$$
S_f = \frac{n^2 v^2}{\mu^2 R^{4/3}}
$$

Where $n$ is Manning's roughness coefficient, $v$ is the flow velocity and $\mu$ is a constant to convert between SI units ($\mu=1.0$) and Imperial units ($\mu=1.49$).

For an unsteady, non-uniform flow, the shear stress $\tau$ can be written in terms of $\tau_0$.

$$
\tau = -\tau_0 P dx
$$

The final form of the friction force can then be defined as:

$$
F_f = - \rho g A S_f dx
$$

### Contraction/expansion Force

Drastic changes in the reach geometry causes energy losses due to turbulence. These forces can be related to the friction force, with the difference that the friction slope $S_f$ is replaced by the energy grade slope $S_e$, representing such loss due to contraction/expansion.

$$
S_e = \frac{K_e}{2g}\frac{\partial (Q/A)^2}{\partial x}
$$

Where $K_e$ is a coefficient that is negative for expansion and positive for contraction. The final equaion of contraction/expansion force $F_e$ is very similar to the friction force.

$$
F_e = - \rho g A S_e dx
$$

### Wind shear Force

Wind blowing against the free surface of the water generates a shear stress $\tau_w$. The greater the shear stress, the greater the wind shear force. The wind shear force is also a function of a wind shear factor $W_f$ and the water density, thus we can write:

$$
\tau_w = -\rho W_f
$$

where:

$W_f = \frac{C_f |v_r| v_r} {2}$

Here, $C_f$ is a constant coefficient related to the shear stress and $v_r$ is the relative velocity of the water with respect to the boundary. It can be defined as:

$$
v_r = \frac{Q}{A}-v_w \cos \omega
$$

Being $v_w$ the velocity of wind, and $\omega$ is the angle that such velocity makes with the average water velocity. The final form of the wind shear stress, considering that $\tau_w = \tau_w B dx$ is:

$$
F_w = -\rho W_f B dx
$$

### Final form of the momentum equation

Joining together all the pieces described above and simplifying, the momentum equation can be written in the following form:

$$
\frac{\partial Q}{\partial t} + \frac{ \partial (\beta Q^2 / A)}{\partial x} +g A\left( \frac{\partial h}{\partial x} + S_f +S_e \right) - \beta q v_x + W_f B = 0
$$

## Summary

The De Saint Venant equations consisted in a 1D unsteady hydrodynamic model which describes the mass and momentum conservation of a system (in the present case, a reach or river section). These two equations are always addressed together. In the differential form they read:

$$
\frac{\partial A}{\partial t} + \frac{\partial q}{\partial x} - q_{lat} = 0
$$

$$
\frac{\partial Q}{\partial t} + \frac{ \partial (\beta Q^2 / A)}{\partial x} +g A\left( \frac{\partial h}{\partial x} + S_f +S_e \right) - \beta q v_x + W_f B = 0
$$

For a steady flow, the derivatives with respect to time becomes equal to zero, so **for steady flow**:

$$
\frac{\partial q}{\partial x} - q_{lat} = 0
$$

$$
\frac{ \partial (\beta Q^2 / A)}{\partial x} +g A\left( \frac{\partial h}{\partial x} + S_f +S_e \right) - \beta q v_x + W_f B = 0
$$

This ends the theoretical description of the modelling process. In the next post, we will see how to simulate the lakes. Hope to see you there!

## References

[Gündüz, O. Derivation of flow equations. ](https://kisi.deu.edu.tr/orhan.gunduz/english/courses/2_derivation_flow_equations.pdf)

Petrone, F. (2010). Model Predictive Control of a Hydro Power Valley.
