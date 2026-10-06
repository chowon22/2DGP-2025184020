from pico2d import *


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(800, 600)

sonic = load_image('sonic-sprite.png')

running = True
while running:
    clear_canvas()
    sonic.clip_draw(1, 447, 29, 39, 400, 300)
    update_canvas()
    handle_events()
    delay(0.1)

close_canvas()
