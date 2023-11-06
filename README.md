Game_Of_Life

Game of life consists of a grid of cells . I will call it as an universe.

Rules

A living cell will survive into the next generation by default, unless:
1. it has fewer than two live neighbours (underpopulation).
2. it has more than three live neighbours (overpopulation).
A dead cell will spring to life if it has exactly three live neighbours (reproduction).


Implementation

1. Intilize an empty universe.
2. Set cells in the universe.
3. Determine if a given cell survives to the next iteration, based on its neighbours.
4. Iterate the function.
5. Iterate steps 3–4 for the desired number of generations.
