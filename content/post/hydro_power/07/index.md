---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Modelling, Simulation and Control of Hydro-Power System - Part 7"
subtitle: "Model of lakes, ducts, pumps and turbines"
summary: "In this series I will show the entire process of developing a model, performing simulations and the use of different control techniques for decision support in flood management systems."
authors: []
tags: ["Flood Forecasting", "Model Predictive Control"]
categories: ["Flood Management"]
date: 2022-02-06T10:01:00
lastmod: 2022-02-06T10:01:00
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

# Overview

In this post we will use the previously developed code starting from  [part 4]({{<  relref "../04"  >}}) to write the code that will be used to simulate the dynamics of lakes, turbines, pumps and ducts (not the complete dynamics, but the relevant one taking some assumptions into consideration). As I mentioned in the previous part, all that code was organized and restructured to create a library, **cacao**. You can check the structure of this project [here](https://github.com/euanrussano/cacao).

## Simulation of the lakes

The dynamics of the lake, as previously described, is governed by the mass conservation equation. Additionally, the height of water in a lake can be calculated by a relation $h=f(m)$, where $h$ is the height and $m$ the actual mass of water in the lake. As an example, for a lake with constant cross-section $A$, containing liquid (incompressible fluid) with density $\rho$, the relation between height and mass can be written as:

$$
h = \frac{m}{A \rho}
$$

Or in an implicity form:

$$
m - h A \rho = 0
$$

For the mass conservation, a lake may have multiple inflows and outflows, so we will create a `inlet` list and an `outlet` list which will hold a variable number of input(s)/output(s). Taking all of these points into consideration, the code for the lake is:

<script src="https://gist.github.com/euanrussano/ad53fb7b1ba1afb3caa4102eb50f610a.js?file=tank.py"></script>

Now it can be a bit confusion because I named the class `Tank` instead of `Lake`. That's because I want to keep the idea of being as general as possible. So I think the term `Tank` is more generic, as it can be used to represent whatever kind of fluid container, and not only specific lakes. Notice that this class inherits from the class `Block`, one of the classes that was written in [part 5]({{<  relref "../05"  >}}) of this series. The class contains two objects of `Variable` class (`mass` and `height`). Because I have 2 variables, I need two constraints for make it completely defined (no degrees of freedom). The two constraints are the `mass_balance` and the `volume_height`, which represents the mass conservation and the height and mass relation, respectively.

Another interesting concept I brought here is the use of [composition](https://en.wikipedia.org/wiki/Composition_over_inheritance) by incorporating a property `content` which I want to hold all the properties of the material (e.g water) in the `Tank` object.

## Material and Content

I wrote two specific classes to hold the specific properties of the material being transported in the lakes, reaches, pumps, etc. The purpose of this is to have flexibility and not be restricted to use only water for example as a fluid.

<script src="https://gist.github.com/euanrussano/ad53fb7b1ba1afb3caa4102eb50f610a.js?file=thermo.py"></script>

These are relatively simple classes, each one with a purpose. The class `Material` contains the specific properties of the chemical compound (e.g water) in a broad sense, while the `Content` class describes a specific amount of that chemical compound. To better understand, water would be a `Material`, while 1 kg of water would be a `Content` object. I may need to refactor this code a bit in the future to be able to handle solutions (e.g salt diluted in water) but for now it should be enough to simulate just pure fluids.

## Simulation of ducts

In a simplified simulation approach, the ducts can be seen simply as orifices through which fluid flows from one tank to another, due to potential energy (level of fluid) upstream or downstream. The potential energy is converted into kinetic energy, generating flow of material. The direction and magnitude of the flow depends on the level upstream and downstream. If the upstream level is higher than the downstream, then flow occurs in the upstream-downstream direction. If downstream level is higher, than the flow is in downstream-upstream direction. The basic equation governing this flow is:

$$
W_q = sign(H_{up} - H_{down}) \rho A c \sqrt{2g |H_{up} - H_{down}|}
$$

Where $W_q$ is the mass flow rate, $H_i$ is the level, $\rho$ the fluid density, $A$ the cross section area of the duct/orifice, $c$ the flow coefficient due to specific characteristics of the orifice/duct geometry.

<script src="https://gist.github.com/euanrussano/ad53fb7b1ba1afb3caa4102eb50f610a.js?file=orifice.py"></script>

## Simulation of Turbines and Pumps

Turbines and pumps are hydraulic elements which can convert kinetic energy from fluid flow into electric energy or the other way around, respectively. Therefore the turbine can be interpreted as an specific `Orifice` element which is able to convert kinetic energy into eletric energy, thus decreasing the fluid flow rate. On the other hand, the pump can impose a specific flow rate. In both cases, a control signal can be used to manipulate their operation between 0 and 100% of its capacity.

<script src="https://gist.github.com/euanrussano/ad53fb7b1ba1afb3caa4102eb50f610a.js?file=eletric.py"></script>
