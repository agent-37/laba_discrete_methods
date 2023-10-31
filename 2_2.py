import numpy as np
from cmath import sqrt


def dist(vec_a):
    sum = 0
    for i in vec_a:
        sum += i * i
    a = sqrt(sum)
    return a.real


def norm_vec(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    for i in range(len(vec_a)):
        buf_max += vec_a[i] * vec_a[i]
    return vec_a / sqrt(buf_max).real

def norm_max(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = 0
    for i in range(len(vec_a)):
        buf_max =max(buf_max, abs(vec_a[i]))
    return buf_max

def dist2(vec_a, vec_b):
    sum = 0
    for i in range(len(vec_a)):
        sum = max(sum, abs(vec_a[i] - vec_b[i]))
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


epsilon = 0.0001


def find_x_n(matrix, cur, B, s):
    ans = np.matrix(s)
    for i in range(len(matrix)):
        sum = 0
        for j in range(i):
            sum += matrix[i, j] * ans[j]
        for j in range(i + 1, len(matrix)):
            sum += matrix[i, j] * cur[j]
        ans[i] = (-sum + B[i]) / matrix[i, i]
    return ans


def method(matrix, epsilon, B):
    s = '1.0'
    for i in range(len(matrix) - 1):
        s = s + '; 1.0'
    vector_x = [np.matrix(s)]
    for i in range(10000):
        # print(find_x_n(matrix, vector_x[len(vector_x) - 1], B, s))
        vector_x.append(find_x_n(matrix, vector_x[len(vector_x) - 1], B, s))

        if (norm_max(vector_x[len(vector_x) - 1] - vector_x[len(vector_x) - 2])) / (
        norm_max(vector_x[len(vector_x) - 2])) < epsilon:
            print("Решение =", vector_x[len(vector_x) - 1], "полученный на шаге", i)
            print("Невязка", matrix @ vector_x[len(vector_x)-1]-B)
            # print(vector_x[len(vector_x)-2])
            # print(np.linalg.norm(matrix))

            return
    print('Для данной матрицы метод Зейделя не работает')


matrix = read_matrix()
B = read_vector()
#check_correct_matrix(matrix)
#B = matrix.transpose() @ B
#matrix = matrix.transpose() @ matrix
if (check_correct_matrix(matrix)):
    method(matrix, epsilon, B)
else:
    B = matrix.transpose() @ B
    matrix = matrix.transpose() @ matrix
    if (check_correct_matrix(matrix)):
        method(matrix, epsilon, B)
    else:
        print('Приводите к диагональному виду')
        B = np.linalg.inv(matrix) @ B
        matrix = np.linalg.inv(matrix) @  matrix
        print(B)
# 2, -0.1, 0.1; -0.1, 2, 0.1; 0.1, -0.1, 2


#  7.6 5.8 4.7; 3.8 4.1 2.7; 2.9 2.1 3.8
# 10.1; 9.7; 7.8


# 1.7 2.8 1.9; 2.1 3.4 1.8; 4.2 -1.7 1.3
# 0.7;1.1; 2.8
