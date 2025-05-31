import pygame
from pygame.locals import *
import sys

class PyMaze:
    def __init__(self, matrix):
        self.matrix = matrix

    def invoke_game(self):
        pygame.init()
        
        fps = 60
        fpsClock = pygame.time.Clock()
        
        cell_size = 40
        margin = 5
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        width = cols * (cell_size + margin)
        height = rows * (cell_size + margin)
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("PyMaze")

        while True:
            screen.fill((0, 0, 0)) 
            for i in range(rows):
                for j in range(cols):
                    x = j * (cell_size + margin)
                    y = i * (cell_size + margin)

                    if self.matrix[i][j] == '1':
                        color = (0, 0, 255)      
                    elif self.matrix[i][j] == 'x':
                        color = (255, 0, 0)      
                    elif self.matrix[i][j] == 'y':
                        color = (0, 255, 0)     
                    else:
                        color = (0, 50, 50) 
                    
                    pygame.draw.rect(screen, color, [x, y, cell_size, cell_size])
            
            pygame.display.flip()
            fpsClock.tick(fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()