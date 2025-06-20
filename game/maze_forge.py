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
        self.difficulty = [('easy', (7,)), ('medium', (9, 11)), ('hard', (13,))]
        self.gameover = False
        self.leaderboardrect = None
        self.menu_button_rect = None
        self.current_music = None  # new: track current music

    def reset_game_state(self):
        self.state = 'menu'
        self.matrix = None
        self.player.reset()
        self.start_time = None
        self.gameover = False
        self.current_music = None
        self.sound_manager.stop_music()

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
                    pos = event.pos

                    if self.state == 'menu':
                        if self.start_button_rect and self.start_button_rect.collidepoint(pos):
                            self.state = 'difficulty_option'
                        elif self.end_button_rect and self.end_button_rect.collidepoint(pos):
                            pygame.quit()
                            sys.exit()
                        elif self.leaderboardrect and self.leaderboardrect.collidepoint(pos):
                            self.state = 'leaderboard'

                    elif self.state == 'difficulty_option':
                        for diff, rect in self.difficulty_buttons.items():
                            if rect.collidepoint(pos):
                                maze = MazeGenerator(random.choice(diff[1]))
                                self.matrix = maze.generate_maze()
                                self.player.reset()
                                self.state = 'chose_character'
                                break

                    elif self.state == 'chose_character':
                        for diff, rect in self.chose_character.items():
                            if rect.collidepoint(pos):
                                self.character_image = diff[0]
                                self.char_end = diff[1]
                                self.sound_manager.stop_music()
                                self.current_music = None
                                self.state = 'game_begin'
                                break

                    elif self.state == 'game_over':
                        if self.menu_button_rect and self.menu_button_rect.collidepoint(pos):
                            self.reset_game_state()

                    elif self.state == 'leaderboard':
                        if self.menu_button_rect and self.menu_button_rect.collidepoint(pos):
                            self.reset_game_state()

                elif event.type == pygame.KEYDOWN:
                    if self.state == 'game_begin':
                        self.start_time = time.time()
                        self.sound_manager.stop_music()
                        self.sound_manager.play_music("assets/sound/game-begins.mp3", loop=-1)
                        self.current_music = 'game'
                        self.state = 'game'
                        self.player.move(event.key, self.matrix, self.renderer, self.character_image, self.char_end)
                    elif self.state == 'game':
                        self.player.move(event.key, self.matrix, self.renderer, self.character_image, self.char_end)
            if self.state == 'menu':
                if self.current_music != 'menu':
                    self.sound_manager.stop_music()
                    self.sound_manager.play_music("assets/sound/game-intro.mp3", loop=-1)
                    self.current_music = 'menu'
                self.start_button_rect, self.end_button_rect, self.leaderboardrect = self.renderer.draw_menu()

            elif self.state == 'difficulty_option':
                self.difficulty_buttons = self.renderer.draw_difficulty_screen(self.difficulty)

            elif self.state == 'chose_character':
                self.chose_character = self.renderer.draw_character()

            elif self.state == 'game_begin':
                self.renderer.draw_maze(self.matrix, self.character_image, self.char_end)

            elif self.state == 'leaderboard':
                self.menu_button_rect = self.renderer._draw_leader_board()

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
            for diff, size in self.difficulty:
                if len(self.matrix) in size:
                    high.insert_score(diff, float(current_score))
                    overall_score = str(high.highest_score(diff))
                    break
            self.menu_button_rect = self.renderer.draw_game_over(current_score, overall_score)
            self.sound_manager.stop_music()
            self.sound_manager.play_music('assets/sound/game-over.mp3', loop=-1)
            self.current_music = 'game_over'
            self.gameover = True
