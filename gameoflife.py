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
            neighbor.append(grid[x+i][y+j])
    return neighbor

    



