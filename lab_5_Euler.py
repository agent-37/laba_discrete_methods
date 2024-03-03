import matplotlib.pyplot as plt


def f(t, x):
    return t * x


def sys_f_x(t, x, y):
    return y


def sys_f_y(t, x, y):
    return -y / t - x


def Euler(t_0, x_0, a, b, h):
    points_t, points_x = [t_0], [x_0]
    while t_0 < b:
        t_0 += h
        x_0 += h * f(t_0, x_0)
        points_t.append(t_0)
        points_x.append(x_0)
    plt.plot(points_t, points_x)
    plt.show()


def Euler_sys(t_0, x_0, y_0, a, b, h):
    points_x, points_y = [x_0], [y_0]
    while t_0 < b:
        t_0 += h
        x_0 += h * sys_f_x(t_0, x_0, y_0)
        y_0 += h * sys_f_y(t_0, x_0, y_0)
        points_x.append(x_0)
        points_y.append(y_0)
    plt.plot(points_x, points_y)
    plt.show()


# a,b=0,1
# t_0, x_0, h = map(float, input().split())
# Euler(t_0, x_0, a, b, h)

a, b = 1, 12
t_0, x_0, y_0, h = 1, 0.7, -0.4, 0.1
Euler_sys(t_0, x_0, y_0, a, b, h)
