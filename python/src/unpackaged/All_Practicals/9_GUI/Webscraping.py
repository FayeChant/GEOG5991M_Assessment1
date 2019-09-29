"""
Created on Thu Sep 26 15:27:33 2019

@author: Faye
"""
#0 SETUP ACTIVITIES
#IMPORT REQUIRED MODULES
import random
import operator
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import agentframework4 as agentframework
import csv
import matplotlib.animation 
import tkinter
import requests
import bs4

#0.1 Web scraping
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html') 
content = r.text 

soup = bs4.BeautifulSoup(content, 'html.parser')
tdsX = soup.find_all(attrs={"class" : "x"})
tdsY = soup.find_all(attrs={"class" : "y"})
tdsZ = soup.find_all(attrs={"class" : "z"})

for td in tdsX:
    print(td.text)
for td in tdsY:
    print(td.text)
for td in tdsZ:
    print(td.text)
