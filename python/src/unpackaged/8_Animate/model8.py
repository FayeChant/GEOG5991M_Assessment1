# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random
import operator
import matplotlib.pyplot
import agentframework4 as agentframework
import csv
import matplotlib.animation 
#0.2 Import csv environment data
#create empty environemnt list
environment = []
#open file
f = open('in.txt', newline='') 
#csv reader
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset: # A list of rows
    rowlist = []
    for value in row: # A list of value
        rowlist.append(value) # append values to row
    environment.append(rowlist) #append rows to envt
f.close()
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show() 
#0.3 Define functions
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#1. SET UP THE AGENTS
#1.1 Create an empty list to contain all the agents
agents = []
#set number of agents to 10
num_of_agents = 10
#set number of agent moves TO 100
num_of_iterations = 100
#set neighbourhood
neighbourhood = 20
#
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
#1.2 START LOCATION & ENVIRONMENT- for each agent in 'num_of_agents' assigned coordinates, and attach environment, and a list of agents using agentframework module and Agent class and a list of agents
for i in range (num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
# print another agents x loc
print("agent 1 x =", agents[0].agents[1].x)

#2. MOVE AGENTS 
carry_on = True	
def update(frame_number):
    
    fig.clear()   

    global carry_on
#for j in range (num_of_iterations):
#    print("iteration # = ", j)
    if carry_on:
        random.shuffle(agents)
#2.1 RANDOM WALK 'NUM_OF ITERATIONS' STEPS using move function        
        for i in range (num_of_agents):
            #move agent
            agents[i].move()
            #agent eat
            agents[i].eat()
            #agents share with neighbours
            agents[i].share_with_neighbours(neighbourhood)  
        #stop when each agent has 100
        full_tummy = 100
        totalstore = 0
        for j in range (num_of_agents):
            if(agents[i].store) > full_tummy:
                totalstore += agents[i].store
                print("total store = ", totalstore)    
        a = full_tummy*num_of_agents    
        if(totalstore > a):
            carry_on = False
            print("stopping condition")
    #plot a graph
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#3. GRAPHICS
#3.1 SCATTER PLOT
#animate sequence 
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=100)
animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
matplotlib.pyplot.show() 

#4. CALCUALTIONS 
#4.1 Distance between ech of the agents
for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b)      

#5. EXPORT
#5.1 Write out eaten environment to csv file 
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in agents[0].environment:
    writer.writerow(row)
f2.close()
#check
diff =[]
for i in range(len(environment)): # A list of rows
    for j in range(len(environment[i])): # A list of value
        diff.append(agents[0].environment[i][j]-environment[i][j]) #caluclate diff
#print(diff)
#matplotlib.pyplot.imshow(diff)
#print out eaten total
