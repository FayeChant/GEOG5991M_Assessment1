# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
#1.2 SET OTHER VARIABLES
#set number of agents to 10
num_of_agents = 10
#set number of agent moves TO 100
num_of_iterations = 100
#1.2 START LOCATION - assigned coordinates to each agent in 'num_of_agents' using a random grid of 100 by 100
for i in range (num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#2. MOVE AGENTS 
#2.1 RANDOM WALK 'NUM_OF ITERATIONS' STEPS
    for j in range (num_of_iterations):
#change y0
        if random.random () <0.5 :
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
#change x0
        if random.random () <0.5 :
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100 

#3.PRINT FINAL COORDINATES   
print (agents)

#4. GRAPHICS
#4.1 SCATTER PLOT
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.scatter(agents[i][0], agents[i][1])
matplotlib.pyplot.show()

#5. CALCUALTIONS 
#5.1 DISTANCE BETWEEN THE TWO AGENTS
print (max (agents, key=operator.itemgetter(1)))





