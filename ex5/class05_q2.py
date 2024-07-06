import numpy as np
import matplotlib.pyplot as plt


def calc_discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def draw_quadratic(a, b, c, vertex):
    x = np.arange(vertex-10, vertex+10, 0.1)
    y = a * (x ** 2) + b * x + c

    plt.plot(x, y)


def solve_quadratic(a, b, c):
    D = calc_discriminant(a, b, c)
    if D < 0:
        print(f'The discriminant of the quadratic equation is {D}, which is negative. No real roots')
        return
    elif D == 0:
        x = -b / (2 * a)
        print(f'The quadratic root is {x}')
    else:
        x_1, x_2 = (-b + np.sqrt(D)) / (2 * a), (-b - np.sqrt(D)) / (2 * a)
        print(f'The quadratic roots are {x_1} and {x_2}')

    draw_quadratic(a, b, c, (-b/2*a))


solve_quadratic(1, -5, 6)
solve_quadratic(1, -5, 30)

plt.grid(True)
plt.show()


# Output from execution:
# The quadratic roots are 3.0 and 2.0
# The discriminant of the quadratic equation is -95, which is negative. No real roots
# 