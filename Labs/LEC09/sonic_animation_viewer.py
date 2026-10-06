from pico2d import *


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


open_canvas(800, 600)

sonic = load_image('sonic-sprite.png')

running = True
while running:
    clear_canvas()
    sonic.draw(400, 300)
    update_canvas()
    handle_events()
    delay(0.1)

close_canvas()
