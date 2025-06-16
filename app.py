import sys
import random
from Mazegenerator import MazeGenerator
from MazeForge import MazeForge

if __name__=='__main__':
    maze_size = random.choice([i for i in range(7,14) if i % 2 == 1])
    maze = MazeGenerator(maze_size)  
    output = maze.generate_maze() 
    gui_game = MazeForge(output) 
    gui_game.invoke_game()

    