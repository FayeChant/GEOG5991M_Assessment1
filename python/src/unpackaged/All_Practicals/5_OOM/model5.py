# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot
import agentframework

#0.2 define functions
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
#set number of agents to 10
num_of_agents = 10
#set number of agent moves TO 100
num_of_iterations = 100
#1.2 START LOCATION - assigned coordinates to each agent in 'num_of_agents' using agentframework module and Agent class
for i in range (num_of_agents):
    agents.append(agentframework.Agent())

#2. MOVE AGENTS 
#2.1 RANDOM WALK 'NUM_OF ITERATIONS' STEPS using move function
for j in range (num_of_iterations):
    for i in range (num_of_agents):
        #move agent
        agents[i].move()

#3. GRAPHICS
#3.1 SCATTER PLOT
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show() 

#4. CALCUALTIONS 
#4.1 Distance between ech of the agents
for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b)      

  
