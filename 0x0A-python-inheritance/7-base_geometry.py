#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
