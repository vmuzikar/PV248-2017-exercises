from pygame import display, draw, time, event
import pygame
from random import randint


class Circle:
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius


resolution = [800, 600]
max_circles = 10
starting_radius = 5
thickness = 3
circles = []
clock = time.Clock()

# init display
screen = display.set_mode(resolution)

while True:
    ev = event.poll()
    if ev.type is pygame.KEYDOWN:
        break

    for circle in circles:
        circle.radius += 1  # circle growth

        # checking collisions
        left = (circle.center[0] - circle.radius) < 0
        right = (circle.center[0] + circle.radius) > resolution[0]
        top = (circle.center[1] - circle.radius) < 0
        bottom = (circle.center[1] + circle.radius) > resolution[1]

        if left or right or top or bottom:
            circles.remove(circle)

    # adding new circles
    for i in range(max_circles - len(circles)):
        color = [randint(20, 255), randint(20, 255), randint(20, 255)]
        center = [randint(starting_radius + 10, resolution[0] - starting_radius - 10), randint(starting_radius + 10, resolution[1] - starting_radius - 10)]
        circles.append(Circle(color, center, starting_radius))

    screen.fill([0, 0, 0])  # clear the screen

    # drawing circles
    for circle in circles:
        draw.circle(screen, circle.color, circle.center, circle.radius, thickness)

    display.flip()
    clock.tick(60)
