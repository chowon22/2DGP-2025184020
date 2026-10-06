from pico2d import *

open_canvas(800, 600)

sonic = load_image('sonic-sprite.png')

running = True
while running:
    clear_canvas()
    sonic.draw(400, 300)
    update_canvas()
    delay(0.1)

close_canvas()
