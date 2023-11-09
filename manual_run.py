from gameoflife import *
import time

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

def main():
    rows = 20
    cols = 20
    zero_grid = generate_universe(rows,cols,randomize = False)
    grid = get_user_input(rows , cols)
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
