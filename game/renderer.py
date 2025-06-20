import pygame
from .constants import WIDTH, HEIGHT, FPS
from HighScoreDB import HighScore
class Renderer:
    def __init__(self, screen, assets, cell_size, margin):
        self.screen = screen
        self.assets = assets
        self.cell_size = cell_size
        self.margin = margin

    def draw_menu(self):
        self.screen.blit(self.assets['welcome'], (0, 0))
        start_rect = self.assets['start_button'].get_rect(center=(WIDTH//2-100, HEIGHT//2))
        self.screen.blit(self.assets['start_button'], start_rect)
        end_rect = self.assets['end_button'].get_rect(center=(WIDTH//2 + 100, HEIGHT//2))
        self.screen.blit(self.assets['end_button'], end_rect)
        leader_board_rect = self.assets['leaderboard'].get_rect(center=(WIDTH//2, HEIGHT//2+180))
        self.screen.blit(self.assets['leaderboard'],leader_board_rect)

        return start_rect, end_rect, leader_board_rect
    
    def draw_character(self):
        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['character'], (WIDTH//2 - 100, HEIGHT//2 - 200))

        character = [('jerry','cheese'),('tom','wool'),('spike','bones')]
        x_positions = [WIDTH//2 - 300, WIDTH//2, WIDTH//2 + 300]
        buttons = {}
        for diff, x in zip(character, x_positions):
            rect = self.assets[diff].get_rect(center=(x, HEIGHT//2 + 50))
            self.screen.blit(self.assets[diff], rect)
            buttons[diff] = rect
        return buttons

    def draw_difficulty_screen(self, difficulties):
        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['choosesize'], (WIDTH//2 - 100, HEIGHT//2 - 170))
        x_positions = [WIDTH//2 - 200, WIDTH//2, WIDTH//2 + 200]
        buttons = {}
        for diff, x in zip(difficulties, x_positions):
            rect = self.assets[diff].get_rect(center=(x, HEIGHT//2 + 50))
            self.screen.blit(self.assets[diff], rect)
            buttons[diff] = rect
        return buttons

    def draw_maze(self, matrix,character_image,char_end):
        self.screen.blit(self.assets['background'], (0, 0))
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.draw_cell(r, c, matrix, character_image,char_end)

    def draw_cell(self, row, col, matrix, character_image, char_end):
        x_off = (1024 - len(matrix[0]) * (self.cell_size + self.margin)) // 2
        y_off = (600 - len(matrix) * (self.cell_size + self.margin)) // 2
        x = x_off + col * (self.cell_size + self.margin)
        y = y_off + row * (self.cell_size + self.margin)
        val = matrix[row][col]
        if val == '1':
            self.screen.blit(self.assets['wall'], (x, y))
        elif val == 'x':
            self.screen.blit(self.assets[character_image], (x, y))
        elif val == 'y':
            self.screen.blit(self.assets[char_end], (x, y))
        else:
            self.screen.blit(self.assets['path'], (x, y))

    def draw_game_over(self, current_score, high_score):
        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['gameover'], (WIDTH//2-150, HEIGHT//2 - 220))
        self.screen.blit(self.assets['currentscore'], (WIDTH//2 - 100, HEIGHT//2 - 100))
        self.screen.blit(self.assets['highscore'], (WIDTH//2 - 97, HEIGHT//2))
        self._draw_score(current_score, 25)
        self._draw_score(high_score, 125)

        restart_button = self.assets['restart_button'].get_rect(center=(WIDTH//2, HEIGHT//2+250))
        self.screen.blit(self.assets['restart_button'], restart_button)
        return restart_button

    def _draw_score(self, score, y_offset):
        x = -30
        for char in score:
            image_name = 'dot' if char == '.' else char
            img = pygame.transform.scale(
                pygame.image.load(f"assets/images/score_point/{image_name}.png").convert_alpha(), (25, 25)
            )
            self.screen.blit(img, (WIDTH//2 + x, HEIGHT//2 + y_offset))
            x += 13
    
    def _draw_leader_board(self):
        data_diff = HighScore()
        output = data_diff.retrieve_highest_score()
        print(output)

        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['leaderboard'],(WIDTH//2-100,HEIGHT//2-200))

        self.screen.blit(self.assets[('easy',(7,))], (WIDTH//2-200, HEIGHT//2-75))
        self.screen.blit(self.assets[('medium',(9,11))], (WIDTH//2-200, HEIGHT//2))
        self.screen.blit(self.assets[('hard',(13,))],(WIDTH//2-200, HEIGHT//2+100))