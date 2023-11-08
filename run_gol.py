from gameoflife import *
import time
import numpy as np
def main():
    rows = int(input("enter the rows--->"))
    cols = int(input("enter the columns--->"))
    grid=generate_universe(rows,cols,randomize = True)
    zero_grid = generate_universe(rows,cols,randomize = False)
    running = True
    while running:
        print('\033c')
        display = show_display(grid)
        print(display)
        time.sleep(0.7)
        next_grid = get_nextGeneration(grid)
        if grid == zero_grid or grid == next_grid:
            print('\033c')
            display = show_display(grid)
            print(display)
            running = False
        grid = next_grid
if __name__ == '__main__':
    main()
