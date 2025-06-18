import pygame
import sys
import time
import random
from .assets_loader import load_assets
from .constants import WIDTH, HEIGHT, FPS
from .sound_manager import SoundManager
from .player import Player
from .renderer import Renderer
from HighScoreDB import HighScore
from Mazegenerator import MazeGenerator

class MazeForge:
    def __init__(self):
        self.matrix = None
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = None
        self.fps = FPS
        self.fpsClock = pygame.time.Clock()
        self.start_button_rect = None
        self.difficulty_buttons = {}
        self.end_button_rect = None
        self.chose_character = {}
        self.character_image = None
        self.char_end = None
        self.state = 'menu'
        self.cell_size = 35
        self.margin = 5
        self.sound_manager = SoundManager()
        self.player = Player()
        self.start_time = None
        self.gameover = False
        self.restart_button_rect = None

    def invoke_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.assets = load_assets(self.cell_size, self.width, self.height)
        self.renderer = Renderer(self.screen, self.assets, self.cell_size, self.margin)

        pygame.display.set_icon(self.assets['icon'])
        pygame.display.set_caption('MazeForge')

        game_begin = True
        while game_begin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_begin = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect and self.start_button_rect.collidepoint(event.pos):
                        self.state = 'difficulty_option'
                    elif self.state == 'difficulty_option':
                        for diff, rect in self.difficulty_buttons.items():
                            if rect.collidepoint(event.pos):
                                maze = MazeGenerator(random.choice(diff[1]))
                                self.matrix = maze.generate_maze()
                                self.player.reset()
                                self.state = 'chose_character'
                                break
                    elif self.state=='chose_character':
                        for diff, rect in self.chose_character.items():
                            if rect.collidepoint(event.pos):
                                self.character_image = diff[0]
                                self.char_end = diff[1]
                                self.sound_manager.stop_music()
                                self.state = 'game_begin'
                                break
                    elif self.end_button_rect and self.end_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.restart_button_rect and self.restart_button_rect.collidepoint(event.pos):
                        self.sound_manager.stop_music()
                        self.sound_manager.play_music('assets/sound/game-intro.mp3')
                        self.state = 'difficulty_option'
                        self.matrix = None
                        self.player.reset()
                        self.start_time = None
                        self.gameover = False
                elif event.type == pygame.KEYDOWN and self.state == 'game':
                    self.sound_manager.play_music('assets/sound/game-begins.mp3')
                    self.player.move(event.key, self.matrix, self.renderer,self.character_image,self.char_end)

            if self.state == 'menu':
                self.sound_manager.play_music("assets/sound/game-intro.mp3")
                self.start_button_rect, self.end_button_rect = self.renderer.draw_menu()
            elif self.state == 'chose_character':
                self.chose_character = self.renderer.draw_character()
            elif self.state == 'difficulty_option':
                self.difficulty_buttons = self.renderer.draw_difficulty_screen()
            elif self.state == 'game_begin':
                self.renderer.draw_maze(self.matrix,self.character_image, self.char_end)
                self.start_time = time.time()
                self.state = 'game'
            elif self.player.has_won(self.matrix):
                self.game_over()
                self.state = 'game_over'
                
            pygame.display.flip()
            self.fpsClock.tick(self.fps)
        pygame.quit()

    def game_over(self):
        if not self.gameover:
            high = HighScore()
            current_score = str(float("{:.2f}".format(time.time() - self.start_time)))
            high.insert_score(len(self.matrix), float(current_score))
            overall_score = str(high.highest_score(len(self.matrix)))
            self.restart_button_rect=self.renderer.draw_game_over(current_score, overall_score)

            self.sound_manager.stop_music()
            self.sound_manager.play_music('assets/sound/game-over.mp3', loop=0)
            self.gameover = True
