from gameoflife import *

def test_generate_universe():
    rows = 3
    cols = 3
    assert generate_universe(rows , cols) == [[0,0,0] , [0,0,0] , [0,0,0]]
    
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
    grid = [[1,0,0] , 
            [0,1,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[0,1,0] , 
                                        [1,0,0] , 
                                        [0,0,0]]
    
def test_get_nextGeneration_case2():
    grid = [[1,1,0] , 
            [1,0,0] , 
            [0,0,0]]
    assert get_nextGeneration(grid) == [[1,1,0] , 
                                        [1,0,0] , 
                                        [0,0,1]]
       
def test_get_nextGeneration_case3():
    grid = [[1,0,1] , 
            [1,1,0] , 
            [0,0,1]]
    assert get_nextGeneration(grid) == [[1,0,0] , 
                                        [1,0,0] , 
                                        [0,0,0]]
       

def test_get_nextGeneration_case4():
    grid = [[1,0,1] , 
            [1,0,0] , 
            [1,1,0]]
    assert get_nextGeneration(grid) == [[0,0,0] , 
                                        [1,1,1] , 
                                        [1,1,0]]
                                        
                                        
def test_show_display():
    grid = [[1,1,1] , 
            [0,0,0] , 
            [1,0,1]]
            
    assert show_display(grid) == """ *  *  * 
 -  -  - 
 *  -  * 
"""






   
