from cmath import cos, sin

import numpy as np


def norm_max(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    for i in range(len(vec_a)):
        buf_max = max(buf_max, abs(vec_a[i]))
    return buf_max.real


def revers_w(vec):
    x, y = vec[0, 0], vec[1, 0]
    buf = (-sin(x - 1) * sin(y) - 1).real
    matr = np.matrix('1.0 1; 1 1')
    matr[0, 0] = sin(y).real / buf
    matr[0, 1] = -1 / buf
    matr[1, 0] = -1 / buf
    matr[1, 1] = -sin(x - 1).real / buf
    # print(matr)
    return matr


def w(vec):
    x, y = vec[0, 0], vec[1, 0]
    matr = np.matrix('1.0 1; 1 1')
    matr[0, 0] = -sin(x - 1).real
    matr[0, 1] = 1
    matr[1, 0] = 1
    matr[1, 1] = sin(y).real
    # print(matr)
    return matr


def transponse_w(vec):
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
    return np.matrix(((cos(x - 1).real + y - 0.5),
                      (x - cos(y).real - 3).real)).transpose()


def fi(vec):
    x, y = vec[0, 0], vec[1, 0]
    return (cos(x - 1).real + y - 0.5) ** 2 + (x - cos(y).real - 3) ** 2


def cross(a, b):
    return (a[0, 0] * b[0, 0] + a[1, 0] * b[1, 0]).real


def find_lambda(vec):
    x, y = vec[0, 0], vec[1, 0]
    return cross(vec, w(vec) @ w(vec).transpose() @ vec) / cross(w(vec) @ w(vec).transpose() @ vec,
                                                                w(vec) @ w(vec).transpose() @ vec)


prev_vec = np.matrix('10.1;0')
cur_vec = np.matrix('3.0; 1')

step = 0
eps = 0.001
while step < 1000 and abs(norm_max(cur_vec - prev_vec) / norm_max(prev_vec)) > eps:
    prev_vec = cur_vec
    cur_vec = cur_vec - find_lambda(cur_vec) * w(cur_vec).transpose() @ func(cur_vec)
    # print(cur_vec, revers_w(cur_vec),func(cur_vec))
    step += 1
if fi(cur_vec) > 0.2:
    print('Wrong dot')
else:
    print(step, cur_vec)
