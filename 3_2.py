from cmath import sin, log
from cmath import sin, log
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy


def func(x):
    # Функция данная в условии
    return (x - 1 + 1 / 2 * np.e ** x).real
    #return (5 * x - np.e ** x).real


def func_pd_n(x, step):
    res = scipy.misc.derivative(func, x, dx=1e-6, n=step)
    return (res).real


def check(l, r):
    flag_neg, flag_pos = 0, 0
    eps = 0.001
    help = 100000
    for i in range(help):
        if abs(func_pd_n(l + (r - l) / help * i, 1)) < eps:
            return False
        buf = func_pd_n(l + (r - l) / help * i, 2)
        if buf > 0:
            flag_pos = 1
        else:
            flag_neg = 1
    if flag_neg == 1 and flag_pos == 1:
        return False
    return True


def find_new_x(cur_x):
    return cur_x - func(cur_x) / func_pd_n(cur_x, 1)


print('Введите отрезок на котором хотите найти корень')
l, r = map(float, input().split())
if check(l, r):
    eps = 0.0001
    present_x = -1e18
    cur_x = (r + l) / 2
    step = 0
    while abs(cur_x - present_x) > eps or step > 1000:
        step += 1
        present_x = cur_x
        cur_x = find_new_x(cur_x)
    print(step, cur_x)
else:
    print('отрезок не прошел проверку')
