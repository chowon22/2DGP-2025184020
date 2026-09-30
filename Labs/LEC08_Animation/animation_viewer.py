from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet_knight.png')

while True:
    get_events()
    clear_canvas()

    update_canvas()
    delay(0.1)

close_canvas()

