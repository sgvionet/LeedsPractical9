# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:08 2019

@author: gyvi
"""
import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

f = open("in.txt", "r")
reader = csv.reader(f)
environment = []

for line in f:
    rowlist = []
    line_split = line.split(',')
    for value in line_split:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()


num_of_agents = 50
neighbourhood = 20
agents = []

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

fig = matplotlib.pyplot.figure(figsize=(7, 7))

carry_on = True
       
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    matplotlib.pyplot.xlim(0,300)
    matplotlib.pyplot.ylim(0,300)
    
    matplotlib.pyplot.imshow(environment)
    
    random.shuffle(agents)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'black')
        
            
    if random.random() < 0.001:
        carry_on = False
        print("random stopping condition")
        
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on):
        yield a			
        a = a + 1
  

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def quit():
    global root
    root.destroy()  
    
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Quit model", command=quit)


tkinter.mainloop()




