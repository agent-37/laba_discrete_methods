import numpy as np
from cmath import sqrt


def dist(vec_a):
    sum = 0
    for i in vec_a:
        sum += i * i
    a = sqrt(sum)
    return a.real


def gauss_method(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_el = abs(matrix[i, i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k, i]) > max_el:
                max_el = abs(matrix[k, i])
                max_row = k

        # matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        # vector[i], vector[max_row] = vector[max_row], vector[i]
        if i != max_row:
            matrix[i] = matrix[i] + matrix[max_row]
            matrix[max_row] = matrix[i] - matrix[max_row]
            matrix[i] = matrix[i] - matrix[max_row]

            vector[i] = vector[i] + vector[max_row]
            vector[max_row] = vector[i] - vector[max_row]
            vector[i] = vector[i] - vector[max_row]
        for k in range(i + 1, n):
            c = -matrix[k, i] / matrix[i, i]
            for j in range(i, n):
                if i == j:
                    matrix[k, j] = 0
                else:
                    matrix[k, j] += c * matrix[i, j]
            vector[k] += c * vector[i]

    x = vector
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i, i]
        for k in range(i - 1, -1, -1):
            vector[k] -= matrix[k, i] * x[i]
    return x


def cross(vec_a, vec_b):
    sum = 0
    for i in range(len(vec_a)):
        sum += vec_a[i] * vec_b[i]
    return sum


def mult_vec(vec_a, num):
    sum = vec_a
    for i in range(len(vec_a)):
        sum[i] = vec_a[i] * num
    return sum


def read_matrix():
    str = input("Введите матрицу в таком формате. Пример формата. 1.7 0.8 0.9; 0.8 0.7 0.3; 0.9 0.3 1.7\n")
    return np.matrix(str)


def read_vector():
    str = input("Введите матрицу в таком формате. Пример формата. 1.7; 0.3; 1.7\n")
    return np.matrix(str)


def check_correct_matrix(matrix):
    polinom = []
    l = []
    for i in range(len(matrix) + 1):
        polinom.append(0)

    def count_poly(deep):
        if len(l) == len(matrix):
            sum = 1
            pos = 0
            sign = 0
            for i in range(len(matrix)):
                sum *= matrix[i, l[i]]
                if i >= l[i]:
                    pos += 1
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    if l[i] > l[j]:
                        sign += 1
            polinom[len(polinom) - pos - 1] += sum * (-1) ** (sign)

            return
        for i in range(len(matrix)):
            if i not in l:
                l.append(i)
                count_poly(deep + 1)
                l.pop()

    count_poly(0)
    max1 = 0
    print(polinom)
    r = np.roots(polinom)
    print(np.roots(polinom))
    for i in range(len(r)):
        max1 = max(max1, abs(r[i]).real)
    if max1 < 0.8:
        return 1
    else:
        return 0





epsilon = 0.00001


def find_x_n(matrix, cur, B, s):
    ans = np.matrix(s)
    for i in range(len(matrix)):
        sum = 0
        for j in range(i):
            sum += matrix[i, j] * ans[j]
        for j in range(i + 1, len(matrix)):
            sum += matrix[i, j] * cur[j]
        ans[i] = (sum + B[i]) / matrix[i, i]
    return ans


def method(matrix, epsilon, B):
    s = '1.0'
    for i in range(len(matrix) - 1):
        s = s + '; 1.0'
    vector_x = [np.matrix(s)]
    for i in range(100):
        buf = B - matrix @ vector_x[len(vector_x) - 1]
        if sqrt(cross(buf, buf)).real < epsilon:
            print("Решение =", vector_x[len(vector_x) - 2], "полученный на шаге", i)
            print('Вектор невязки', buf)
            return
        alpha = cross(buf, buf) / cross(matrix @ buf, buf)
        vector_x.append(vector_x[len(vector_x) - 1] + mult_vec(buf, alpha))
        # print(cross(buf, buf), sqrt(cross(buf, buf)).real, buf, alpha, mult_vec(buf, alpha))


matrix = read_matrix()
B = read_vector()
# check_correct_matrix(matrix)
# B = matrix.transpose() @ B
# matrix = matrix.transpose() @ matrix
buf_matrix = matrix
buf_B = B

if (check_correct_matrix(matrix)):
    method(matrix, epsilon, B)
else:
    B = matrix.transpose() @ B
    matrix = matrix.transpose() @ matrix
    if (check_correct_matrix(matrix)):
        method(matrix, epsilon, B)
    else:
        print('Приводите к диагональному виду')
        print(gauss_method(buf_matrix, buf_B))
# 0, -0.1, 0.1; -0.1, 0, 0.1; 0.1, -0.1, 0


# 1.7 2.8 1.9; 2.1 3.4 1.8; 4.2 -1.7 1.3
# 0.7;1.1; 2.8
