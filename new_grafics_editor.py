#!/usr/bin/python3.5
# Goloviznina Anastasiya

import turtle
import json
from math import cos
# from sys import exit

cmds = {}


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
    file_name = ''

    def __init__(self):
        print('\nHi! It is a grafics editor. '
              'You can enter the following commands: \n')
        for i in self.commands_list:
            print('- ' + i)
        while True:
            command = input('\nEnter command: ')
            # ключ в словаре (значение под этим ключом)
            h = {self.commands_list[command].__name__:
                 self.commands_list[command](self)}
            if self.commands_list[command].__name__ != 'open_file':
                self.file.append(h)

        # self.my_func(10, 10)

    """
    def my_func(self, *args):
        print('args')

    """

    @commands
    def new_file(self, *args):
        self.a = turtle.Turtle()
        self.a.speed(10)
        return 1

    @commands
    def save_file(self):
        file_name = self.file_name and self.file_name or \
                    input('Enter files name: ')
        f = open(file_name, 'w')
        f.write(json.dumps(self.file))
        f.close()
        return 1

    @commands
    def open_file(self, *args):
        self.file_name = args and args[0] or input('Enter files name: ')
        f = open(self.file_name, 'r')
        text = f.read()
        f.close()
        self.file = json.loads(text)
        for line in self.file:
            for key in line:
                self.commands_list[key](self, line[key])
        return self.file_name

    @commands
    def set_pen_color(self, *args):
        color = args and args[0] or input('Enter color: ')
        self.a.pencolor(color)
        return color

    @commands
    def set_pen_size(self, *args):
        size = args and args[0] or input('Enter size: ')
        self.a.pensize(size)
        return size

    @commands
    def set_fill_color(self, *args):
        color = args and args[0] or input('Enter color: ')
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
    def line(self, *args):
        points = args and args[0] or self.input_point(2)
        self.a.setheading(0)
        self.a.penup()
        self.a.goto(points[0])
        self.a.pendown()
        self.a.setpos(points[1])
        self.a.penup()
        return points

    @commands
    def rectangle(self, *args):
        points = args and args[0] or self.input_point(2)
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
    def triangle(self, *args):
        points = args and args[0] or self.input_point(3)
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
    def circle(self, *args):
        start_point = []
        self.a.setheading(90)
        if args:
            start_point = args[0][0]
            radius = args[0][1]
        else:
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
    def my_cos(self, *args):
        if args:
            points = args[0][0]
            deth_cos = args[0][1]
        else:
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

    @commands
    def exit(self):
        exit()


def main():
    s = Figure()


if __name__ == '__main__':
    main()
