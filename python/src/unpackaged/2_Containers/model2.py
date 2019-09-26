# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:00:02 2019

@author: Faye
"""
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
#1.2 START LOCATION - assigned coordinates to each agent using a random grid of 100 by 100
    agents.append([random.randint(0,100),random.randint(0,100)])

#2. MOVE AGENT 1 
#2.1 Random walk one step
#change y0
        if random.random () <0.5 :
            agents[0][0] += 1
        else:
            agents[0][0] -= 1
#change x0
        if random.random () <0.5 :
            agents[0][1] += 1
        else:
            agents[0][1] -= 1  
#2.2 Random walk second step  
#change y0 
      if random.random () <0.5 :
            agents[0][0] += 1
        else:
            agents[0][0] -= 1
#change x0
        if random.random () <0.5 :
            agents[0][1] += 1
        else:
            agents[0][1] -= 1  

#3. MOVE AGENT 2
#3.1 Random walk one step
#change y1
        if random.random () <0.5 :
            agents[1][0] += 1
        else:
            agents[1][0] -= 1
#change x1
        if random.random () <0.5 :
            agents[1][1] += 1
        else:
            agents[1][1] -= 1  
#3.1 Random walk second step
#change y1 
      if random.random () <0.5 :
            agents[1][0] += 1
        else:
            agents[1][0] -= 1
#change x1
        if random.random () <0.5 :
            agents[1][1] += 1
        else:
            agents[1][1] -= 1 

#4.PRINT FINAL COORDINATES   
print (agents)

#5. CALCUALTIONS 
#5.1 DISTANCE BETWEEN THE TWO AGENTS
print (max (agents, key=operator.itemgetter(1)))

#6. GRAPHICS
#6.1 SCATTER PLOT
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='blue')
a = (max (agents))
matplotlib.pyplot.scatter(a[1], a[0], color='red')
matplotlib.pyplot.show()
