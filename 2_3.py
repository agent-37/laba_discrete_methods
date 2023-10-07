import numpy as np
from cmath import sqrt


def dist(vec_a):
    sum = 0
    for i in vec_a:
        sum += i * i
    a = sqrt(sum)
    return a.real


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
    for i in range(len(matrix)):
        if matrix[i, i] == 0:
            print('Матрица не коректна')
            return 1
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
method(matrix, epsilon, B)

# 0, -0.1, 0.1; -0.1, 0, 0.1; 0.1, -0.1, 0
