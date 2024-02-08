from PIL import Image

from config import MAZE_IMAGE_PATH, MAZE_WIDTH, MAZE_HEIGHT


def get_maze():
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
