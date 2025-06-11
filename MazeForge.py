import pygame
from pygame.locals import *
import sys

class PyMaze:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = 480
        self.width = 640
        self.screen = None
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.start_button_rect = None
        self.end_button_rect = None
        self.state = 'menu'
    def invoke_game(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MazeForge')
        
        game_begin = True
        while game_begin:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_begin = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect and self.start_button_rect.collidepoint(event.pos):
                        self.state = 'game'     
                    elif self.end_button_rect and self.end_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            if self.state =='menu':
                self.welcome_to_glitch_grid()
            elif self.state=='game':
                self.create_box()
            pygame.display.flip()
            self.fpsClock.tick(self.fps)
        pygame.quit()

    def welcome_to_glitch_grid(self):
        try:
            image = pygame.image.load('assets/welcome.png').convert()
            image = pygame.transform.scale(image,(self.width,self.height))
        except pygame.error:
            image = pygame.Surface((self.width, self.height))
            image.fill((0, 0, 0))
        self.screen.blit(image, (0, 0))

        start_button_image = pygame.image.load('assets/start.png').convert_alpha()
        start_button_image = pygame.transform.scale(start_button_image, (100, 100))
        button_rect = start_button_image.get_rect(center=(self.width // 2-100, self.height //2))
        self.screen.blit(start_button_image, button_rect)
        self.start_button_rect = button_rect

        end_button_image = pygame.image.load('assets/quit.png').convert_alpha()
        end_button_image = pygame.transform.scale(end_button_image, (100, 100))
        button_rect = end_button_image.get_rect(center=(self.width // 2+100, self.height //2))
        self.screen.blit(end_button_image, button_rect)

        self.end_button_rect = button_rect


    def create_box(self):
        
        rows = columns =  len(self.matrix)
        cell_size = 25
        margin = 5
        maze_width = columns * (cell_size + margin)
        maze_height = rows * (cell_size + margin)
        try:
            image = pygame.image.load('assets/background.png').convert()
            image = pygame.transform.scale(image,(self.width,self.height))
        except pygame.error:
            image = pygame.Surface((self.width, self.height))
            image.fill((0, 0, 0))
        self.screen.blit(image, (0, 0))
        x_offset = (self.width - maze_width) // 2
        y_offset = (self.height - maze_height) // 2
        for row in range(rows):
            for cols in range(columns):
                x = x_offset + cols*(cell_size+margin)
                y = y_offset + row*(cell_size+margin)
                if self.matrix[row][cols] == '1':
                    color = (255, 255, 255)      
                elif self.matrix[row][cols] == 'x':
                    color = (255, 0, 0)      
                elif self.matrix[row][cols] == 'y':
                    color = (0, 255, 0)     
                else:
                    color = (0, 50, 50) 
                    
                pygame.draw.rect(self.screen, color, [x, y, cell_size, cell_size])
        