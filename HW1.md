# Assignment1 - Practice Designing Models (Template)
(remove: **text between brackets to be removed**)

> * Participant name: Michael Sterkel (Your name)
> * Project Title: Food Waste in Supermarkets (Title of the problem you are looking and modeling)

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

(remove: States your motivation clearly: why is it important / interesting to solve this problem?)
(remove: Add real-world examples, if any)
(remove: Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)

Orlando is a bustling city in which many people associate with Mickey Mouse and the 4 parks theme parks he runs around and the swarms of tourists that come visit him every year.  However, Orlando is home to people who live, work and play in the area and thus must meet basic needs of having place to live and procuring things to eat.  For most residents of Orlando, procuring things to eat means either going to a restaurant or buying food at a local supermarket and then taking the food home to cook.  Supermarkets, with our interconnected global economy, are able to provide almost any type of food year round to provide many different choices for the consumer.  Now this choice rates very high with the modern consumer as they can buy and prepare whatever they want anytime of yea.

The downside to this type of design is that supermarkets must stock a multitue of food that may not get bought before it is no longer sellable to the public.  On top of this we, the consumer, have become very accusted to only buying the best looking produce or what we have been told is the best looking and will shun the items that do no meet this criteria even if they are still edible.  

Finding a solution to getting this produce sold to cut down on food waste is an important topic to understand and try and solve due to the amount of food wasted in the US annually which is estimated by the USDA to be around 30-40 percent annually (https://www.usda.gov/oce/foodwaste/faqs.htm).  This problem is more than just a waste of resources and money by the population, it impacts the amount of farm land needed to grow the food, space taken up in landfills and it effects our food security (https://www.usda.gov/oce/foodwaste/faqs.htm).

The statistics above are for both the retail side of the consumer and both have parts to play in reducing food waste.  The focus will be on the retail side and how they could improve their ability to sell all produce received.  One solution I have witnessed first hand that I have partaken in is the selling of blemished, older produce at drastically reduced prices to persuade customers to buy to prevent it from being discarded.  The goal of this was to persuade customers to overlook the blemish and purchase because it is not at fully price.  I myself have done this at supermarkets when I lived out in California and they did this.

The goal of is to simulate consumers buying produce based on its quality, which in this model is based on number of days produce has been on the shelf.  T

## Requirements (Experimental Design)

(remove: You should start by specifying a set of requirements. I specified a topic Smart Cities but what exactly does that mean-  you should practice formulating your own set of requirements and an experiment. Define a hypothesis of a problem cities face and how a smart city would possibly help alleviate this issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

The purpose of this model is to determine if selling older and blemished produce will reduce the amount of produce thrown away at supermarkets due to them going past the quality that can be sold to consumers.  

A Smart City would help in this area due to its ability to keep track of large data sets and have these data sets organized in a predetermined way.  The Smart City would allow stores to track not only quantity of inventory but also how old an item was when it was sold.  THis would allow a store to see at what price point an item will see based on if it is blemished or older than the fresh produce that just arrived.  By tagging certain items the store can see the speed at which items sell to help determine a more optimal reordering cycle that reduces the amount of excess items that are brought in to sell.

Inputs to the system would be the amount of produce in the store, the age of the produce and the price of the produce.  The outputs would be the amount of produce sold, the age when sold and the price it was sold.



## Smart City (My Problem) Model

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City (My Problem) Simulation

(remove: for part 3 add two to three sentences here and link the [**(your own name)**](model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)

In order to test the hypothesis about whether selling older, blemished produce at a lower price point will reduce food waste a simulation of supermarket will be created.  The simulation will focus on the produce department.  Full simulation details are here.


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
