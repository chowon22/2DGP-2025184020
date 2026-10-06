from pico2d import *

SCALE = 8
FRAME_TIME = 0.1  # 프레임 하나를 보여 주는 시간(초)
CENTER_X = 400
GROUND_Y = 100  # 발을 맞추는 바닥선 높이

# 동작별 프레임 좌표 (left, bottom, width, height)
actions = [
    # 1. 걷기 시작 / 가속
    [(1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 28, 39), (86, 447, 30, 38),
     (118, 447, 30, 38), (150, 447, 30, 38), (182, 447, 29, 38), (211, 448, 29, 38),
     (240, 448, 29, 38), (270, 448, 24, 32), (302, 448, 29, 26)],
    # 2. 달리기
    [(8, 408, 26, 37), (37, 408, 27, 37), (65, 407, 31, 38), (97, 408, 37, 37),
     (135, 410, 32, 35), (170, 408, 32, 38), (206, 408, 26, 38), (238, 408, 24, 37),
     (263, 408, 30, 37), (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38)],
    # 3. 브레이크 / 회전 동작
    [(1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38), (130, 362, 34, 42),
     (181, 362, 34, 41), (228, 363, 33, 40)],
]

action = 0  # 재생할 동작 번호 (0부터)


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
    left, bottom, w, h = actions[action][frame]
    sonic.clip_draw(left, bottom, w, h, CENTER_X, GROUND_Y + h * SCALE // 2, w * SCALE, h * SCALE)
    update_canvas()
    handle_events()
    frame = (frame + 1) % len(actions[action])
    delay(FRAME_TIME)

close_canvas()
