from math import cos, sin, sqrt

from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 300
r = 100
pi = 3.141592
theta = 0
while 1:
    events = get_events()
    # 게임 상호작용
    x = 400 + r * cos(theta)
    y = 300 + r * sin(theta)
    theta += 0.02

    # 게임 보여주기
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    delay(0.01)


close_canvas()

