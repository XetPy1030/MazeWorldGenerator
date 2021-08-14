photo_maze = "maze.png"
m_wi = 80 #maze width
m_he = 80 #maze height
world_dir = "world"





import bedrock, os
import struct, time
from PIL import Image, ImageDraw

image = Image.open(photo_maze)  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

image1 = Image.open(photo_maze)  # Открываем изображение
draw1 = ImageDraw.Draw(image1)  # Создаем инструмент для рисования
pix1 = image1.load()  # Выгружаем значения пикселей

for i in range((m_wi+1)*2):
    for o in range((m_he+1)*2):
        draw.point((i, o), (255, 255, 255))


for i in range(m_he*2):
    draw.point((m_he*2, m_he*2-i), (0, 0, 0))

for i in range(m_wi):
    if pix1[i*16+2, height-1][0] == 0:
        draw.point((m_wi*2-1-i*2, m_wi*2), (0, 0, 0))
    else:
        pass#print(m_wi*2+1-i*2, m_wi*2)



for i in range(m_wi):
    for o in range(1):
        if pix1[i*16+2, (o)*16+1][0] != 0:
            pass#print((i*2+1, o*2))



for i in range(m_wi):
    for o in range(m_he):
        if pix1[i*16+2, (o)*16+1][0] == 0:
            draw.point((i*2+1, o*2), (0, 0, 0))
for i in range(m_wi):
    for o in range(m_he):
        if pix1[(i)*16+1, (o)*16+2][0] == 0:
            draw.point((i*2, o*2+1), (0, 0, 0))

#точки
for i in range(m_wi+1):
    for o in range(m_he+1):
        draw.point((i*2, o*2), (0, 0, 0))
#draw.point((79, 160), (0, 0, 0))
image.save("test.png", "PNG") #не забываем сохранить изображение
#image1.save("test1.png", "PNG")
#0, 16
brick_block = bedrock.Block("minecraft:brick_block")
oak_planks = bedrock.Block("minecraft:planks")
glass = bedrock.Block("minecraft:glass")
with bedrock.World(os.getcwd()+"\\{}\\".format(world_dir)) as world:
    for i in range(m_wi*2+1):
        for o in range(m_he*2+1):
            print(i, " ", o)
            if pix[i, o][0] == 0:
                world.setBlock(i, 3, o, brick_block)
                world.setBlock(i, 4, o, oak_planks)
                world.setBlock(i, 5, o, oak_planks)
                world.setBlock(i, 6, o, oak_planks)
                world.setBlock(i, 7, o, oak_planks)
            else:
                world.setBlock(i, 3, o, brick_block)
                world.setBlock(i, 7, o, glass)