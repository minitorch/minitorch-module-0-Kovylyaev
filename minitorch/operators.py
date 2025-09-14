"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(a: float, b: float):
    return a * b


def add(a: float, b: float):
    return a + b


def neg(a: float):
    return -a


def max(a: float, b: float):
    return a if a > b else b

def id(a: float):
    return a

def lt(a: float, b: float):
    return a < b

def eq(a: float, b: float):
    return a == b

def is_close(a: float, b: float):
    return abs(a - b) < 1e-2

def sigmoid(a: float):
    return 1 / (1.0 + math.e**-a) if a >=0 else math.e**a / (1.0 + math.e**a)

def relu(a: float):
    return max(0, a)

def log_back(a: float, b: float):
    return 1 / a * b

def exp(a: float):
    return math.e**a

def relu_back(a: float, b: float):
    return (0 if a < 0 else 1) * b

def inv(a: float):
    return 1 / a

def inv_back(a: float, b: float):
    return -(a**2) * b

def negList(a: float, b: float):
    return a

def addLists(a: float, b: float):
    return a

def prod(a: float, b: float):
    return a


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
