from cmath import sin, log
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy


def func(x):
    # Функция данная в условии
    return (x ** 2 + 4 * sin(x)).real


def find_new_x(l, r, sign, cur_x):
    e = func(l)
    if e > 0:
        e = 1
    else:
        e = 0
    s = 0
    if sign == 1:
        s = 1
    else:
        s = 0
    if (e + s) % 2 == 0:
        return l - (func(l) * (cur_x - l)) / (func(cur_x) - func(l))
    else:
        return cur_x - (func(cur_x) * (r - cur_x)) / (func(r) - func(cur_x))


def find_x_0(l, r, sign):
    e = func(l)
    if e > 0:
        e = 1
    else:
        e = 0
    if sign == 1:
        s = 1
    else:
        s = 0
    if (e + s) % 2 == 0:
        return r
    else:
        return l


def func_pd_2(x):
    res = scipy.misc.derivative(func, x, dx=1e-6, n=2)
    return (res).real


def check(l, r):
    flag_neg, flag_pos = 0, 0
    for i in range(1000):

        buf = func_pd_2(l + (r - l) / 1000 * i)
        if buf > 0:
            flag_pos = 1
        else:
            flag_neg = 1
    if flag_neg == 1 and flag_pos == 1:
        return False
    else:
        if flag_neg == 1:
            return -1
        else:
            return 1

#
# xmin =-5
# xmax = 5
# count = 200
# xlist = np.linspace(xmin, xmax, count)
# ylist = [func(x) for x in xlist]
# plt.plot(xlist, ylist)
# plt.show()


print('Введите отрезок на котором хотите найти корень')
l, r = map(float, input().split())
if check(l, r):
    sign = check(l, r)
    eps = 0.000001
    present_x = -1e18
    cur_x = find_x_0(l, r, sign)
    step = 0
    while abs(cur_x - present_x) > eps or step > 1000:
        step += 1
        present_x = cur_x
        cur_x = find_new_x(l, r, sign, cur_x)
        # print(cur_x, present_x)
    print(step, cur_x)
else:
    print('Вторая производная имеет разные знаки на отрезке')
