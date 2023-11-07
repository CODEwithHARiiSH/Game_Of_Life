from gameoflife import *
import pygame

def get_pygame():
    rows = 30
    cols = 30
    window_height = rows*cols
    window_width = rows*cols
    background = [255,255,255]
    alive = [255,255,0]
    
    pygame.init()
    
    window = pygame.display.set_mode((window_height , window_width)) #setting the window
    pygame.display.set_caption("Game of life")
    grid = generate_universe(rows,cols,randomize=True)
    
    #for creating the window and alive, just like we created the show_display function
    def drawgrid():
        window.fill(background)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    pygame.draw.rect(window,alive,(i*cols,j*cols,cols,cols))
    
    running = True
    clock = pygame.time.Clock()
    
    #If you put the grid is inside the loop, so on every time the grid will change. It will be a endless loop.
    #You can put grid outside the loop so it will automatically stop.
    #Clock.tick() is for timing if it stops move curser.
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            drawgrid()
            pygame.display.flip()
        
            grid=get_nextGeneration(grid)
            clock.tick(7)
    pygame.quit()

if __name__ == '__main__':
    get_pygame()

