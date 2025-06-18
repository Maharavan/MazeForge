import pygame
class Player:
    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, key, matrix, renderer, character_image,char_end):
        new_row, new_col = self.row, self.col
        if key == pygame.K_LEFT:
            new_col -= 1
        elif key == pygame.K_RIGHT:
            new_col += 1
        elif key == pygame.K_UP:
            new_row -= 1
        elif key == pygame.K_DOWN:
            new_row += 1

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] != '1':
            matrix[self.row][self.col] = '0'
            renderer.draw_cell(self.row, self.col, matrix, character_image,char_end)
            self.row, self.col = new_row, new_col
            matrix[self.row][self.col] = 'x'
            renderer.draw_cell(self.row, self.col, matrix, character_image,char_end)

    def reset(self):
        self.row, self.col = 0, 0

    def has_won(self, matrix):
        return self.row == len(matrix) - 1 and self.col == len(matrix[0]) - 1
