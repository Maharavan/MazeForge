import pygame
from pygame.locals import *
import sys
import time
from HighScoreDB import HighScore
class MazeForge:
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
        self.cell_size = 35
        self.margin = 5
        self.music_played = False
        self.mov_row = 0
        self.mov_col = 0
        self.start_time = None
        self.gameover = False
        
    def invoke_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MazeForge')
        self.assets_generator()
        
        try:
            pygame.display.set_icon(self.assets['icon'])
            pygame.display.set_caption('MazeForge')
        except Exception as e:
            print('Using default icon:', e)
        
        game_begin = True
        while game_begin:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_begin = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect and self.start_button_rect.collidepoint(event.pos):
                        self.state = 'maze_create'
                        pygame.mixer_music.stop()  
                        self.music_played = False
                    elif self.end_button_rect and self.end_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type ==pygame.KEYDOWN:
                    if self.state=='game':
                        self.music_enabler('assets/sound/game-begins.mp3')
                        self.key_movement(event.key)
            if self.state =='menu':
                self.welcome_to_glitch_grid()
            elif self.state=='maze_create':
                self.create_box()  
                self.start_time = time.time()
                self.state='game'
            elif self.mov_row==len(self.matrix)-1 and self.mov_col==len(self.matrix)-1:
                self.game_over()
                self.state='game_over'
            pygame.display.flip()
            self.fpsClock.tick(self.fps)
        pygame.quit()

    def welcome_to_glitch_grid(self):
        
        self.music_enabler("assets/sound/game-intro.mp3")
        self.screen.blit(self.assets['welcome'], (0, 0))
        

        button_rect = self.assets['start_button'].get_rect(center=(self.width // 2-100, self.height //2))
        self.screen.blit(self.assets['start_button'], button_rect)
        self.start_button_rect = button_rect

        button_rect = self.assets['end_button'].get_rect(center=(self.width // 2+100, self.height //2))
        self.screen.blit(self.assets['end_button'], button_rect)

        self.end_button_rect = button_rect

    def assets_generator(self):
        self.assets = {
            'wall': pygame.transform.scale(pygame.image.load('assets/images/wall.png').convert_alpha(), (self.cell_size, self.cell_size)),
            'path': pygame.transform.scale(pygame.image.load('assets/images/path.png').convert_alpha(), (self.cell_size, self.cell_size)),
            'jerry': pygame.transform.scale(pygame.image.load('assets/images/jerry.png').convert_alpha(), (self.cell_size, self.cell_size)),
            'cheese': pygame.transform.scale(pygame.image.load('assets/images/cheese.png').convert_alpha(), (self.cell_size, self.cell_size)),
            'icon': pygame.image.load('assets/images/icon.png').convert_alpha(),
            'gameover':pygame.transform.scale(pygame.image.load('assets/images/gameover.png').convert(),(self.width,self.height)),
            'background':pygame.transform.scale(pygame.image.load('assets/images/background.png').convert(),(self.width,self.height)),
            'welcome':pygame.transform.scale(pygame.image.load('assets/images/welcome.png').convert(),(self.width,self.height)),    
            'gameover':pygame.transform.scale(pygame.image.load('assets/images/gameover.png').convert_alpha(),(400,400)),
            'highscore':pygame.transform.scale(pygame.image.load('assets/images/highscore.png').convert_alpha(),(300,300)),
            'currentscore':pygame.transform.scale(pygame.image.load('assets/images/score.png').convert_alpha(),(300,300)),
            'start_button':pygame.transform.scale(pygame.image.load('assets/images/start.png').convert_alpha(), (100, 100)),
            'end_button':pygame.transform.scale(pygame.image.load('assets/images/quit.png').convert_alpha(), (100, 100))
        }

    def create_box(self):
        rows = columns = len(self.matrix)
        maze_width = columns * (self.cell_size + self.margin)
        maze_height = rows * (self.cell_size + self.margin)

        self.screen.blit(self.assets['background'],(0,0))

        x_offset = (self.width - maze_width) // 2
        y_offset = (self.height - maze_height) // 2
        
        for row in range(rows):
            for cols in range(columns):
                x = x_offset + cols * (self.cell_size + self.margin)
                y = y_offset + row * (self.cell_size + self.margin)
                cell_value = self.matrix[row][cols]

                if cell_value == '1':
                    self.screen.blit(self.assets['wall'], (x, y))
                elif cell_value == 'x':
                    self.screen.blit(self.assets['jerry'], (x, y))
                elif cell_value == 'y':
                    self.screen.blit(self.assets['cheese'], (x, y))
                else:
                    self.screen.blit(self.assets['path'], (x, y))

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
        
        if 0<=new_row<len(self.matrix) and 0<=new_col<len(self.matrix):
            if self.matrix[new_row][new_col]!='1':
                self.matrix[self.mov_row][self.mov_col]='0'
                self.redraw_visted_cell(self.mov_row, self.mov_col)
                self.mov_row,self.mov_col = new_row,new_col
                self.matrix[self.mov_row][self.mov_col]='x'
                self.redraw_visted_cell(self.mov_row,self.mov_col)

            

    def game_over(self):
        if not self.gameover:
            high = HighScore()
            high.create_table()
            current_score = str(float("{:.2f}".format(time.time()-self.start_time)))
            high.insert_score(len(self.matrix),float(current_score))
            overall_score = str(high.highest_score(len(self.matrix)))
            self.screen.blit(self.assets['welcome'],(0,0))

            self.screen.blit(self.assets['gameover'], (self.width//2-200, self.height//2-250))
            self.screen.blit(self.assets['currentscore'], (self.width//2-150, self.height//2-100))
            self.screen.blit(self.assets['highscore'], (self.width//2-150, self.height//2))
            
            self.append_score(current_score,80)
            self.append_score(overall_score,180)
            pygame.mixer_music.stop()
            self.music_played=False

            self.music_enabler('assets/sound/game-over.mp3')
            self.music_played = True
            self.gameover = True


    def append_score(self,scorepoint,height_gap):
        width = -50
        for score in scorepoint:
            score, height = ('dot', 30) if score == '.' else (score, 25)
            out = pygame.transform.scale(pygame.image.load(f"assets/images/score_point/{score}.png").convert_alpha(), (25, 25))
            self.screen.blit(out, (self.width//2+width, self.height//2+height_gap))
            width+=15
            
    
    def redraw_visted_cell(self, row, col):
        x_offset = (self.width - len(self.matrix[0]) * (self.cell_size + self.margin)) // 2
        y_offset = (self.height - len(self.matrix) * (self.cell_size + self.margin)) // 2

        x = x_offset + col * (self.cell_size + self.margin)
        y = y_offset + row * (self.cell_size + self.margin)

        cell_value = self.matrix[row][col]

        if cell_value == '1':
            self.screen.blit(self.assets['wall'], (x, y))
        elif cell_value == 'x':
            self.screen.blit(self.assets['jerry'], (x, y))
        elif cell_value=='y':
            self.screen.blit(self.assets['cheese'], (x, y))
        else:
            self.screen.blit(self.assets['path'], (x, y))
    
    def music_enabler(self,audio):
        if not self.music_played:
            pygame.mixer.init()
            pygame.mixer.music.load(audio)
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            self.music_played = True
