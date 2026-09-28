# 실습 과제 진행
from math import *
from pico2d import *

open_canvas(800,600)

character = load_image("character.png")

def MoveCircle():
    print("Circle")
    
    radius = 100

    for angle in range(360):
        x = radius * sin(radians(angle)) + 400
        y = radius * cos(radians(angle)) + 300
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)
        get_events()

def MoveRectangle():
    print("Rectangle")

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    x = 400
    y = 400
    for i in range(5):
        while 1:
            x += d[i % 4][0]
            y += d[i % 4][1]

            clear_canvas()
            character.draw(x,y)
            update_canvas()

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

            delay(0.01)
        get_events()
    pass

def MoveTriangle():
    print("Triangle")

    points = [(500, 300), (300, 300), (400, 400)]
    

    pass

while 1:
    MoveCircle()
    MoveRectangle()
    MoveTriangle()
    pass