from cmath import sin, cos, e
import matplotlib.pyplot as plt


def f(x):
    return -2 * x


# def s_solve(Y, x):
#     global p, q
#     return [Y[0], -p * Y[1] - q * Y[0] - f(x)]


def gaus(matrix, b):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[j], matrix[i] = matrix[i], matrix[j]
                    b[i], b[j] = b[j], b[i]
                    break
        k = matrix[i][i]
        if k == 0:
            return None
        b[i] /= k
        for j in range(i, n):
            matrix[i][j] /= k
        for j in range(i + 1, n):
            k = matrix[j][i]
            if k != 0:
                b[j] -= k * b[i]
                for h1 in range(i, n):
                    matrix[j][h1] -= k * matrix[i][h1]
        # print(matrix)
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            b[j] -= b[i] * matrix[j][i]
            matrix[j][i] = 0

    return b


def y(x):
    global c1, c2
    return c1 / e ** x + c2 / e ** (3 * x) - 2 * x / 3 + 8 / 9


n = 20
a, b = 1, 2
h = (b - a) / n
alp1, beta1, gamma1 = 0, 1, 0
alp2, beta2, gamma2 = -1, 1, 1
p, q = 4, 3
c1, c2 = 1.15925231190463, 7.318712771423379
matrix = []
b = []
for i in range(1, n):
    buf = [0 for j in range(n + 1)]
    buf[i - 1] = 1
    buf[i] = -2 - p * h + q * h ** 2
    buf[i + 1] = 1 + p * h
    # print(buf)
    matrix.append(buf)
    b.append(f(a + i * h) * h ** 2)
buf1, buf2 = [0 for j in range(n + 1)], [0 for j in range(n + 1)]
buf1[0] = 1
buf1[1] = beta1 / (h*(alp1 - beta1 / h))
matrix.append(buf1)
b.append(gamma1/(alp1 - beta1 / h))

buf2[n] = 1
buf2[n - 1] = -beta2 / (h*(alp2 + beta2 / h))
matrix.append(buf2)
b.append(gamma2/(alp2 + beta2 / h))

tim = [a + i * h for i in range(n + 1)]
ans = gaus(matrix, b)
# print(ans)
plt.plot(tim, ans)
y1 = [y(a + i * h) for i in range(n + 1)]
plt.plot(tim, y1)
plt.show()
