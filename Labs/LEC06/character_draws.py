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

def MoveRectangle():
    print("Rectangle")
    pass

def MoveTriangle():
    print("Triangle")
    pass

while 1:
    MoveCircle()
    MoveRectangle()
    MoveTriangle()
    pass