from pico2d import *

# 스프라이트 시트 프레임 정보: (left, bottom, width, height, anchor_x), pico2d 좌표계(좌하단 원점)
# anchor_x: 프레임 왼쪽 끝에서 두 발 사이 중점까지의 거리 (x 보정용)
ANIMATIONS = [
    ('idle', [
        (89, 847, 150, 126, 60), (317, 847, 155, 124, 66), (545, 847, 162, 126, 69), (783, 847, 157, 121, 67),
    ]),
    ('run', [
        (73, 654, 183, 127, 72), (323, 654, 176, 127, 64), (567, 654, 172, 127, 63),
        (812, 660, 181, 121, 58), (1059, 660, 180, 120, 61), (1294, 655, 169, 129, 62),
    ]),
    ('jump', [
        (73, 445, 177, 109, 63), (339, 458, 167, 133, 62), (625, 488, 201, 132, 76),
        (890, 451, 192, 131, 83), (1193, 444, 187, 110, 65),
    ]),
    ('attack', [
        (89, 229, 124, 155, 80), (278, 228, 156, 154, 90), (464, 227, 144, 170, 64), (664, 227, 197, 124, 70),
        (901, 227, 182, 148, 62), (1127, 227, 171, 116, 49), (1340, 229, 169, 130, 72),
    ]),
    ('hurt', [
        (122, 40, 158, 105, 91), (356, 40, 144, 126, 103), (629, 40, 156, 90, 55),
    ]),
]

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_DELAY = 0.08
SCALE = 2.5
FOOT_Y = 150  # 캐릭터 발이 놓일 화면 y좌표
REPEAT_COUNT = 5  # 애니메이션마다 반복 재생할 횟수
PAUSE_TIME = 1.0  # 애니메이션 전환 시 정지 시간(초)

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

grass = load_image('grass.png')
character = load_image('animation_sheet_knight.png')

anim_index = 0
frame = 0
repeat = 0

while True:
    get_events()
    clear_canvas()
    grass.draw(400, 30)

    name, frames = ANIMATIONS[anim_index]
    left, bottom, width, height, anchor_x = frames[frame]
    # 프레임마다 높이가 달라도 발 위치가 고정되도록 중심 y좌표 보정
    base = min(f[1] for f in frames)
    y = FOOT_Y + (bottom - base) * SCALE + height * SCALE / 2
    # 프레임마다 캐릭터 위치가 달라도 발이 화면 중앙에 오도록 중심 x좌표 보정
    x = CANVAS_WIDTH // 2 + (width / 2 - anchor_x) * SCALE
    character.clip_draw(left, bottom, width, height, x, y,
                        width * SCALE, height * SCALE)

    update_canvas()
    frame = (frame + 1) % len(frames)
    if frame == 0:  # 마지막 프레임까지 재생하고 처음으로 돌아오면 한 사이클 완료
        repeat += 1
        if repeat == REPEAT_COUNT:  # 정해진 횟수만큼 반복하면 다음 애니메이션으로 전환
            anim_index = (anim_index + 1) % len(ANIMATIONS)  # 마지막 애니메이션 다음엔 처음으로
            repeat = 0
            delay(PAUSE_TIME)  # 다음 애니메이션으로 넘어가기 전 정지
    delay(FRAME_DELAY)

close_canvas()

