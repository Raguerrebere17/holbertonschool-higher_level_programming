#!/usr/bin/python3
""" 11-square Module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class of the Square that inheritances an Rectangle"""
    def __init__(self, size):
        """Method init"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init(size, size)

    def area(self):
        """Method area"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
