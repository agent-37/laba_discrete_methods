import warnings
import numpy as np

from scipy.misc import derivative

warnings.simplefilter("ignore", DeprecationWarning)


def f(x):
    return x - 1 + 1 / 2 * np.e ** x


def ffd(x):
    return derivative(f, x, dx=0.0001, n=1)


def fsd(x):
    return derivative(f, x, dx=0.0001, n=2)


def check_fsd(left, right):
    step = 0.000001
    rg = np.arange(left, right + step, step)
    d2 = derivative(f, rg, dx=0.001, n=2)
    d1 = derivative(f, rg, dx=0.001, n=1)
    if (np.all(d2 > 0) or np.all(d2 < 0)) and np.all(d1 != 0):
        return True
    return False


def main():
    left, right = map(float, input('Введите интервал: ').split())
    while not check_fsd(left, right):
        print('Интервал не подходит')
        left, right = map(float, input('Введите интервал: ').split())
    x = (left + right) / 2
    x_new = x - f(x) / ffd(x)
    it = 1
    while np.abs(x_new - x) > EPS:
        x = x_new
        x_new = x - f(x) / ffd(x)
        it += 1
    print(x_new, it)
    print(x_new)


# Подходящий интервал [1, 1.25]
if __name__ == "__main__":
    EPS = 0.0001
    main()
