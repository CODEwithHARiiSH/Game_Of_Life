import curses
from gameoflife import *
import time

# Manual Initializing the grid
message = """Press ENTER to generate
Press ESC to exit
"""
def display_matrix(win, matrix):
    ALIVE = "■"
    DEAD = "□"
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                win.addch(i, j * 2, DEAD)  # Display dead cells
            elif value == 1:
                win.addch(i, j * 2, ALIVE)  # Display alive cells

    win.addstr(len(matrix) + 1, 0, message)


def toggle_cell_state(matrix, row, col):
    if matrix[row][col] == 0:
        matrix[row][col] = 1
    elif matrix[row][col] == 1:
        matrix[row][col] = 0


def manual(stdscr):
    rows = 20
    cols = 20
    matrix = generate_universe(rows,cols,randomize = False)
    curses.curs_set(0)
    stdscr.keypad(1)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    while True:
        stdscr.clear()
        display_matrix(stdscr, matrix)
        stdscr.refresh()

        key = stdscr.getch()
        if key == 27:  # Exit on 'Esc' key
            break
        elif (
            key == curses.KEY_ENTER or key == 10 or key == 13):  # Generate matrix on 'Enter' key
            stdscr.clear()
            matrix = get_nextGeneration(matrix)
            stdscr.addstr(len(matrix) + 1, 0, message)
            stdscr.refresh()
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            row, col = my, mx // 2  # Convert mouse coordinates to matrix coordinates
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
                toggle_cell_state(matrix, row, col)

#Auto intializing the grid

def autorun():
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
print("\n")
print("MODES")
print("-----------------------")
print("\n")
print(" press 1 for auto mode ")
print("-----------------------")
print("\n")
print(" press 2 for manual mode ")
print("-----------------------")
print("\n")

mode = int(input("choose mode---> "))

if mode == 1:
    if __name__ == "__main__":
        autorun()
elif mode == 2:
    if __name__ == "__main__":
        curses.wrapper(manual)












