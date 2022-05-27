import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return x ** 4 - 4 * x ** 2 + 5


def dg(x):
    return 4 * x ** 3 - 8 * x


x_2 = np.linspace(-2, 2, 1000)

plt.figure(figsize=[10, 6])
plt.subplot(2, 1, 2)
plt.plot(x_2, g(x_2), color="red")
plt.show()