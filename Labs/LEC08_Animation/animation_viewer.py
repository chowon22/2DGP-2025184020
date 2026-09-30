from pico2d import *

# 스프라이트 시트 프레임 정보: (left, bottom, width, height, anchor_x), pico2d 좌표계(좌하단 원점)
# anchor_x: 프레임 왼쪽 끝에서 두 발 사이 중점까지의 거리 (x 보정용)
ANIMATIONS = [
    ('idle', [
        (46, 845, 184, 154, 83), (235, 845, 175, 155, 80), (421, 845, 166, 155, 75), (609, 845, 180, 157, 81),
    ]),
    ('run', [
        (42, 652, 187, 163, 76), (240, 653, 176, 163, 66), (425, 653, 183, 163, 68),
        (614, 655, 175, 160, 58), (788, 653, 193, 163, 76), (989, 653, 193, 171, 48),
    ]),
    ('jump', [
        (42, 416, 148, 143, 87), (239, 416, 158, 184, 66), (444, 450, 180, 177, 50),
        (645, 466, 200, 163, 58), (863, 416, 255, 144, 69),
    ]),
    ('attack', [
        (32, 202, 190, 149, 88), (232, 201, 294, 208, 80), (526, 201, 308, 194, 57),
        (845, 201, 272, 142, 66), (1133, 205, 191, 161, 71), (1330, 205, 181, 161, 81),
    ]),
    ('hurt', [
        (37, 25, 192, 151, 93), (252, 25, 176, 132, 60), (464, 25, 206, 145, 86),
    ]),
]

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_DELAY = 0.08
SCALE = 2
FOOT_Y = 150  # 캐릭터 발이 놓일 화면 y좌표

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

grass = load_image('grass.png')
character = load_image('animation_sheet_knight.png')

frame = 0

while True:
    get_events()
    clear_canvas()
    grass.draw(400, 30)

    name, frames = ANIMATIONS[0]
    left, bottom, width, height, anchor_x = frames[frame]
    # 프레임마다 높이가 달라도 발 위치가 고정되도록 중심 y좌표 보정
    base = min(f[1] for f in frames)
    y = FOOT_Y + (bottom - base) * SCALE + height * SCALE // 2
    # 프레임마다 캐릭터 위치가 달라도 발이 화면 중앙에 오도록 중심 x좌표 보정
    x = CANVAS_WIDTH // 2 + (width // 2 - anchor_x) * SCALE
    character.clip_draw(left, bottom, width, height, x, y,
                        width * SCALE, height * SCALE)

    update_canvas()
    frame = (frame + 1) % len(frames)
    delay(FRAME_DELAY)

close_canvas()

