import pygame
from pygame.locals import *
import sys

class PyMaze:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = 600
        self.width = 1024
        self.screen = None
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.start_button_rect = None
        self.end_button_rect = None
        self.state = 'menu'
        self.cell_size = 30
        self.margin = 5
        self.loc = []
    def invoke_game(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MazeForge')
        try:
            icon = pygame.image.load('assets/icon.png').convert_alpha()
            pygame.display.set_icon(icon)
            pygame.display.set_caption('MazeForge')
        except Exception as e:
            print('Using default icon:', e)
        
        game_begin = True
        while game_begin:
            pygame.time.delay(10)
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
                self.loc.clear()
                self.create_box()
                self.key_movement()
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
        rows = columns = len(self.matrix)
        maze_width = columns * (self.cell_size + self.margin)
        maze_height = rows * (self.cell_size + self.margin)

        try:
            background = pygame.image.load('assets/background.png').convert()
            background = pygame.transform.scale(background, (self.width, self.height))
        except pygame.error:
            background = pygame.Surface((self.width, self.height))
            background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))

        x_offset = (self.width - maze_width) // 2
        y_offset = (self.height - maze_height) // 2

        for row in range(rows):
            for cols in range(columns):
                x = x_offset + cols * (self.cell_size + self.margin)
                y = y_offset + row * (self.cell_size + self.margin)
                self.loc.append((x,y))
                cell_value = self.matrix[row][cols]

                if cell_value == '1':
                    self.insert_image_in_maze('assets/wall.png',x,y)
                elif cell_value == '0':
                    self.insert_image_in_maze('assets/path.png',x,y)
                elif cell_value == 'x':
                    self.insert_image_in_maze('assets/jerry.png',x,y)
                else:
                    if cell_value == 'y':
                        color = (0, 255, 0)
                    else:
                        color = (0, 50, 50)

                    pygame.draw.rect(self.screen, color, [x, y, self.cell_size, self.cell_size])


    def insert_image_in_maze(self, image_path,x,y):
        wall = pygame.image.load(image_path).convert_alpha()
        wall = pygame.transform.scale(wall, (self.cell_size, self.cell_size))
        self.screen.blit(wall, (x, y))
    

    def key_movement(self):
        keys = pygame.key.get_pressed()
        start,end = self.loc[0][0],self.loc[0][1]

        if keys[pygame.K_LEFT]: 
            start+=1
        if keys[pygame.K_RIGHT]: 
            start+=1    
        if keys[pygame.K_UP]: 
            end-= 1     
        if keys[pygame.K_DOWN]: 
            end+= 1
        self.insert_image_in_maze('assets/jerry.png',start,end)
        pygame.display.update()