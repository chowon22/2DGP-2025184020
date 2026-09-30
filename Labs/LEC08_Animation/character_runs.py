from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
frame = 0
action = 0

for x in range(750, 5, -5):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(
        (frame % 8) * 100, 0,     #left, bottom 
        100, 100,           #width, height
        x, 100,           #destination x, y
        200, 200            #scale
    )
    update_canvas()
    delay(0.05)
    get_events()

while 1:
    for frame in range(0, 16):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(
            (frame % 8) * 100, action * 100,     #left, bottom 
            100, 100,           #width, height
            400, 400,           #destination x, y
            200, 200            #scale
        )
        update_canvas()
        delay(0.05)
        get_events()
    action = (action + 1) % 4
    pass

#close_canvas()

