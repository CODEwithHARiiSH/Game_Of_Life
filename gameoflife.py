def generate_universe(rows , cols):
    universe = []
    for i in range(rows):
        universe.append([0] * cols)
    return universe
    
def get_neighbor(grid , x , y):
    return [0,0,0,0,0,0,0,1]

    



