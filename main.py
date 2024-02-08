import os

import bedrock
import blocks
from config import WORLD_DIR, WALL_BLOCKS, Y_OFFSET, HALLWAY_BLOCKS
from parser import get_maze


def maze_to_world(world_path):
    with bedrock.World(world_path) as world:
        for y, y_val in enumerate(maze):
            for x, x_val in enumerate(y_val):
                if x_val:
                    # Стены
                    for y_offset, block in enumerate(WALL_BLOCKS):
                        if block is blocks.AIR:
                            continue

                        world.setBlock(x, Y_OFFSET + y_offset, y, block)
                else:
                    # Пространство для перемещения
                    for y_offset, block in enumerate(HALLWAY_BLOCKS):
                        if block is blocks.AIR:
                            continue

                        world.setBlock(x, Y_OFFSET + y_offset, y, block)


if __name__ == '__main__':
    maze = get_maze()

    path = os.path.join(os.getcwd(), WORLD_DIR)
    maze_to_world(path)
