# /usr/bin/python3.5

import turtle
import math


class Figure:

    def __init__(self, a):
        # self.__circle__((0, 0), 140, a)
        # self.__rectangle__([(0, 0), (100, 50)], a)
        # self.__line__([(0, 0), (100, 50)], a)
        # self.__triangle__([(0, 0), (100, 50), (300, -80)], a)
        self.__my_cos__([(-300.0, 100.0), (300.0, 100.0)], 5.0, a)

    def __line__(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        a.setpos(points[1])
        a.penup()

    def __circle__(self, start_point, radius, a):
        a.setheading(90)
        a.penup()
        a.goto(start_point[0] + radius, start_point[1])
        a.pendown()
        a.circle(radius)
        a.penup()

    def __rectangle__(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        a.setpos(points[1][0], points[0][1])
        a.setpos(points[1])
        a.setpos(points[0][0], points[1][1])
        a.setpos(points[0])
        a.penup()

    def __triangle__(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        for i in points:
            a.setpos(i)
        a.setpos(points[0])
        a.penup()

    def __my_cos__(self, points, deth_cos, a):
        a.penup()
        a.setpos(points[0])
        a.pendown()
        i = points[0][0]
        while i <= points[1][0]:
            y = math.cos(i)*deth_cos + points[0][1]
            a.setpos(i, y)
            i += 5.0
        a.penup()


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    Figure(my_turtle)
    turtle.done()

if __name__ == "__main__":
    main()
