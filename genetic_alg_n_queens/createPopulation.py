# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:15:39 2018

@author: safiye ayazoz
"""

import random


board_size = 8

populationBoards = []

begin_population_size = 10



def createPopulationBoards(populationBoards):
    
     for i in range(begin_population_size):
        
        parent = []
        
        for j in range(board_size):
            
            parent.append(j)
            
        for n in range(board_size):   
            
             r = random.randint(0, 7)
             
             temp = parent[n]
             
             parent[n] = parent[r]
             
             parent [r] =temp
                
        populationBoards.append(parent) 
        
def printPopulation(populationBoards ,size): 

    for i in range(size):   
       print(populationBoards[i])
        
    print("\n") 

def optimumBoard(board):
    
    for i in range(board_size):
        for j in range(board_size):
            
            if(board[i]==j):
                print(" Q" , end="")
            else:print(" ■",end="")           
    
        print("")
    
    
    
    
    
    