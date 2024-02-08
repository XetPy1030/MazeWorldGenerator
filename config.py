import blocks

MAZE_IMAGE_PATH = 'example_maze.png'
WORLD_DIR = 'example_world'

MAZE_WIDTH = 80
MAZE_HEIGHT = 80

Y_OFFSET = 3

WALL_BLOCKS = [
    blocks.BRICK_BLOCK,
    blocks.OAK_PLANKS,
    blocks.OAK_PLANKS,
    blocks.OAK_PLANKS,
    blocks.OAK_PLANKS,
]

HALLWAY_BLOCKS = [
    blocks.BRICK_BLOCK,
    blocks.AIR,
    blocks.AIR,
    blocks.AIR,
    blocks.GLASS,
]
