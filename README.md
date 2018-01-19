# Assignment1 - Practice Designing Models (Template)
(remove: **text between brackets to be removed**)

> * Participant name: Michael Sterkel 
> * Project Title: Food Waste in Supermarkets 

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

(remove: States your motivation clearly: why is it important / interesting to solve this problem?)
(remove: Add real-world examples, if any)
(remove: Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)

Orlando, home of the free, home of the brave, home of Mickey Mouse but more importantly home to people who work, live and play in the city and its surrounding areas.  The people who live in Orlando have the same basic necessities of needing a place to live, needing to work and needing to eat.  To satisfy the need to eat, Orlando residents can go out to eat at a restaurant or buying food at a local supermarket to take home to cook and eat.  Supermarkets are a wonder of the modern world in their ability to provide cosumers with year round choices of produce regardless of season the modern consumer has become accustomed to being able to buy whatever produce they want at anytime of the year. 

The ability to use the global economy to procure produce is a remarkable feat by the supermarket but its does come with a downside in terms of food waste.  To satisfy the consumer's demand for choice, supermarkets must keep their shelves stocked with a multitude of products but this can lead to an overabundance of stock that must be thrown away when it is no longer fit for sale to the public.   On top of this we, the consumer, have become very accusted to only buying the best looking produce or what we have been told is the best looking and will shun the items that do no meet this criteria even if they are still edible.  

Finding a solution to getting this produce sold to cut down on food waste is an important topic to understand and try and solve due to the amount of food wasted in the US annually which is estimated by the USDA to be around 30-40 percent (https://www.usda.gov/oce/foodwaste/faqs.htm).  This problem is more than just a waste of resources and money by the population, it impacts the amount of farm land needed to grow the food, space taken up in landfills and it effects our food security (https://www.usda.gov/oce/foodwaste/faqs.htm).

The statistics above are for both the retail and consumer side and both have parties have a role to play in reducing food waste.  The focus will be on the retail side and how they could improve their ability to sella greater majority of produce received.  One solution I have witnessed first hand is the selling of blemished, older produce at drastically reduced prices to persuade customers to buy to prevent the produce from being discarded.  The produce was still edible it just was not quite as fresh as the full priced items and did not necessarily look as pretty. I myself have done this at supermarkets when I lived out in California and they did this.

The focus of the simulation will be to determine if reducing the price on older/blemished produce will help to sell more of the inventory than current methods.

## Requirements (Experimental Design)

(remove: You should start by specifying a set of requirements. I specified a topic Smart Cities but what exactly does that mean-  you should practice formulating your own set of requirements and an experiment. Define a hypothesis of a problem cities face and how a smart city would possibly help alleviate this issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

The purpose of this simulation is to determine if selling older and blemished produce at reduced prices (i.e. %50 off, 75% off) will increase the amount of produce purchased and reduce the amount of produce thrown away due to the produce going beyond its sellable date.

As stated in the problem a Smart City is one where different electronic data collection sensors are used to gather data to allow the more efficient management of resources.  In the context of the problem of supermarkets and food waste data would be collected on the age of produce when it is purchased and if sale prices have an influence on the movement of stock.  Most produce in supermarkets are already marked with small barcodes which could be modified to pass imbedded "picked on" dates and "best by" dates and store price scanners could be modified to be able to read these thus providing age data on the produce.  The age data could then be used to rotate produce in the sections to bring older, but still edible produce, to the front to get sold and it could help determine optimal arrangements of items based on certain layouts for promotoing the most turnover.  Data on how quickly items sell from when they arrived at the store can provide data to the supermarket about the most optimal reordering cycle to reduce the amout of excess inventory that needs to be sold.  One last benefit is an ability to pick out the produce that needs to be put in a more heavily discounted section by being able to scan to see the day it was picked and the first day it was put on the shelf.

Inputs to the system would be the amount of produce in the store, the age of the produce and the price of the produce.  The outputs would be the amount of produce sold, the age when sold and the price it was sold.



## Smart City (My Problem) Model

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

The below links provide details on the model.  The object diagram provide a high level overview of components, the Class diagram provides details, the behavior diagram provides details of the behavior of hte model and the Agent/User case provides details on what the Agent/s do.

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City (My Problem) Simulation

(remove: for part 3 add two to three sentences here and link the [**(your own name)**](model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)

The simulation for this the supermarket waste problem will be built using Agent Based Simulation techniques and will focus on the produce section.  The simulation will test the hypothesis of whether selling older, blemished produce at a lower price point will reduce food waste a simulation of supermarket will be created.  Information about shopping habits will be gathered to provide inputs to the simulation.  Full details are provided in the [**Analysis Readme**](analysis/SupermarketFoodWaste.md).


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
