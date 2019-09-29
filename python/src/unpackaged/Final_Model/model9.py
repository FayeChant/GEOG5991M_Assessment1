"""Stereoheighting data preparation tool.
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

# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#IMPORT REQUIRED MODULES
import random
import operator
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import agentframework5 as agentframework
import csv
import matplotlib.animation 
import tkinter
import requests
import bs4

#0.1 Web scraping
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html') 
content = r.text 
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
print(td_xs)
print(td_ys)

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
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
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
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=100)

#GUI
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
    canvas.draw() 
root = tkinter.Tk() 
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() 

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
