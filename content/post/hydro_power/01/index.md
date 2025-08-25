---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Modelling, Simulation and Control of Hydro-Power System - Part 1"
subtitle: "System description"
summary: "In this series I will show the entire process of developing a model, performing simulations and the use of different control techniques for decision support in flood management systems."
authors: []
tags: ["Flood Forecasting", "Model Predictive Control"]
categories: ["Flood Management"]
date: 2021-02-07T10:01:00
lastmod: 2021-02-07T10:01:00
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

A hydro power system is an human-made structure or arrangement of structures usually built with the main purpose of generating electric power, though it may also be used for recreation, flood mitigation or other reasons.

This system can be composed by lakes, reaches, dams, pumps, valves, turbines, ducts which connect the elements. Some of these elements must be controlled, either manually or automatically, in order to generate electricity while avoiding and minimizing the chances of flood or other accidents, such as dam breaking. For that, some constraints are usually imposed at the levels of the lakes and reaches, as well as on the flow rater of pipes and rivers.

In this series of post, we will see how to develop a model for an academic case of a hydro-power system, how simulations can be used to predict possible scenarios in such system, and how automatic control techniques can be used to keep track of certain properties of the system and avoid problems, or optimize energy production, for example.

## The hydro-power system

For the sake of simplicity, we will consider a system formed by 3 lakes and 3 reaches, as shown in the figure below.

{{< figure src="./hydro_power.png" title="Figure 1 - Scheme of the hydro-power system." >}}

A lake is basically a reservoir of water, i.e a big tank with one or more inlets and outlets, where water can accumulate (if there is more water entering the lake than leaving it). Such lakes may be artificial (man-made) or natural. Artificial lakes are usually created by deviating a water course or by excavation.

The lakes are interconnected using ducts, each one containing a controllable valve, turbine or pump. These elements can be used to change the local flow rates.

A reach, as defined by [USGS](https://www.usgs.gov/faqs/what-a-reach?qt-news_science_products=0#qt-news_science_products), is basically a river section with similar hydraulic attributes, such as discharge, area and slope. There are other possible definitions but we will stick to this one. Thus, a river with length of 100 km may be interpreted as a single reach if its properties are more or less uniform, or it may be interpreted as multiple reaches, if its properties vary significantly. In some cases, it may be worth to split a river into multiple reaches even when its properties are uniform, since this approach can help in the modelling process.

The following table summarizes all the components of the system as shown in the figure above.

|Element|Description|
|---|---|
|L|Lake|
|P|Pump|
|T|Turbine|
|R|Reach|
|V|Valve|
|D|Dam|
|In|Inflow|
|Out|Outflow|



## Definition of variables and assumptions

To simplify the model, we can take the following assumptions:

+ Negligible dynamics of valves, pumps and turbines. This may be assumed considering that the fast dynamics of such elements when compared with the flow rates from the interconnected elements, thus the flow rates are equal to their own set points;

Since the objective is to control electricity generation, while meeting some constraints, it's important to define which variables of the system are controlled, which are manipulated and which are disturbances (uncontrollable inputs).

**Controlled variables**

+ flow rates in ducts and reaches, from $i$ to $j$ ($q_{ij}$);
+ levels of lakes and reaches ($h_i$);
+ generated/consumed electric power ($p_i$);

**Manipulated variables**

+ opening rate of valves, in terms of flow rate reference ($u_i$);
+ opening rate of turbines, in terms of flow rate reference ($u_i$);
+ imposed flow rate of pumps, in terms of flow rate reference($u_i$);

**Disturbances/ Uncontrolled variables**

+ water inflow due to upstream section, tributaries ($d_i$)

The following block representation of the system illustrates the variables involved in the problem as described above.

{{< figure src="./hydro_power_block.png" title="Figure 2 - Block scheme of the hydro-power system." >}}

In the next post we will go over the development of the mathematical model for each components of this system.
