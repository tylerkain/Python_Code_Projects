import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from sympy import symbols, diff


def f(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 1 / (r + 1)


multiplier = .1
max_iter = 200
params = np.array([1.8, 1.0])
values_array = params.reshape(1, 2)


def f(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 1 / (r + 1)


x_1 = np.linspace(start=-3, stop=3, num=32)
y_1 = np.linspace(start=-3, stop=3, num=32)

x_1, y_1 = np.meshgrid(x_1, y_1)

fig = plt.figure(figsize=[16, 12])
ax = plt.axes(projection='3d')

ax.plot_surface(x_1, y_1, f(x_1, y_1), cmap=cm.autumn)
# plt.show()

a, b = symbols('x, y')

cost = f(a, b).evalf(subs={a: 1.8, b: 1.0})

for n in range(max_iter):
    gradient_x = diff(f(a, b), a).evalf(subs={a: params[0], b: params[1]})
    gradient_y = diff(f(a, b), b).evalf(subs={a: params[0], b: params[1]})
    gradients = np.array([gradient_x, gradient_y])
    params = params - multiplier * gradients

# print(gradients)
# print(params[0], params[1])

kirk = np.array([['Captain', 'Enterprise']])
