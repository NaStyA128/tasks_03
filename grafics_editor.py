#!/usr/bin/python3.5
# Goloviznina Nastya

import turtle
import math

COMMANDS = ['draw_line', 'draw_rectangle', 'draw_triangle',
            'draw_circle', 'draw_cos_line', 'quit']


class Figure:

    cmds = []

    def __init__(self, a, type):
        self.cmds[type]
        print('Input pencolor: ')
        pc = input()
        a.pencolor(pc)
        print('Input fillcolor: ')
        fc = input()
        a.fillcolor(fc)
        if type == COMMANDS[0]:
            points = self.input_point(2)
            self.line(points, a)
        elif type == COMMANDS[1]:
            points = self.input_point(2)
            self.rectangle(points, a)
        elif type == COMMANDS[2]:
            points = self.input_point(3)
            self.triangle(points, a)
        elif type == COMMANDS[3]:
            point = []
            print('Input central point: ')
            point.append(int(input('x = ')))
            point.append(int(input('y = ')))
            print('Input radius: ')
            r = int(input())
            self.circle(point, r, a)
        elif type == COMMANDS[4]:
            points = self.input_point(2)
            print('Input zip: ')
            zip = float(input())
            self.my_cos(points, zip, a)
        elif type == COMMANDS[5]:
            quit()
        else:
            print('Error')

    def input_point(self, count):
        points = []
        point = []
        i = 0
        while i < count:
            print('Input point: ')
            point.append(int(input('x = ')))
            point.append(int(input('y = ')))
            points.append(point)
            point = []
            i += 1
        return points

    def line(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        a.setpos(points[1])
        a.penup()

    def circle(self, start_point, radius, a):
        a.setheading(90)
        a.penup()
        a.goto(start_point[0] + radius, start_point[1])
        a.pendown()
        a.begin_fill()
        a.circle(radius)
        a.end_fill()
        a.penup()

    def rectangle(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        a.begin_fill()
        a.setpos(points[1][0], points[0][1])
        a.setpos(points[1])
        a.setpos(points[0][0], points[1][1])
        a.setpos(points[0])
        a.end_fill()
        a.penup()

    def triangle(self, points, a):
        a.setheading(0)
        a.penup()
        a.goto(points[0])
        a.pendown()
        a.begin_fill()
        for i in points:
            a.setpos(i)
        a.setpos(points[0])
        a.end_fill()
        a.penup()

    def my_cos(self, points, deth_cos, a):
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
    while True:
        print("Input command")
        type = input()
        Figure(my_turtle, type)
    turtle.done()

if __name__ == "__main__":
    main()
