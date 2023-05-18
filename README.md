# Break the Bank
<!-- <img src="https://github.com/kielran/breakthebank/blob/jane-story/imgs/logo.PNG" width=10% height=10%></img> -->
By 9Lives++: [Gency Dela Torre](https://github.com/gen-cy), [Jane Ran](https://github.com/kielran), [Andre Nguyen](https://github.com/nguyena537), [Zhiyuan (Aidan) Wen](https://github.com/zhiyuanwen), [Alexander Kaattari-Lim](https://github.com/DiscoDoggy)

<img src="https://github.com/kielran/breakthebank/assets/72327643/fc8307aa-b5db-46e6-8963-d88469fc4b8f" width=60% height=60%></img>


## Project Description
Our team developed Break the Bank with the goal of modernizing the classic 2-player-1-keyboard indie game scheme popular in the early 2010s. Player(s) interact with the map by controlling characters using the W-A-S-D and up-down-left-right keys, completing the stage by moving their characters to their respective exits.

<img src="https://github.com/kielran/breakthebank/assets/72327643/df14aa8e-1f20-430c-be02-eebda2517a45" width=60% height=60%></img>

## Languages & Tools
* Programming: Python
* Libraries: Pygame
* Version Control: Github
* IDE: Visual Studio Code
* Diagramming: Visual Paradigm
* Art Assets & Animation: Clip Studio Paint

## Project Input/Output
Players will interact with the game through direct keyboard commands which translate into real-time changes on the screen. The player will be able to move around the map, jump, collect points, pick up their unique item, and use their item to manipulate objects and scenarios on the map. Correct inputs will be rewarded with a higher game score and passage to the next stage.
<img src="https://github.com/kielran/breakthebank/blob/jane-story/imgs/tutorial.PNG" width=60% height=60%></img>

## Implementation
* Composite pattern: Gives buttons a wider array of usage. From one primary Button class we are able to derive buttons to control menu swapping, quitting, stage selection, audio muting, and the unique tutorial hover function. (work in progress)


<!-- We chose this
We will be using Composite, Factory and Strategy. For the composite pattern:  
   * Why you picked this pattern and what feature you will implement with it  
   We selected Composite for easier implementation of similar objects (making enemy types that derive from a generic Enemy class, for example, and having all things in the game be Entity class objects).  
   * What problem you anticipate encountering when implementing your project that you will solve using the design pattern  
   We want to have a large variety of entity class derived-types but still allow the player to interact with each of them in unique yet consistent ways. 
   * Why the chosen design pattern will lead to a good solution to that problem  
   Using a composite structure of subclasses derived from one master "entity" class saves time from having to rewrite the same methods each time for every new enemy type. On top of that, this keeps the expected results of common actions consistent with other entities. This design pattern can be extended to the "room" object as well, where one master room object contains some basic functionality such as "observe" or "search" and subclasses such as battle rooms, trapped rooms or loot rooms derive from said master room object. We can use this to achieve runtime polymorphism by calling the same dealDamage(), interact() etc. methods on those objects. 
   In this pattern, the Quest class is the component class, which contains an aggregation of Room objects. Room is a composite object from which CombatRoom and OddityRoom are derived from. 
   
For the factory pattern: 
   * Why you picked this pattern and what feature you will implement with it  
   Random generation of quests is intended to be a feature, so we need a factory to create many different objects (items, enemies, rooms) based on various critiera (difficulty, rarity etc.) and link them together. 
   * What problem you anticipate encountering when implementing your project that you will solve using the design pattern  
   We need to create many objects with unique definitions in their own files, so a factory pattern is ideal for doing so. 
   * Why the chosen design pattern will lead to a good solution to that problem  
   We can have a factory class that keeps track of and manages all different types of items, enemies and rooms we will be creating. It allows for unique generate() functions that we can use to generate a large amount of random objects to populate quests with. 
   
For the strategy pattern:
   * Why you picked this pattern and what feature you will implement with it  
   As this is a game, the player should have many options to choose from. Options in combat, options in traversing rooms, options when resting at town. 
   * What problem you anticipate encountering when implementing your project that you will solve using the design pattern  
   We want the user to be able to select a strategy for their player character at runtime. 
   * Why the chosen design pattern will lead to a good solution to that problem  
   We will create various strategies and allow the user to select them by interacting with the program. 

## Design Documents

Class diagram: 
![image](https://user-images.githubusercontent.com/49847628/110477489-13c51700-8098-11eb-9f17-63cb3b7ee28d.png)

This diagram shows the structure of our program. The Composite pattern consists of Quest (the component class), Room (the composite class), CombatRoom and OddityRoom (leaf classes that are derived from the Room class). Quest is the handler for the various rooms while the room types manage the different kinds of encounters the player can come across. The Factory pattern consists of a Generator, which generates the three types of objects - Entities (enemies), Rooms and Items, for usage in Quest. The Strategy pattern is implemented in Adventurer, where the client interacts during runtime with the class to choose a strategy during combat, when roaming the town and when traversing between rooms. 

 ## Screenshots
Combat:
![image](https://user-images.githubusercontent.com/49847628/110477138-a913db80-8097-11eb-90b9-7b081463db1c.png)

Combat 2:\
![image](https://user-images.githubusercontent.com/49847628/110477390-f2fcc180-8097-11eb-9f74-e1ecbb5694f7.png)

Room traversal and item inspection: 
![image](https://user-images.githubusercontent.com/49847628/110477084-98fbfc00-8097-11eb-816a-9de00dfa9cf1.png)

Town roaming and quest board:\
![image](https://user-images.githubusercontent.com/49847628/110477197-b9c45180-8097-11eb-856d-c5e2916d9595.png)

Special room interaction and player inspect:
![image](https://user-images.githubusercontent.com/49847628/110477217-c183f600-8097-11eb-89fb-935a0a58e501.png)
 
 ## Installation/Usage
 1. Clone this repository recursively in your terminal using `git clone --recursive` and the https link under the code button. 
 2. Run `cmake3 .` and `make` to compile the program. If that doesn't work, you can alternatively compile with the command `g++ source/main.cpp source/Adventurer.cpp -std=c++11` instead. There is also a pre-compiled release executable (see step below). 
 3. Run the main executable. Enjoy! Please let us know of any comments/suggestions/bugs :)
 
 ## Testing
 We created unit tests for the various methods in the program and also extensively tested the functionality of all items, abilities, enemies and rooms within main. There are specific test files (under tests directory) for entities, items, rooms, and town which ensure that all of these objects execute properly. In order to test all the components working together, we created test cases within main simulating the user.  -->
 
