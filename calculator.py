"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:  # or check depending on your division order (raise ZeroDivisionError if divisor is 0)
        raise ZeroDivisionError
    return b / a

def log(a, b):
    # use math library + raise ValueError for invalid inputs/base
    if ...:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b


