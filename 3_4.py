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


prev_vec = np.matrix('10.1;0')
cur_vec = np.matrix('3.0; 1')

print(find_dot_dp_g(Matrix([3.034, -0.093])))

#
# step = 0
# eps = 0.001
# while step < 1000 and abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
#     prev_vec = cur_vec
#     cur_vec = cur_vec - find_lambda(cur_vec) * w(cur_vec).transpose() @ func(cur_vec)
#     # print(cur_vec, revers_w(cur_vec),func(cur_vec))
#     step += 1
# if fi(cur_vec) > 0.2:
#     print('Wrong dot')
# else:
#     print(step, cur_vec)
