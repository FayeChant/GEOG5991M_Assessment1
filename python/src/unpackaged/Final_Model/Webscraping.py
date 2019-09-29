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
