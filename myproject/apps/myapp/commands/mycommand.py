#!/usr/bin/env python

"""
Command to demonstrate a bug in Pylint w.r.t. imports.
The import in this file works fine as far as Python's concerned, but Pylint
incorrectly flags it as invalid.
"""
from myproject.classes import MyClass

if __name__ == '__main__':
    MyClass().say_hello()
