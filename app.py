import sys
import random
from Mazegenerator import MazeGenerator
from PyMaze import PyMaze

if __name__=='__main__':
    maze_size = random.randint(10,15)
    maze = MazeGenerator(maze_size)  
    output = maze.generate_maze() 
    gui_game = PyMaze(output) 
    gui_game.invoke_game()

    