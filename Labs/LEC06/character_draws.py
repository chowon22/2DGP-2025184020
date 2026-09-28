# 실습 과제 진행
from math import *
from pico2d import *

open_canvas(800,600)

character = load_image("character.png")

x = 400
y = 400

DELAY_TIME= 0.01

def Draw(x, y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(DELAY_TIME)
    get_events()

def MoveCircle(x, y):
    print("Circle")
    
    radius = 100

    for angle in range(360):
        x = radius * sin(radians(angle)) + 400
        y = radius * cos(radians(angle)) + 300
    Draw(x, y)

def MoveRectangle(x, y):
    print("Rectangle")

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for i in range(5):
        while 1:
            x += d[i % 4][0]
            y += d[i % 4][1]

            Draw(x, y)

            if x > 500:
                x = 500
                break
            elif x < 300:
                x = 300
                break
            elif y > 400:
                y = 400
                break
            elif y < 200:
                y = 200
                break
            elif i == 4 and x >= 400:
                x = 4
                break

    pass

def MoveTriangle(x, y):
    print("Triangle")

    points = [(400, 400), (500, 300), (300, 300), (400, 400)]
    
    for i in range(3):
        for t in range(100):
            x = points[i][0] + (points[i + 1][0] - points[i][0]) * t / 100
            y = points[i][1] + (points[i + 1][1] - points[i][1]) * t / 100
            
            Draw(x, y)
            
    

while 1:
    MoveCircle(x, y)
    MoveRectangle(x, y)
    MoveTriangle(x, y)
    pass