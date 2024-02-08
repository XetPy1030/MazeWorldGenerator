import os

from config import WORLD_DIR
from maze import get_maze, maze_to_world

if __name__ == '__main__':
    maze_ = get_maze()

    path = os.path.join(os.getcwd(), WORLD_DIR)
    maze_to_world(path, maze_)
