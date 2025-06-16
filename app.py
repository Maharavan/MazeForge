import sys
import random
from Mazegenerator import MazeGenerator
from MazeForge import PyMaze

if __name__=='__main__':
    maze_size = random.choice([i for i in range(7,14) if i % 2 == 1])
    maze = MazeGenerator(7)  
    output = maze.generate_maze() 
    print(output)
    gui_game = PyMaze(output) 
    gui_game.invoke_game()

    