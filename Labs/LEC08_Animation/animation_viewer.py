from pico2d import *

# 스프라이트 시트 프레임 정보: (left, bottom, width, height), pico2d 좌표계(좌하단 원점)
ANIMATIONS = [
    ('idle', [
        (46, 845, 184, 154), (235, 845, 175, 155), (421, 845, 166, 155), (609, 845, 180, 157),
    ]),
    ('run', [
        (42, 652, 187, 163), (240, 653, 176, 163), (425, 653, 183, 163),
        (614, 655, 175, 160), (788, 653, 193, 163), (989, 653, 193, 171),
    ]),
    ('jump', [
        (42, 416, 148, 143), (239, 416, 158, 184), (444, 450, 180, 177),
        (645, 466, 200, 163), (863, 416, 255, 144),
    ]),
    ('attack', [
        (32, 202, 190, 149), (232, 201, 294, 208), (526, 201, 308, 194),
        (845, 201, 272, 142), (1133, 205, 191, 161), (1330, 205, 181, 161),
    ]),
    ('hurt', [
        (37, 25, 192, 151), (252, 25, 176, 132), (464, 25, 206, 145),
    ]),
]

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

grass = load_image('grass.png')
character = load_image('animation_sheet_knight.png')

frame = 0

while True:
    get_events()
    clear_canvas()
    grass.draw(400, 30)

    name, frames = ANIMATIONS[0]
    left, bottom, width, height = frames[frame]
    character.clip_draw(left, bottom, width, height, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

    update_canvas()
    frame = (frame + 1) % len(frames)
    delay(0.1)

close_canvas()

