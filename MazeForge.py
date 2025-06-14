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
        self.mov_row = 0
        self.mov_col = 0
        self.assets = None
    def invoke_game(self):
        pygame.init()
        

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MazeForge')
        self.assets = {
        'wall': pygame.transform.scale(pygame.image.load('assets/wall.png').convert_alpha(), (self.cell_size, self.cell_size)),
        'path': pygame.transform.scale(pygame.image.load('assets/path.png').convert_alpha(), (self.cell_size, self.cell_size)),
        'jerry': pygame.transform.scale(pygame.image.load('assets/jerry.png').convert_alpha(), (self.cell_size, self.cell_size)),
        'icon': pygame.image.load('assets/icon.png').convert_alpha()
        }
        try:
            pygame.display.set_icon(self.assets['icon'])
            pygame.display.set_caption('MazeForge')
        except Exception as e:
            print('Using default icon:', e)
        
        game_begin = True
        while game_begin:
            # pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_begin = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect and self.start_button_rect.collidepoint(event.pos):
                        self.state = 'maze_create'     
                    elif self.end_button_rect and self.end_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type ==pygame.KEYDOWN:
                    if self.state=='game':
                        self.key_movement(event.key)
            if self.state =='menu':
                self.welcome_to_glitch_grid()
            elif self.state=='maze_create':
                self.create_box()
                self.create_timer()
                self.state='game'
                
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
                cell_value = self.matrix[row][cols]

                if cell_value == '1':
                    self.screen.blit(self.assets['wall'], (x, y))
                elif cell_value == '0':
                    self.screen.blit(self.assets['path'], (x, y))
                elif cell_value == 'x':
                    self.screen.blit(self.assets['jerry'], (x, y))
                else:
                    if cell_value == 'y':
                        color = (0, 255, 0)
                    else:
                        color = (0, 50, 50)

                    pygame.draw.rect(self.screen, color, [x, y, self.cell_size, self.cell_size])

    def key_movement(self,key):
        new_row, new_col = self.mov_row,self.mov_col
        if key==pygame.K_LEFT: 
            new_col-=1
        if key==pygame.K_RIGHT: 
            new_col+=1    
        if key==pygame.K_UP: 
            new_row-=1     
        if key==pygame.K_DOWN: 
            new_row+=1
        
        
        if 0<=new_row<=len(self.matrix) and 0<=new_col<len(self.matrix):
            if self.matrix[new_row][new_col]!='1':
                self.matrix[self.mov_row][self.mov_col]='0'
                self.redraw_visted_cell(self.mov_row, self.mov_col)
                self.mov_row,self.mov_col = new_row,new_col
                self.matrix[self.mov_row][self.mov_col]='x'
                self.redraw_visted_cell(self.mov_row,self.mov_col)
        if new_row==len(self.matrix)-1 and new_col==len(self.matrix)-1:
            pass

    
    
    def redraw_visted_cell(self, row, col):
        x_offset = (self.width - len(self.matrix[0]) * (self.cell_size + self.margin)) // 2
        y_offset = (self.height - len(self.matrix) * (self.cell_size + self.margin)) // 2

        x = x_offset + col * (self.cell_size + self.margin)
        y = y_offset + row * (self.cell_size + self.margin)

        cell_value = self.matrix[row][col]

        if cell_value == '1':
            self.screen.blit(self.assets['wall'], (x, y))
        elif cell_value == '0':
            self.screen.blit(self.assets['path'], (x, y))
        elif cell_value == 'x':
            self.screen.blit(self.assets['jerry'], (x, y))
        elif cell_value == 'y':
            pygame.draw.rect(self.screen, (0, 255, 0), [x, y, self.cell_size, self.cell_size])
        else:
            pygame.draw.rect(self.screen, (0, 50, 50), [x, y, self.cell_size, self.cell_size])


        
    

        
        
        