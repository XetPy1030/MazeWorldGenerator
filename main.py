import os

from config import WORLD_DIR
from maze import get_maze_from_image, maze_to_world

if __name__ == '__main__':
    maze_ = get_maze_from_image()

    path = os.path.join(os.getcwd(), WORLD_DIR)
    maze_to_world(path, maze_)
