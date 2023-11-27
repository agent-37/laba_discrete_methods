from cmath import sin, log


def func(x):
    # Функция данная в условии
    return (x * x * x - 6 * x - 8).real


def dpfunc(x):
    return (3 * x * x - 6).real


def find_new_x(cur_x):
    return cur_x - func(cur_x) / dpfunc(cur_x)


print('Введите отрезок на котором хотите найти корень')
l, r = map(float, input().split())
eps = 0.0001
present_x = -1e18
cur_x = (r + l) / 2
step = 0
while abs(cur_x - present_x) > eps or step > 1000:
    step += 1
    present_x = cur_x
    cur_x = find_new_x(cur_x)
print(step, cur_x)
