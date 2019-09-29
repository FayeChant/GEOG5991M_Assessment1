"""Agent Based Model.
Copyright (C) <2019>  <Faye Chant>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
num_of_agents = 10
num_of_iterations = 100
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
#1.2 START LOCATION & ENVIRONMENT- for each agent in 'num_of_agents' assigned coordinates, and attach environment, and a list of agents using agentframework module and Agent class and a list of agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#2. MOVE AGENTS 
def update(frame_number):
    
    fig.clear()   
#2.1 RANDOM WALK 'NUM_OF ITERATIONS' STEPS using move function        
    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
          
    #plot a graph    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])

#3. GRAPHICS
#3.1 SCATTER PLOT
#animate sequence 
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()














