# -*- coding: utf-8 -*-
#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random

#1. SET UP AGENT 1 
#1.1 START LOCATION - assigned coordinates using a random grid of 100 by 100
y0 = int (random.random()*100)
x0 = int (random.random()*100)
#could also use - y0 = randon.randint(0,99)
#test that this has worked
#print (x0)
#print (y0)

#2. MOVE AGENT 1 
#2.1 Random walk one step
#change y0
if random.random () <0.5 :
    y0 += 1
else:
    y0 -= 1
#change x0
if random.random () <0.5 :
    x0 += 1
else:
    x0 -= 1
#2.2 Random walk second step    
#change y0
if random.random () <0.5 :
    y0 += 1
else:
    y0 -= 1
#change x0
if random.random () <0.5 :
    x0 += 1
else:
    x0 -= 1
    
#3. SET UP AGENT 2 
#3.1 START LOCATION
y1 = int (random.random()*100)
x1 = int (random.random()*100)
#test this has worked
#print (x1)
#print (y1)

#4. MOVE AGENT 2
#4.1 Random walk one step
#change y1
if random.random () <0.5 :
    y1 += 1
else:
    y1 -= 1
#change x1
if random.random () <0.5 :
    x1 += 1
else:
    x1 -= 1
#4.2 Random walk second step
#change y1
if random.random () <0.5 :
    y1 += 1
else:
    y1 -= 1
#change x1
if random.random () <0.5 :
    x0 += 1
else:
    x1 -= 1

#5.PRINT FINAL COORDINATES    
print (y0, x0, y1, x1)

#6. CALCUALTIONS 
#6.1 DISTANCE BETWEEN THE TWO AGENTS
dist = (((y1-y0)**2)+((x1-x0)**2))**0.5
print (dist)