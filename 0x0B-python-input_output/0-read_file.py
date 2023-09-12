#!/usr/bin/python3
"""Defines a text file reading function."""
def read_file(filename=""):
    """function that reads a text file and prints it"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
