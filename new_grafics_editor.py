#!/usr/bin/python3.5
# Goloviznina Anastasiya

import turtle

cmds = {}


def commands(func):
    global cmds
    cmds[func.__name__] = func
    return func


class Figure(object):

    commands_list = cmds

    def __init__(self, command):
        print(self.commands_list[command])
        self.commands_list[command](self, 4)
        # self.my_func = decor(self.my_func)
        # self.my_func(a)

    @commands
    def my_func(self, a):
        print(a * a)
    # my_func = decor(my_func)


def main():
    s = Figure('my_func')


if __name__ == '__main__':
    main()
