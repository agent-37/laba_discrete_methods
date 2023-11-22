from cmath import cos, sin

import numpy as np


def norm_max(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    for i in range(len(vec_a)):
        buf_max = max(buf_max, abs(vec_a[i]))
    return buf_max.real


def revers_w(vec):
    x, y = vec[0,0], vec[1,0]
    matr = np.matrix('1 1; 1 1')
    matr[0, 0] = 2 * y / (2 * y * cos(x + y) - 2 * x * cos(y + x) - 11 / 5 * y)
    matr[0, 1] = -cos(y + x) / (2 * y * cos(y + x) - 2 * x * cos(y + x) - 11 / 5 * y)
    matr[1, 0] = -2 * x / (2 * y * cos(y + x) - 2 * x * cos(y + x) - 11 / 5 * y)
    matr[1, 1] = (cos(y + x) - 11 / 10) / (2 * y * cos(y + x) - 2 * x * cos(y + x) - 11 / 5 * y)
    return matr


def func(vec):
    x, y = vec[0], vec[1]
    return np.matrix(((sin(x[0, 0] + y[0, 0]) - 1.1 * x[0, 0] - 0.1).real,
                      (x[0, 0] * x[0, 0] + y[0, 0] * y[0, 0] - 1).real)).transpose()


prev_vec = np.matrix('0.1;0')
cur_vec = np.matrix('0.6;0.8')

step = 0
eps = 0.0001
while step < 1000 or abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
    prev_vec = cur_vec
    cur_vec = cur_vec - revers_w(cur_vec) @ func(cur_vec)
    step += 1
print(step, cur_vec)
