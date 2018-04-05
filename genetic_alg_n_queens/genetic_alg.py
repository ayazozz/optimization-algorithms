# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:24:57 2018

@author: safiye ayazoz
"""

import createPopulation
import math
import random

board_size = 8

populationBoards = []

begin_population_size = 10

population_size = 8

fitnessValues = []

parentsIndex = []



def compute_fitness( parentBoard ):

        ''' computes fitness of current board

        bigger number is better'''

        fitness = goal

        for i in range(board_size):

            for j in range(i+1, board_size):

                if math.fabs(parentBoard[i] - parentBoard[j]) == j - i :

                    # for each queen guarding another one reduce fitness by 1

                    fitness-=1    
                    
        return fitness   
    
def isFindFitnessValue(size):

     for board in range(size):

            if (fitnessValues[board] == goal) :
              
                 return True

     return False
    
def findBestSolution(populationBoards):
    
    generationSize = 0    
    
    if isFindFitnessValue(begin_population_size)== True:     
       
       print("***OPTIMUM POPULATION***\n")
       
       createPopulation.printPopulation(populationBoards,begin_population_size)
       
    else:  
       
       #to select 8 boards with the best fitness value
       newPopulationBoards = selectOptPopulationRange(populationBoards)
       #createPopulation.printPopulation(newPopulationBoards , board_size);
       
       while True:
           
            generationSize += 1
            
            global fitnessValues
            
            print ("generation size : ", generationSize)
            
            newPopulationBoards = crossOver(newPopulationBoards)
 
            fitnessValues.clear()
            
            for n in range(population_size):                
                fitnessValues.append(compute_fitness(newPopulationBoards[n]))
                
            
            #to sort new generation (added child) 
            newPopulationBoards = sortNewPopulation(newPopulationBoards) 
            
            print("\n** NEW POPULATION **\n")
            
            createPopulation.printPopulation(newPopulationBoards, board_size)
            
                     
            if(isFindFitnessValue(population_size)== True):     
       
               print("***OPTIMUM POPULATION***\n")
       
               createPopulation.printPopulation(newPopulationBoards, population_size)
               
               createPopulation.optimumBoard(newPopulationBoards[0])
               
               break
           
def sortNewPopulation(oldPopulation):
    
     global fitnessValues 
     
     population_list = [] 
     
     newPopulation = []
     
     for  i in range(population_size):

            population_list.append((i, fitnessValues[i]))
            
            population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
            
     for j in range(len(population_list)):
            
            newPopulation.append(oldPopulation[population_list[j][0]])
            fitnessValues[j]= population_list[j][1]
                   
       
     return newPopulation
 
def rouletteSelection(newPopulationBoards):
    
  
    sumFitnessValue = 0
    tempSumFitnessValue = 0
    selectedBoard = 0 
   
    global parentsIndex
    
    for board in range(len(newPopulationBoards)):
        
         sumFitnessValue += fitnessValues[board]
         
    #  r is like a virtual ball  
    r = random.randint(0, (sumFitnessValue-1))  
    
   
    # the total fitness value of the population exceeds x and the board is selected
    for i in range(len(fitnessValues)):
        
        tempSumFitnessValue +=fitnessValues[i]
       
        if(tempSumFitnessValue >= r):
           selectedBoard = newPopulationBoards[i]
           parentsIndex.append(i)
           return selectedBoard


def selectOptPopulationRange(populationBoards):
        
        global fitnessValues       
        
        population_list = []
        
        newPopulationBoard = []

        for  i in range(begin_population_size):

            population_list.append((i, fitnessValues[i]))
            
            population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
            
        population_list =  population_list[:-2]   
        
        fitnessValues = fitnessValues[:-2]  

        for j in range(len(population_list)):
            
            newPopulationBoard.append(populationBoards[population_list[j][0]])
            fitnessValues[j]= population_list[j][1]
                    
        return newPopulationBoard

def crossOver (population):
    
       goal = int((board_size*(board_size-1))/2)
       parent = []
       
       mutation_probability = 0.025
        
       #choose parents 
       parent.append(rouletteSelection(population))
    
       parent.append(rouletteSelection(population))  
       
       #createPopulation.printPopulation(parent,2)
       
       #it is decided which parent and which chromosome will start
       begin_gene=random.randint(0, board_size-1)             
       begin_parent_no= random.randint(0,1)
  
       #begin cross over
       
       child = []
       block_gene_count = board_size/2 # the child will receive half of every parent
       firstBlockParent=[]
       secondBlockParent =[]
       
       childSize = 0       
       index = 0 
       isFind = True    
      
       
       for i in range(2):
           if(begin_parent_no==i):
               firstBlockParent = parent[i]
           else:
               secondBlockParent= parent[i]
               
      
       if(begin_gene>board_size/2): # if the initial value is in the second half of the parent's genes
           
           diff = board_size-begin_gene
                    
           while(begin_gene < board_size):
               child.append(firstBlockParent[begin_gene])
               begin_gene +=1
               childSize +=1
           
          
           
           while (diff<block_gene_count):
               child.append(firstBlockParent[index])
               index +=1
               childSize +=1
               diff +=1
               
       else:
           for i in range(int(block_gene_count)):
               child.append(firstBlockParent[begin_gene])
               begin_gene +=1
               childSize +=1

                 
        
       for i in range(board_size): # genes that are not in the child are taken from the second mother
                
          for j in range(childSize):

                if(secondBlockParent[i] == child[j]):      
                       isFind = True
                       break                       
                else:
                       isFind = False
          if(isFind == False):        
                child.append(secondBlockParent[i])
                childSize +=1
                   
       child_fitness = compute_fitness(child)
       #print("FITNESS_CHILD : "+str(child_fitness))
   
       # for mutate
       if(child_fitness!=goal):
          if random.random() < mutation_probability:
            child = mutate(child)
            child_fitness = compute_fitness(child)
              
         
       if(child_fitness > fitnessValues[population_size-1]):
           population[population_size-1] = child
           
       return population    


def mutate(child):
    
        rGeneIndex= random.randint(0, board_size-1)      
        rGeneValue = random.randint(0, board_size-1)  
        currentGeneValue = child[rGeneIndex]
        
        for i in range(board_size):
            if child[i]==rGeneValue :
                child[i] =currentGeneValue
                child[rGeneIndex]=rGeneValue 
       
        return child    
            
if __name__ == '__main__':
    
    goal = int((board_size*(board_size-1))/2)
    
    #First Generation population_size =10
    createPopulation.createPopulationBoards(populationBoards)
    
    createPopulation.printPopulation(populationBoards , begin_population_size)   
    
      #compute first population fitness Value
    for n in range(begin_population_size):  
            fitnessValues.append(compute_fitness(populationBoards[n]))
           
            
            
    findBestSolution(populationBoards)  

             