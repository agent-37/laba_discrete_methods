from cmath import cos, sin

import numpy as np


def norm_max(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    for i in range(len(vec_a)):
        buf_max = max(buf_max, abs(vec_a[i]))
    return buf_max.real



def w(vec):
    x, y = vec[0, 0], vec[1, 0]
    matr = np.matrix('1.0 1; 1 1')
    matr[0, 0] = -sin(x - 1).real
    matr[0, 1] = 1
    matr[1, 0] = 1
    matr[1, 1] = sin(y).real
    # print(matr)
    return matr


def func(vec):
    x, y = vec[0, 0], vec[1, 0]
    return np.matrix(((cos(x - 1) + y - 0.5).real,
                      (x - cos(y) - 3).real)).transpose()


prev_vec = np.matrix('0.1;0')
cur_vec = np.matrix('2; 50')

step = 0
eps = 0.001
while step < 10000 and abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
    prev_vec = cur_vec
    cur_vec = cur_vec - np.linalg.inv(w(cur_vec)) @ func(cur_vec)
    # print(cur_vec, revers_w(cur_vec),func(cur_vec))
    step += 1
print(step, cur_vec)
