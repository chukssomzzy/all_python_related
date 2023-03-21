#!/usr/bin/python3

"""Create a widget"""

class Widget:
    def __init__(self, name):
        self.name = name
        self.__width = 50
        self.__height = 50
    def size(self):
        return (self.__width, self.__height)
    def resize(self, width, height):
        self.__width = width
        self.__height = height
    def dispose(self):
        pass
