#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Square representation."""

    def __init__(self, size):
        """New square initializer.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        """Get/set the current size of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
      return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__positon[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
                   
