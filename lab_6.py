from cmath import sin, cos, e
import matplotlib.pyplot as plt


def f(x):
    return sin(x).real


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
    return sin(x) / 10 + 3 / 10 * cos(x) + c1 * e ** (2 * x) + c2 * e ** x


def rec(pos, q_i, phi_i, q_i_1, phi_i_1):
    global ans, n, p, q, h, a
    if pos == n:
        global X2, mu2
        # print(q_i,q_i_1,phi_i,phi_i_1,'!!!!')
        y_n = (mu2 + X2 * phi_i_1) / (1 + q_i_1 * X2)
        ans.append(y_n)
        print(pos, y_n)
        return y_n
    e_i, d_i, g_ii = 1 + p * h, -2 - p * h + q * h ** 2, h ** 2 * f(a + (pos + 1) * h)
    q_ii = -e_i / (q_i + d_i)
    phi_ii = (g_ii - phi_i) / (q_i + d_i)
    y_ii = rec(pos + 1, q_ii, phi_ii, q_i, phi_i)
    y_i = y_ii * q_i + phi_i
    ans.append(y_i)
    print(pos, y_i)
    return y_i


n = 200
a, b = 0, 1
h = (b - a) / n
alp1, beta1, gamma1 = 1, 2, -1
alp2, beta2, gamma2 = 0, 1, 1
p, q = -3, 2
c1, c2 = 0.2495746688213849, -0.9159577813689748

# q0, phi0 = -beta1 / (h * (alp1 - beta1 / h)), gamma1 / (alp1 - beta1 / h)
# q0, phi0 = beta1 / (h * (alp1 + beta1 / h)), beta1 / (h * (alp1 + beta1 / h))
# X2, mu2 = beta2 / (h * (alp2 + beta2 / h)), gamma2 / (alp2 + beta2 / h)
tim = [a + i * h for i in range(n + 1)]
# ans = []
# rec(0, q0, phi0, 0, 0)
# ans.reverse()
# print(ans)
# print(ans)
# plt.plot(tim, ans)
matrix = [[0 for j in range(n + 1)] for i in range(n + 1)]
b = [0 for i in range(n + 1)]
for i in range(1, n):
    matrix[i][i - 1] = 1 / h ** 2
    matrix[i][i] = -2 / (h ** 2) - p / h + q
    matrix[i][i + 1] = 1 / (h ** 2) + p / h
    b[i] = f(a + i * h)
b[0] = gamma1
matrix[0][0] = alp1 - beta1 / h
matrix[0][1] = beta1 / h
b[n] = gamma2
matrix[n][n] = alp2 + beta2 / h
matrix[n][n - 1] = -beta2 / h
ans = gaus(matrix, b)
plt.plot(tim, ans)
y1 = [y(a + i * h) for i in range(n + 1)]
plt.plot(tim, y1)
plt.show()
