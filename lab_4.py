from cmath import cos, sin
from sympy import sin, cos, Matrix, diff, solve, N
import numpy as np
from sympy.abc import x, y, t

eps = 1e-5


def func():
    return np.e ** (-x)


def f(num):
    return func().limit(x, num)


def find_square_rectangle(a, b, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * f(a + (i + 1 / 2) * h)
    return sum


def find_square_trapezoid(a, b, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * (f(a + i * h) + f(a + (i + 1) * h)) / 2
    return sum


def find_square_simpson(a, b, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * (f(a + i * h) + 4 * f(a + (i + 1 / 2) * h) + f(a + (i + 1) * h)) / 6
    return sum


def find_square(a, b, g):
    N = 4
    buf = g(a, b, N)
    while (abs(buf - g(a, b, 2 * N)) > eps):
        buf = g(a, b, 2 * N)
        N *= 2
    print(buf, g(a, b, 2 * N), N)


a, b = map(float, input('Введите отрезок [a,b]\n').split())
find_square(a, b, find_square_rectangle)
find_square(a, b, find_square_trapezoid)
find_square(a, b, find_square_simpson)