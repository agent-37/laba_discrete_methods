from cmath import e

import matplotlib.pyplot as plt


def f(t, x):
    return t * x


def sys_f_x(t, x, y):
    # return y
    return 2 + y - x ** 2


def sys_f_y(t, x, y):
    # return -y / t - x
    return 2 * x * (x - y)


def f_e(t):
    return e ** (t ** 2 / 2).real


def R_K_2(t_0, x_0, a, b, h):
    points_t, points_x, pe_x = [t_0], [x_0], [x_0]
    while t_0 < b:
        x_0 += h * f(t_0 + h / 2, x_0 + h / 2 * f(t_0, x_0))
        points_t.append(t_0 + h)
        points_x.append(x_0)
        pe_x.append(f_e(t_0 + h))
        t_0 += h
    plt.plot(points_t, points_x)
    plt.plot(points_t, pe_x)
    print('t', 'Runge-Kutte', 'True x(t)', 'dif', sep='        ')
    for i in range(len(points_t)):
        print(points_t[i], points_x[i], pe_x[i], abs(points_x[i] - pe_x[i]))
    plt.show()


def R_K_4(t_0, x_0, a, b, h):
    points_t, points_x, pe_x = [t_0], [x_0], [x_0]
    while t_0 < b:
        k1 = h * f(t_0, x_0)
        k2 = h * f(t_0 + h / 2, x_0 + k1 / 2)
        k3 = h * f(t_0 + h / 2, x_0 + k2 / 2)
        k4 = h * f(t_0 + h, x_0 + k3)
        x_0 += 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        points_t.append(t_0 + h)
        points_x.append(x_0)
        pe_x.append(f_e(t_0 + h))
        t_0 += h
    plt.plot(points_t, points_x)
    plt.plot(points_t, pe_x)
    print('t', 'Runge-Kutte', 'True x(t)', 'dif', sep='        ')
    for i in range(len(points_t)):
        print(points_t[i], points_x[i], pe_x[i], abs(points_x[i] - pe_x[i]))
    plt.show()


def R_K_4_S(t_0, x_0, y_0, a, b, h):
    points_x, points_y = [], []
    # h = 0.001
    while t_0 < b:
        k1 = h * sys_f_x(t_0, x_0, y_0)
        q1 = h * sys_f_y(t_0, x_0, y_0)
        k2 = h * sys_f_x(t_0 + h / 2, x_0 + k1 / 2, y_0 + q1 / 2)
        q2 = h * sys_f_y(t_0 + h / 2, x_0 + k1 / 2, y_0 + q1 / 2)
        k3 = h * sys_f_x(t_0 + h / 2, x_0 + k2 / 2, y_0 + q2 / 2)
        q3 = h * sys_f_y(t_0 + h / 2, x_0 + k2 / 2, y_0 + q2 / 2)
        k4 = h * sys_f_x(t_0 + h, x_0 + k3, y_0 + q3)
        q4 = h * sys_f_y(t_0 + h, x_0 + k3, y_0 + q3)
        x_0 += 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_0 += 1 / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
        points_x.append(x_0)
        points_y.append(y_0)
        t_0 += h
    plt.plot(points_x, points_y)
    # plt.show()


# a, b = 0, 1
# t_0, x_0, h = 0, 1, 0.1
# R_K_2(t_0, x_0, a, b, h)

# a, b = 0, 1
# t_0, x_0, h = 0, 1, 0.1
# R_K_4(t_0, x_0, a, b, h)
#
# a, b = 1, 12
# t_0, x_0, y_0, h = 1, 0.7, -0.4, 0.1
# R_K_4_S(t_0, x_0, y_0, a, b, h)

# В варианте №8 из Матвеева для лабораторных работ, есть 3 точки равновесия (-1,-1),(0,-2),(2,2)
t_0, h = 0, 0.01
a, b = 0, 2
eps=0.01
R_K_4_S(t_0, -1-eps, -1, a, b, h)
R_K_4_S(t_0, -1+eps, -1, a, b, h)
R_K_4_S(t_0, -1, -1-eps, a, b, h)
R_K_4_S(t_0, -1, -1+eps, a, b, h)

R_K_4_S(t_0, 0-eps, -2, a, b, h)
R_K_4_S(t_0, 0+eps, -2, a, b, h)
R_K_4_S(t_0, 0, -2-eps, a, b, h)
R_K_4_S(t_0, 0, -2+eps, a, b, h)

R_K_4_S(t_0, 2-10*eps, 2, a, b, h)
R_K_4_S(t_0, 2+10*eps, 2, a, b, h)
R_K_4_S(t_0, 2, 2-10*eps, a, b, h)
R_K_4_S(t_0, 2, 2+10*eps, a, b, h)
plt.show()