from cmath import cos, sin
from sympy import sin, cos, Matrix
import numpy as np
from sympy.abc import x, y


def norm_max(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    #print(vec_a)
    for i in range(len(vec_a)):
        buf_max = max(buf_max, abs(vec_a[i]))
    return buf_max


def w(vec):
    dp = Matrix([x, y])
    matr = func().jacobian(dp)
    return matr.limit(x, vec[0, 0]).limit(y, vec[1, 0])


def func():
    # return np.matrix(((cos(x - 1) + y - 0.5).real,
    #                   (x - cos(y) - 3).real)).transpose()
    return Matrix([cos(y - 1) + x - 0.8, y - cos(x) - 2])


def colculate_func(vec):
    return func().limit(x, vec[0, 0]).limit(y, vec[1, 0])



prev_vec = Matrix([0.1,0])
cur_vec = Matrix([1.0, 1.0])


step = 0
eps = 0.0000001

while step < 1000 and abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
    prev_vec = cur_vec
    cur_vec = cur_vec - w(cur_vec).inv(method="LU") * colculate_func(cur_vec)
    # print(cur_vec, revers_w(cur_vec),func(cur_vec))
    step += 1
print(step, cur_vec)
