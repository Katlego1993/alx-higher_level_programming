#!/usr/bin/python3
"""Square defined."""

class Square:
    """Square representation"""
    def__init__(self, size=0):
        """Initialize a new Square.
        Args:
        size (int): Size of new Square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
