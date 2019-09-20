# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:27:41 2019

@author: gyvi
"""
import random
class Agent():
    def __init__(self, environment, agents, y, x):
        self.y = random.randint(0,300)
        self.x = random.randint(0,300)
        self.environment = environment
        self.store = 0      
        self.agents = agents
        self.store = 0
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
    def eat(self):
        if self.environment[self.y][self.x] > 100:
            self.environment[self.y][self.x] -= 100
            self.store += 100
            
    def distance_between(self, agents_row_b):
        return (((self.x - agents_row_b.x)**2) +
                ((self.y - agents_row_b.y)**2))**0.5
                
    def share_with_neighbours(self, neighbourhood):
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:
                total = self.store + self.agents[i].store 
                average = total/2
                self.store = average
                self.agents[i].store = average