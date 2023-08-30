#!/usr/bin/python3
"""Square class defined."""


class Square:
    """Square representation."""

    def __init__(self, size=0):
        """New Square initializer.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
