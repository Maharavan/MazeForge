import random
import pygame
class MazeGenerator:
    def __init__(self,size):
        self.size = size
        self.row = self.size
        self.column = self.size
        self.maze = [[1 for _ in range(self.column)] for _ in range(self.row)]
        self.direction = [(2,0),(0,2),(0,-2),(-2,0)]
    def check_valid(self,x,y):
        if 0<=x<self.row and 0<=y<self.column:
            return True
        return False

    def maze_algo(self,row,col):
        self.maze[row][col] = 0
        random.shuffle(self.direction)
        for dx,dy in self.direction:
            cur_row,cur_col = row+dx, col+dy
            if self.check_valid(cur_row,cur_col) and self.maze[cur_row][cur_col]:
                next_row = (row+cur_row)//2
                next_col = (col+cur_col)//2
                self.maze[next_row][next_col]=0
                self.maze_algo(cur_row, cur_col) 
            
    def generate_maze(self):
        while True:
            self.maze_algo(0,0)
            if self.maze[self.row-1][self.column-1]==0:
                break
        self.maze[0][0] = 'x'
        self.maze[self.row-1][self.column-1] = 'y'
        for i in range(self.row):
            self.maze[i] = [str(j) for j in self.maze[i]]
        return self.maze