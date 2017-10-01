#!/usr/bin/env python3

import turtle
import math


def drawHouse(count = 2):
    wallSize = 90
    roofHeight = 60

    roofSize = math.sqrt(math.pow(wallSize / 2, 2) + math.pow(roofHeight, 2))
    roofAngle = math.degrees(math.asin(roofHeight / roofSize))

    wallColor = "brown"
    roofColor = "red"

    margin = 20  # between houses

    # heading, distance, color
    directions = [
        (270, wallSize, wallColor),
        (0, wallSize, wallColor),
        (90, wallSize, wallColor),
        (180, wallSize, wallColor),
        (roofAngle, roofSize, roofColor),
        (-roofAngle, roofSize, roofColor)
    ]

    while count:
        turtle.pd()
        for heading, distance, color in directions:
            turtle.color(color)
            turtle.seth(heading)
            turtle.forward(distance)
        turtle.pu()
        turtle.seth(0)
        turtle.forward(margin)
        count -= 1


def main():
    turtle.shape("turtle")
    drawHouse(3)
    turtle.exitonclick()


if __name__ == "__main__":
    main()