# https://github.com/FNCYMonk/lab11-GA-DA
# Partner 1: Graham Avidano
# Partner 2: Daniel Atkins

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


def exponent(a, b):
    return a ** b
#import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b): #a is denominator
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return b / a

def log(a, b): #a is base
    if b <= 0:
        raise ValueError("Can't log negative number or zero.")
    if a<=0 or a == 1:
        raise ValueError("Can't log with a base of a negative number, 1, or 0,")
    return math.log(b,a)

def exp(a, b):
    return a**b

