from cmath import cos, sin
from sympy import sin, cos, Matrix, diff, solve, N
import numpy as np
from sympy.abc import x, y, t


def func():
    return Matrix([cos(x - 1) + y - 0.5, x - cos(y) - 3])


def fi():
    buf = Matrix([cos(x - 1) + y - 0.5, x - cos(y) - 3])
    return N(buf[0] ** 2 + buf[1] ** 2)


def g(vec):
    dp_fi_x = N(diff(fi(), x).limit(x, vec[0, 0]).limit(y, vec[1, 0]), 2)
    dp_fi_y = N(diff(fi(), y).limit(x, vec[0, 0]).limit(y, vec[1, 0]), 2)
    print(dp_fi_x, dp_fi_y)
    x1 = N(vec[0, 0] - t * dp_fi_x, 2)
    y1 = N(vec[1, 0] - t * dp_fi_y, 2)
    print(x1, y1, fi())
    g_t = N(fi().limit(x, x1).limit(y, y1), 2)

    return g_t


def find_dot_dp_g(vec):
    res = g(vec)
    dp_g = N(diff(res, t), 2)
    print('Here', dp_g)
    # Как решить это уравнение нужно первое решение большее 0 ????
    dots = solve(dp_g, t)
    if len(dots) == 0:
        print('Something happened')
    else:
        # Нужно найти не первый dot[0] а первый положительный то есть dot[i]>0
        dp_fi_x = N(diff(fi(), x).limit(x, vec[0, 0]).limit(y, vec[1, 0]))
        dp_fi_y = N(diff(fi(), y).limit(x, vec[0, 0]).limit(y, vec[1, 0]))
        return Matrix([vec[0, 0] - dots[0] * dp_fi_x, vec[1, 0] - dots[0] * dp_fi_y])


def grad(vec):
    dp_fi_x = N(diff(fi(), x).limit(x, vec[0, 0]).limit(y, vec[1, 0]), 2)
    dp_fi_y = N(diff(fi(), y).limit(x, vec[0, 0]).limit(y, vec[1, 0]), 2)
    return Matrix([dp_fi_x, dp_fi_y])


def norm_max(a):
    return max(abs(a[0, 0]), abs(a[1, 0]))


prev_vec = Matrix([10.1, 0])
cur_vec = Matrix([3.0, 1])

step = 0
eps = 0.000001
buf = 1
e1 = 0.99
while step < 1000 and abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
    print(step, buf, cur_vec)
    prev_vec = cur_vec
    buf *= e1
    cur_vec = cur_vec - buf * grad(cur_vec)
    # print(cur_vec, revers_w(cur_vec),func(cur_vec))
    step += 1
if fi().limit(x, cur_vec[0, 0]).limit(y, cur_vec[1, 0]) > 0.2:
    print('Wrong dot')
else:
    print('Ans')
    print(step, cur_vec)
