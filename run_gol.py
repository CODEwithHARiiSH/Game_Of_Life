from gameoflife import *

def main():
    rows = 10
    cols = 10
    grid=generate_universe(rows,cols,randomize=True)

    print(grid)
    display=show_display(grid)
    print(display)
    while True:
        if all(cell == 0 for row in grid for cell in row):
            break
        grid = get_nextGeneration(grid)
        display = show_display(grid)
        print(display)



if __name__ == '__main__':
    main()
