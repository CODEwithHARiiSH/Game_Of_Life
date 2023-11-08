from gameoflife import *
import time
import numpy as np
def main():
    rows = 20
    cols = 20
    grid=generate_universe(rows,cols,randomize = True)
    zero_grid = generate_universe(rows,cols,randomize = False)
    running = True
    while running:
        show_display(grid)
        time.sleep(0.7)
        next_grid = get_nextGeneration(grid)
        if grid == zero_grid or grid == next_grid:
            show_display(grid)
            running = False
        grid = next_grid
if __name__ == '__main__':
    main()
