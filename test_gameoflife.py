from gameoflife import *

def test_generate_universe():
    rows = 3
    cols = 3
    assert generate_random_universe(rows , cols,randomize=False) == [[0,0,0] , [0,0,0] , [0,0,0]]
    
def test_generate_universe_random():
    rows = 3
    cols = 3
    universe = generate_random_universe(rows , cols,randomize=True)
    assert len(universe) == 3
    assert len(universe[0])== 3
    
def test_generate_universe_byUser():
    rows = 3
    cols = 3
    x_cordinates = [1,2,0]
    y_cordinates = [1,2,0]
    assert generate_universe(rows,cols,x_cordinates,y_cordinates) == [[1,0,0] , 
                                                                    [0,1,0] , 
                                                                    [0,0,1]]
    
def test_get_neighbor():
    grid = [[1,0,0] , 
            [0,1,0] , 
            [0,0,0]]
    x_cordinate = 0
    y_cordinate = 0
    assert get_neighbor(grid , x_cordinate , y_cordinate) == [0,0,1]
    
    grid = [[1,0,1] , 
            [0,1,0] , 
            [1,2,3]]
    x_cordinate = 1
    y_cordinate = 1
    assert get_neighbor(grid , x_cordinate , y_cordinate) == [1,0,1,0,0,1,2,3]
    
def test_get_nextGeneration_case1():
    grid = [[0,0,0] , 
            [0,1,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[0,0,0] , 
                                        [0,0,0] , 
                                        [0,0,0]]
    
def test_get_nextGeneration_case2():
    grid = [[1,1,0] , 
            [1,0,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[1,1,0] , 
                                        [1,1,0] , 
                                        [0,0,0]]
       
def test_get_nextGeneration_case3():
    grid = [[1,0,0] , 
            [0,0,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[0,0,0] , 
                                        [0,0,0] , 
                                        [0,0,0]]
       

def test_get_nextGeneration_case4():
    grid = [[1,0,1] , 
            [1,0,0] , 
            [1,1,0]]
    assert get_nextGeneration(grid) == [[0,1,0] , 
                                        [1,0,0] , 
                                        [1,1,0]]

def test_get_nextGeneration_Alldead():
    grid = [[0,0,0] , 
            [0,0,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[0,0,0] , 
                                        [0,0,0] , 
                                        [0,0,0]]                                        
                                        
def test_show_display():
    grid = [[1,1,1] , 
            [0,0,0] , 
            [1,0,1]]
            
    assert show_display(grid) == """ *  *  * 
 -  -  - 
 *  -  * 
"""

    grid = [[1,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0],
            [1,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0],
            [1,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

    assert show_display(grid) == """ *  -  *  -  -  -  -  - 
 -  -  -  -  -  -  -  - 
 *  *  *  *  *  *  *  * 
 *  -  *  -  *  -  *  - 
 *  -  *  -  -  -  -  - 
 -  -  -  -  -  -  -  - 
 *  *  *  *  *  *  *  * 
 *  -  *  -  *  -  *  - 
 *  -  *  -  -  -  -  - 
 -  -  -  -  -  -  -  - 
"""













   
