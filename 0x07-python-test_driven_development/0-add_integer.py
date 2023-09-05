#!/usr/bin/python3

"""Integer addition function define."""

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b.
    Float arguments are typecasted to ints before addition id performed.
    Raises:
      TypeError: If either of a or b is a non-onteger and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
