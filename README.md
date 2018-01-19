# Assignment1 - Practice Designing Models (Template)

> * Participant name: Michael Sterkel 
> * Project Title: Food Waste in Supermarkets 

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

Orlando, home of Mickey Mouse and his friends but more importantly home to people who work, live and play in the city and its surrounding areas.  The people who live in Orlando have the basic necessities of needing a place to live, needing to work and needing to eat.  To satisfy the need to eat, Orlando residents can go out to eat at a restaurant or buy food at a local supermarket to take home to cook and eat.  Supermarkets are a wonder of the modern world in their ability to provide cosumers with year round choices of produce regardless of season and the modern consumer has become accustomed to being able to buy whatever produce they want at anytime of the year. 

The ability to use the global economy to procure produce is a remarkable feat by the supermarket but it does come with a downside in terms of food waste.  To satisfy the consumer's demand for choice, supermarkets must keep their shelves stocked with a multitude of products, however this can lead to an overabundance of stock that must be thrown away when it is no longer fit for sale.   On top of this we, the consumer, have become very accusted to only buying the best looking produce or what we have been told is the best looking and will shun the items that do no meet this criteria even if they are still edible.  

Finding a solution to getting this produce sold to cut down on food waste is an important topic to understand and try and solve due to the amount of food wasted in the US annually, which is estimated by the USDA to be around 30-40 percent (https://www.usda.gov/oce/foodwaste/faqs.htm).  This problem is more than just a waste of resources and money by the population, it impacts the amount of farm land needed to grow the food, space taken up in landfills and it effects our food security (https://www.usda.gov/oce/foodwaste/faqs.htm).

The statistics above are for both the retail and consumer side and both have parties have a role to play in reducing food waste.  The focus will be on the retail side and how they could improve their ability to sell a greater majority of produce received.  One solution I have witnessed first hand is the selling of blemished, older produce at drastically reduced prices to persuade customers to purchase the item in order to prevent the produce from being discarded.  The produce was still edible it just was not quite as fresh as the full priced items and did not necessarily look as pretty. I myself have purchased these kinds of produce at where they did this very thing at  supermarkets when I lived out in California.

The focus of the simulation will be to determine if reducing the price on older/blemished produce will help to sell more of the inventory than current methods.

## Requirements (Experimental Design)

The purpose of this simulation is to determine if selling older and blemished produce at reduced prices (i.e. %50 off, 75% off) will increase the amount of produce purchased and reduce the amount of produce thrown away due to the produce going beyond its sellable date.

As stated in the problem a Smart City is one where different electronic data collection sensors are used to gather data to allow the more efficient management of resources.  In the context of the problem of supermarkets and food waste data would be collected on the age of produce when it is purchased and if sale prices have an influence on the movement of stock.  Most produce in supermarkets are already marked with small barcodes which could be modified to pass imbedded "picked on" dates and "best by" dates and store price scanners could be modified to be able to read these thus providing age data on the produce.  The age data could then be used to rotate produce in the sections to bring older, but still edible produce, to the front to get sold and it could help determine optimal arrangements of items based on certain layouts for promotoing the most turnover.  Data on how quickly items sell from when they arrived at the store can provide data to the supermarket about the most optimal reordering cycle to reduce the amout of excess inventory that needs to be sold.  One last benefit is an ability to pick out the produce that needs to be put in a more heavily discounted section by being able to scan to see the day it was picked and the first day it was put on the shelf.

Inputs to the system would be the amount of produce in the store, the age of the produce and the price of the produce.  The outputs would be the amount of produce sold, the age when sold and the price it was sold.


## Smart City (My Problem) Model

The below links provide details on the model.  The object diagram provide a high level overview of components, the Class diagram provides details on attributes of the system and the behavior diagram provides details of the behavior of the model.

* [**Object Diagram**](model/object_diagram.md)
* [**Class Diagram**](model/class_diagram.md)
* [**Behavior Diagram**](model/behavior_diagram.md) 


## Smart City (My Problem) Simulation

The simulation for this the supermarket waste problem will be built using Agent Based Simulation techniques and will focus on the produce section.  The simulation will test the hypothesis of whether selling older, blemished produce at a lower price point will reduce food waste. A simulation of supermarket will be created.  Information about shopping habits will be gathered to provide inputs to the simulation.  Full details are provided in the [**Analysis Readme**](analysis/SupermarketFoodWaste.md).


## Smart City (My Problem) Model
[**Code template**](code/README.md) Links to page with code and code description.

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
 [**POTS System**](code/POTS_system/README.md) 
 
