#0 SETUP ACTIVITIES
#0.1 IMPORT REQUIRED MODULES
import random

#CREATE AGENT CLASS
class Agent ():
#SET ENVIRONMENT VARIABLE, AND STORE VARIABLE, DEFINE START LOCATION USING RANDOM INTEGER BETWEEN 0 AND 99
    def __init__ (self, environment):
        self.environment = environment
        self.store = 0 
        self._x = random.randint(0,99)  
        self._y = random.randint(0,99)
#PROTECT X AND Y COORDINATES    
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property")                   
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property")
#DEFINE MOVE FUNCTION    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100   
#DEFINE EAT FUNCTION    
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 10
