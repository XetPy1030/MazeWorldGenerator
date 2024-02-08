from PIL import Image

import bedrock
import blocks
from config import MAZE_IMAGE_PATH, MAZE_WIDTH, MAZE_HEIGHT, WALL_BLOCKS, Y_OFFSET, HALLWAY_BLOCKS


def get_maze_from_image():
    image = Image.open(MAZE_IMAGE_PATH)
    pix = image.load()
    width, height = image.size

    # maze[y][x]
    maze = [
        [0 for _ in range(MAZE_WIDTH * 2 + 1)]
        for _ in range(MAZE_HEIGHT * 2 + 1)
    ]

    # Правая стенка
    for i in range(MAZE_HEIGHT * 2):
        maze[MAZE_HEIGHT * 2 - i][MAZE_HEIGHT * 2] = 1

    # Нижняя стенка
    for i in range(MAZE_WIDTH):
        # Если выход
        if pix[i * 16 + 2, height - 1][0] == 0:
            maze[MAZE_WIDTH * 2][MAZE_WIDTH * 2 - 1 - i * 2] = 1

    # Стенки по горизонтали
    for i in range(MAZE_WIDTH):
        for o in range(MAZE_HEIGHT):
            if pix[i * 16 + 2, o * 16 + 1][0] == 0:
                maze[o * 2][i * 2 + 1] = 1

    # Стенки по вертикали
    for i in range(MAZE_WIDTH):
        for o in range(MAZE_HEIGHT):
            if pix[i * 16 + 1, o * 16 + 2][0] == 0:
                maze[o * 2 + 1][i * 2] = 1

    # Столбцы меж стенками
    for i in range(MAZE_WIDTH + 1):
        for o in range(MAZE_HEIGHT + 1):
            maze[o * 2][i * 2] = 1

    return maze


def maze_to_world(world_path, maze):
    with bedrock.World(world_path) as world:
        for y, y_val in enumerate(maze):
            for x, x_val in enumerate(y_val):
                set_blocks_to_maze(
                    world, x, y,
                    WALL_BLOCKS if x_val else HALLWAY_BLOCKS
                )


def set_blocks_to_maze(world, x, y, list_blocks):
    for y_offset, block in enumerate(list_blocks):
        if block is blocks.AIR:
            continue

        world.setBlock(x, Y_OFFSET + y_offset, y, block)
