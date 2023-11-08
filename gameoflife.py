import random
import numpy as np
def generate_random_universe(rows , cols, randomize=True):
    if randomize:
        universe = [[random.choice([0,1]) for i in range (cols)] for i in range(rows)]
    else:
        universe = []
        for i in range(rows):
            universe.append([0] * cols)
    return universe
    
def generate_universe(rows , cols,x_cordinates,y_cordinates):
    universe = []
    for i in range(rows):
        universe.append([0] * cols)
    run = len(x_cordinates)
    i=0
    while i<run:
        x=x_cordinates.pop()
        y=y_cordinates.pop()
        universe[x][y] = 1
        i+=1
    return universe
    
def get_neighbor(grid , x , y):
    neighbor =[]
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            x_neighbor = x+i
            y_neighbor = y+j
            if 0 <= x_neighbor < len(grid) and 0 <= y_neighbor < len(grid[0]):
                neighbor.append(grid[x_neighbor][y_neighbor])
    return neighbor

def get_nextGeneration(grid):
    new_generation=[]
    for i in range(len(grid)):
        new_generation.append([0] * len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbor = get_neighbor(grid,i,j)
            count = sum(neighbor)
            if grid[i][j]:
                if count in [2,3]:
                    new_generation[i][j] = 1
                else:
                    new_generation[i][j] = 0
            else:
                if count == 3:
                    new_generation[i][j] = 1
                else:
                    new_generation[i][j] =0
    return new_generation 
    

def show_display(grid):
    display = ""
    for row in grid:
        for col in row:
            if col == 1:
                display += " * "
            else:
                display += " - "
        display += '\n'
    return display
                



