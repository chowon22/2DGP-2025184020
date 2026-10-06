from pico2d import *

SCALE = 8
FRAME_TIME = 0.1  # 프레임 하나를 보여 주는 시간(초)
CENTER_X = 400
GROUND_Y = 100  # 발을 맞추는 바닥선 높이

# 1번 동작: 걷기 시작 / 가속 (left, bottom, width, height)
action1 = [
    (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 28, 39), (86, 447, 30, 38),
    (118, 447, 30, 38), (150, 447, 30, 38), (182, 447, 29, 38), (211, 448, 29, 38),
    (240, 448, 29, 38), (270, 448, 24, 32), (302, 448, 29, 26),
]


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
frame = 0
while running:
    clear_canvas()
    left, bottom, w, h = action1[frame]
    sonic.clip_draw(left, bottom, w, h, CENTER_X, GROUND_Y + h * SCALE // 2, w * SCALE, h * SCALE)
    update_canvas()
    handle_events()
    frame = (frame + 1) % len(action1)
    delay(FRAME_TIME)

close_canvas()
