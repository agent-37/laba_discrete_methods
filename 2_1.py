import numpy as np


def read_matrix():
    str = input("Введите матрицу в таком формате. Пример формата. 1.7 0.8 0.9; 0.8 0.7 0.3; 0.9 0.3 1.7\n")
    return np.matrix(str)


vector_G = np.matrix("1.1; 1; 1")
epsilon = 0.00001


def check_all_lambda_correct(l, B):

    for i in range(len(B)):
        if abs(l[i]) >= 1:
            return False
    return True


def method(B, G, epsilon):
    l = np.linalg.eigvals(B)
    vector_x = [G]
    check_all_lambda_correct(l, B)
    for i in range(100):
        vector_x.append(B @ vector_x[len(vector_x) - 1] + G)
        if np.linalg.norm(vector_x[len(vector_x) - 1] - vector_x[len(vector_x) - 2]) / np.linalg.norm(
                vector_x[len(vector_x) - 2]) < epsilon:
            print("Решение =", vector_x[len(vector_x) - 1], "полученный на шаге", i)
            print('Невязка =', np.linalg.norm((np.identity(len(B)) - B) @ vector_x[len(vector_x) - 2] - G))
            break
print("What heppened")

B = read_matrix()
method(B, vector_G, epsilon)

# 0, -0.1, 0.1; -0.1, 0, 0.1; 0.1, -0.1, 0