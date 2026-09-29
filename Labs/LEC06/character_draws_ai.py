from math import *
from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_DELAY = 0.01

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
character = load_image("character.png")


def draw_frame(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)
    get_events()


def move_steps(start, direction, count):
    x, y = start
    dx, dy = direction
    for _ in range(count):
        x += dx
        y += dy
        draw_frame(x, y)


def move_along_path(points, steps=100):
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        for t in range(steps):
            draw_frame(x1 + (x2 - x1) * t / steps, y1 + (y2 - y1) * t / steps)


def move_circle(center=(400, 300), radius=100):
    print("Circle")
    cx, cy = center
    for angle in range(360):
        x = cx + radius * sin(radians(angle))
        y = cy + radius * cos(radians(angle))
    draw_frame(x, y)


def move_rectangle():
    print("Rectangle")
    # (시작점, 방향, 이동 횟수)
    segments = [
        ((400, 400), (1, 0), 101),
        ((500, 400), (0, -1), 201),
        ((500, 200), (-1, 0), 201),
        ((300, 200), (0, 1), 201),
        ((300, 400), (1, 0), 100),
    ]
    for start, direction, count in segments:
        move_steps(start, direction, count)


def move_triangle():
    print("Triangle")
    move_along_path([(400, 400), (500, 300), (300, 300), (400, 400)])


def main():
    while True:
        move_circle()
        move_rectangle()
        move_triangle()


if __name__ == "__main__":
    main()
