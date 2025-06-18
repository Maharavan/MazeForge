import pygame
from .constants import WIDTH, HEIGHT, FPS

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
        return start_rect, end_rect

    def draw_difficulty_screen(self):
        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['choosesize'], (WIDTH//2 - 150, HEIGHT//2 - 250))
        difficulties = [('easy', (7,)), ('medium', (9, 11)), ('hard', (13,))]
        x_positions = [WIDTH//2 - 200, WIDTH//2, WIDTH//2 + 200]
        buttons = {}
        for diff, x in zip(difficulties, x_positions):
            rect = self.assets[diff].get_rect(center=(x, HEIGHT//2 + 50))
            self.screen.blit(self.assets[diff], rect)
            buttons[diff] = rect
        return buttons

    def draw_maze(self, matrix):
        self.screen.blit(self.assets['background'], (0, 0))
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.draw_cell(r, c, matrix)

    def draw_cell(self, row, col, matrix):
        x_off = (1024 - len(matrix[0]) * (self.cell_size + self.margin)) // 2
        y_off = (600 - len(matrix) * (self.cell_size + self.margin)) // 2
        x = x_off + col * (self.cell_size + self.margin)
        y = y_off + row * (self.cell_size + self.margin)
        val = matrix[row][col]
        if val == '1':
            self.screen.blit(self.assets['wall'], (x, y))
        elif val == 'x':
            self.screen.blit(self.assets['jerry'], (x, y))
        elif val == 'y':
            self.screen.blit(self.assets['cheese'], (x, y))
        else:
            self.screen.blit(self.assets['path'], (x, y))

    def draw_game_over(self, current_score, high_score):
        self.screen.blit(self.assets['welcome'], (0, 0))
        self.screen.blit(self.assets['gameover'], (WIDTH//2 - 200, HEIGHT//2 - 250))
        self.screen.blit(self.assets['currentscore'], (WIDTH//2 - 150, HEIGHT//2 - 100))
        self.screen.blit(self.assets['highscore'], (WIDTH//2 - 150, HEIGHT//2))
        self._draw_score(current_score, 80)
        self._draw_score(high_score, 180)

    def _draw_score(self, score, y_offset):
        x = -50
        for char in score:
            image_name = 'dot' if char == '.' else char
            img = pygame.transform.scale(
                pygame.image.load(f"assets/images/score_point/{image_name}.png").convert_alpha(), (25, 25)
            )
            self.screen.blit(img, (WIDTH//2 + x, HEIGHT//2 + y_offset))
            x += 13