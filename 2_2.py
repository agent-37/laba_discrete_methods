import numpy as np
from cmath import sqrt


def dist(vec_a):
    sum = 0
    for i in vec_a:
        sum += i * i
    a = sqrt(sum)
    return a.real


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
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += abs(matrix[i, j])
        if sum >= abs(matrix[i, i]) == 0:
            print('Матрица не коректна')
            return 0
    return 1


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
        vector_x.append(find_x_n(matrix, vector_x[len(vector_x) - 1], B, s))
        if np.linalg.norm(matrix) / abs(1.0 - np.linalg.norm(matrix)) * dist2(
                vector_x[len(vector_x) - 1], vector_x[len(vector_x) - 2]) < epsilon:
            print("Решение =", vector_x[len(vector_x) - 1], "полученный на шаге", i)
            # print(vector_x[len(vector_x)-2])
            # print(np.linalg.norm(matrix))

            return
    print('Для данной матрицы метод Зейделя не работает')

matrix = read_matrix()
if check_correct_matrix(matrix):
    B = read_vector()
    method(matrix, epsilon, B)

# 2, -0.1, 0.1; -0.1, 2, 0.1; 0.1, -0.1, 2
