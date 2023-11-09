import random
import os
def generate_universe(rows , cols, randomize=True):
    if randomize:
        universe = [[random.choice([0,1]) for i in range (cols)] for i in range(rows)]
    else:
        universe = []
        for i in range(rows):
            universe.append([0] * cols)
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
    alive = " ■ "
    dead = " ▢ "
    alive_clr = "\033[31m"
    dead_clr = "\033[31m"
    for row in grid:
        for col in row:
            if col == 1:
                display += alive_clr + alive 
            else:
                display += dead_clr + dead 
        display += '\n'
    os.system("clear")
    print(display)
    return display
                

def get_user_input(rows,cols):
    grid = generate_universe(rows , cols,randomize=False)
    show_display(grid)
    
    x, y = 0, 0  # Initial cursor position
    
    while True:
        show_display(grid)
        print("Instructions:")
        print("--------------------------------------")
        print("Press 'q' to quit")
        print("Use arrow keys to navigate the grid.")
        print("Press 'space' to toggle cell state.")
        print("--------------------------------------")
        key = input("Enter a command: ")
        if key == "q":
            print("Exiting the program.")
            break
        elif key == " ":
            # Toggele between alive and dead
            grid[y][x] = 1 if grid[y][x] == 0 else 0
            # Navigation
        elif key == "\x1b[A":  
            y = max(0, y - 1)
        elif key == "\x1b[B": 
            y = min(rows - 1, y + 1)
        elif key == "\x1b[C":  
            x = min(rows - 1, x + 1)
        elif key == "\x1b[D": 
            x = max(0, x - 1)
    return grid




































