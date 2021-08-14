import bedrock, os
import struct, time
from PIL import Image, ImageDraw

image = Image.open('maze.png')  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

image1 = Image.open('maze.png')  # Открываем изображение
draw1 = ImageDraw.Draw(image1)  # Создаем инструмент для рисования
pix1 = image1.load()  # Выгружаем значения пикселей

m_wi = 80
m_he = 80

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

coord = [81, 160]
finish = [79, 0]
t = 0
dist = 0
turn = ["u", "r", "d", "l"]
played = True
def next_l(t):
    t-=1
    if t == -1:
        t = 3
    return t
def next_r(t):
    t+=1
    if t == 4:
        t = 0
    return t
def coords(turn, t):
    #print(t)
    if turn[t] in ["u", "d"]:
        return [[1, 0], [0, 1], [-1, 0], [0, -1]]
    elif turn[t] in ["l", "r"]:
        return [[0, -1], [1, 0], [0, 1], [-1, 0]]

def check_u(pix, coord):
    if pix[coord[0], coord[1]-1][0] == 255:
        return 0
    else:
        return check_r(pix, coord)
def check_r(pix, coord):
    if pix[coord[0]+1, coord[1]][0] == 255:
        return 1
    else:
        return check_d(pix, coord)
def check_d(pix, coord):
    if pix[coord[0], coord[1]+1][0] == 255:
        return 2
    else:
        return check_l(pix, coord)
def check_l(pix, coord):
    if pix[coord[0]-1, coord[1]][0] == 255:
        return 3
    else:
        return check_u(pix, coord)
#["u", "r", "d", "l"]
def move(t, dist, coord):
    dist+=1
    if t == 0:
        coord[1] -= 1
    elif t == 1:
        coord[0] +=1
    elif t == 2:
        coord[1] +=1
    elif t == 3:
        coord[0] -=1
    return dist, coord
checks = [check_l, check_u, check_r, check_d]
#по левой стенке
while played:
    if coord == finish:
        print(dist)
        played = False
    else:
        try:
            t = checks[t](pix, coord)
            dist, coord = move(t, dist, coord)
            #print(dist)
            #print(coord, " ", pix[coord[0], coord[1]], " ", t)
        except Exception as e:
            print(e)
            break
        #draw.point((coord[0], coord[1]), (255, 0, 0))
        #image.save("test.png", "PNG")
        #draw.point((coord[0], coord[1]), (255, 255, 255))
        #time.sleep(2)