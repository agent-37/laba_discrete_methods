from cmath import cos, sin
from sympy import sin, cos, Matrix, diff, solve, N, integrate
import numpy as np
from sympy.abc import x, y, t
import scipy

eps = 1e-5


def func():
    return cos(t + x ** 2 + 0.5) / (2 + sin(x ** 2 + 1))


def f(x, t):
    return cos(t + x ** 2 + 0.5) / (2 + sin(x ** 2 + 1))


def f_t(t1):
    return func().limit(t, t1)


def find_square_rectangle(a, b, t, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * f(a + (i + 1 / 2) * h, t)
    return sum


def find_square_trapezoid(a, b, t, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * (f(a + i * h, t) + f(a + (i + 1) * h, t)) / 2
    return sum


def find_square_simpson(a, b, t, N):
    h = (b - a) / N
    sum = 0
    for i in range(N):
        sum += h * (f(a + i * h, t) + 4 * f(a + (i + 1 / 2) * h, t) + f(a + (i + 1) * h, t)) / 6
    return sum


def find_square(a, b, t, g):
    N = 4
    buf = g(a, b, t, N)
    while abs(buf - g(a, b, t, 2 * N)) > eps:
        buf = g(a, b, t, 2 * N)
        N *= 2
    print(buf, N, end=' |')


t1 = 0

c, d, Nt = map(float, input('Введите отрезок [c,d] для времени t и количество шагов\n').split())
a, b = map(float, input('Введите отрезок [a,b]\n').split())
print('Прямоугольники', 'Трапеции', 'Симпсон', sep='               ')
for i in range(round(Nt)):
    t1 = c + (d - c) / Nt * i
    print(t1, end=' |')
    find_square(a, b, t1, find_square_rectangle)
    find_square(a, b, t1, find_square_trapezoid)
    find_square(a, b, t1, find_square_simpson)


    def fx(x):
        global t1
        return cos(t1 + x ** 2 + 0.5) / (2 + sin(x ** 2 + 1))


    print(scipy.integrate.quad(fx, a, b))
