from gameoflife import *
import time
def main():
    rows = 20
    cols = 20
    zero_grid = generate_universe(rows,cols,randomize = False)
    grid=generate_universe(rows,cols,randomize = True)
    running = True
    while running:
        show_display(grid)
        time.sleep(0.7)
        next_grid = get_nextGeneration(grid)
        if grid == zero_grid:
            show_display(grid)
            running = False
        grid = next_grid
if __name__ == '__main__':
    main()
