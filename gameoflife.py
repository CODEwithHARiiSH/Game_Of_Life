def generate_universe(rows , cols):
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
            if 0 <= (x+i) < len(grid) and 0 <= (y+j) < len(grid[0]):
                neighbor.append(grid[x+i][y+j])
    return neighbor

def get_nextGeneration(grid):
    new_generation=[]
    for i in range(len(grid)):
        new_generation.append([0] * len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbor = get_neighbor(grid,i,j)
            count = sum(neighbor)
            if grid[i][j] == 1:
                if count < 2:
                    new_generation[i][j] = 0
                else:
                    new_generation[i][j] = 1
    return new_generation 



