# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot
import time

#0.2 Start timer
start = time.clock()
#0.3 define functions
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
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
    for i in range (num_of_agents):
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
#  
#3. GRAPHICS
#3.1 SCATTER PLOT
#plot a graph
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
# matplotlib.pyplot.show() 

#4. CALCUALTIONS 
#4.1 Distance between ech of the agents
distance = []
for agents_row_a in agents:
     for agents_row_b in agents:
         distance.append([distance_between(agents_row_a, agents_row_b)])      
         print(distance)
#4.2 Max and Min distances between agents
print("maximum =", max(distance)) 
print("minimum =", min(distance))
#4.3 Calcualte time elapsed
end = time.clock()
print("time = " + str(end - start))        
