from gameoflife import *

def test_generate_universe():
    rows = 3
    cols = 3
    assert generate_universe(rows , cols) == [[0,0,0] , [0,0,0] , [0,0,0]]
    
def test_get_neighbour():
    grid = [[1,0,1] , 
            [0,1,0] , 
            [1,2,3]]
    x_cordinate = 0
    y_cordinate = 0
    assert get_neighbour(grid , x_cordinate , y_cordinate) == [0,0,0,0,0,0,1]
    

    

    
