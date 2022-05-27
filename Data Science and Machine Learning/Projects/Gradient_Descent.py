# Import Statements

import numpy as np
import matplotlib.pyplot as plt


# Code
"""Functions"""


def f(x):
    return x ** 2 + x + 1


def g(x):
    return x ** 4 - 4 * x ** 2 + 5


# Derivatives
def df(x):
    return 2 * x + 1


def dg(x):
    return 4 * x ** 3 - 8 * x


def h(x):
    return x ** 5 - 2 * x ** 4 + 2


def dh(x):
    return 5*x**4 - 8*x**3


# Variables

# x_1 = np.linspace(start=-3, stop=3, num=500)
# x_2 = np.linspace(-3, 3, 500)
x_3 = np.linspace(start=-2.5, stop=2.5, num=1000)


# Gradient Descent
def gradient_descent(derivative_func, initial_guess, multiplier=0.01, precision=0.001, max_iter=300):
    new_x = initial_guess
    x_list = [new_x]
    slope_list = [derivative_func(new_x)]

    for n in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - multiplier * gradient

        step_size = abs(new_x - previous_x)
        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))

        if step_size < precision:
            break
    return new_x, slope_list, x_list


data_tuple = gradient_descent(derivative_func=dh, initial_guess=1.9)


print(len(data_tuple[1]))
