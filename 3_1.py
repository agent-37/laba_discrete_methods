from cmath import sin, log


def func(x):
    # Функция данная в условии
    return (x * log(x)-1.5  ).real


def find_new_x(l, r, sign, cur_x):
    e = func(l)
    if e > 0:
        e = 1
    else:
        e = 0
    if (e + sign) % 2 == 0:
        return cur_x - (func(cur_x) * (cur_x - l)) / (func(cur_x) - func(l))
    else:
        return cur_x - (func(cur_x) * (r - cur_x)) / (func(r) - func(cur_x))


print('Введите отрезок на котором хотите найти корень')
l, r = map(float, input().split())
print('Введите знак производной на этом интервале(+1, если > 0, и 0, если < 0)')
sign = int(input())
eps = 0.0001
present_x = -1e18
cur_x = l - (func(l) * (r - l)) / (func(r) - func(l))
step = 0
while abs(cur_x - present_x) > eps or step > 1000:
    step += 1
    present_x = cur_x
    cur_x = find_new_x(l, r, sign, cur_x)
print(step, cur_x)
