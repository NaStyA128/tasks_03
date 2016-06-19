#!/usr/bin/python3.5
# Goloviznina Anastasiya

import turtle
import json
from math import cos

cmds = {}
ar = {}


def commands(func):
    global cmds
    cmds[func.__name__] = func
    return func


"""
def decor(method):
    def wrapper(self, *args):
        # ar[method.__name__] = method(self, *args)
        print(args)
        print('hi')
        return method(self, *args)
    return wrapper

"""


class Figure(object):

    commands_list = cmds
    a = 0
    file = []

    def __init__(self):
        print('\nHi! It is a grafics editor. '
              'You can enter the following commands: \n')
        for i in self.commands_list:
            print('- ' + i)
        while True:
            command = input('\nEnter command: ')
            h = {self.commands_list[command].__name__: self.commands_list[command]()}
            self.file.append(h)

        # self.my_func(10, 10)

    """
    def my_func(self, *args):
        print('args')

    """

    @commands
    def new_file(self):
        self.a = turtle.Turtle()
        self.a.speed(10)
        return 1

    @commands
    def save_file(self):
        file_name = input('Enter files name: ')
        f = open(file_name, 'a+')
        f.write(json.dumps(self.file))
        f.close()
        return 1

    @commands
    def open_file(self):
        file_name = input('Enter files name: ')
        f = open(file_name)
        text = f.read()
        self.file = json.loads(text)
        print(self.file)

    @commands
    def set_pen_color(self):
        color = input('Enter color: ')
        self.a.pencolor(color)
        return color

    @commands
    def set_pen_size(self):
        size = input('Enter size: ')
        self.a.pensize(size)
        return size

    @commands
    def set_fill_color(self):
        color = input('Enter color: ')
        self.a.fillcolor(color)
        return color

    def input_point(self, count):
        points = []
        point = []
        i = 0
        while i < count:
            print('Enter point: ')
            point.append(int(input('x = ')))
            point.append(int(input('y = ')))
            points.append(point)
            point = []
            i += 1
        return points

    @commands
    def line(self):
        points = self.input_point(2)
        self.a.setheading(0)
        self.a.penup()
        self.a.goto(points[0])
        self.a.pendown()
        self.a.setpos(points[1])
        self.a.penup()
        return points

    @commands
    def rectangle(self):
        points = self.input_point(2)
        self.a.setheading(0)
        self.a.penup()
        self.a.goto(points[0])
        self.a.pendown()
        self.a.begin_fill()
        self.a.setpos(points[1][0], points[0][1])
        self.a.setpos(points[1])
        self.a.setpos(points[0][0], points[1][1])
        self.a.setpos(points[0])
        self.a.end_fill()
        self.a.penup()
        return points

    @commands
    def triangle(self):
        points = self.input_point(3)
        self.a.setheading(0)
        self.a.penup()
        self.a.goto(points[0])
        self.a.pendown()
        self.a.begin_fill()
        for i in points:
            self.a.setpos(i)
        self.a.setpos(points[0])
        self.a.end_fill()
        self.a.penup()
        return points

    @commands
    def circle(self):
        self.a.setheading(90)
        start_point = []
        print('Enter central point: ')
        start_point.append(int(input('x = ')))
        start_point.append(int(input('y = ')))
        radius = int(input('Enter radius: '))
        self.a.penup()
        self.a.goto(start_point[0] + radius, start_point[1])
        self.a.pendown()
        self.a.begin_fill()
        self.a.circle(radius)
        self.a.end_fill()
        self.a.penup()
        return [start_point, radius]

    @commands
    def my_cos(self):
        points = self.input_point(2)
        print('Input zip: ')
        deth_cos = float(input())
        self.a.penup()
        self.a.setpos(points[0])
        self.a.pendown()
        i = points[0][0]
        while i <= points[1][0]:
            y = cos(i) * deth_cos + points[0][1]
            self.a.setpos(i, y)
            i += 5.0
        self.a.penup()
        return [points, deth_cos]


def main():
    s = Figure()


if __name__ == '__main__':
    main()
