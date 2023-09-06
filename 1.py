import numpy as np


def cross(vec_a, vec_b):
    ''' Функция для нахождения скалярного произведения'''
    return vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1] + vec_a[2] * vec_b[2]


def norm_vec(vec_a):
    '''Функция для нормализации вектора'''
    buf_max = max(vec_a[0], vec_a[1], vec_a[2])
    return vec_a / buf_max


matrix = np.matrix('1.7 0.8 0.9; 0.8 0.7 0.3; 0.9 0.3 1.7')
vectors = [np.matrix('1; 1; 1'), matrix @ np.matrix('1; 1; 1')]
alpha_matrix = [cross(vectors[0], vectors[1]) / cross(vectors[0], vectors[0])]
while True:
    vec_size = len(vectors)
    vectors.append(matrix @ vectors[vec_size - 1])
    alpha_matrix.append(
        cross(vectors[vec_size - 1], vectors[vec_size]) / cross(vectors[vec_size - 1],
                                                                vectors[vec_size - 1]))
    size = len(alpha_matrix)
    if abs(alpha_matrix[size - 1] - alpha_matrix[size - 2]) < 1e-15:
        break
result_alpha = alpha_matrix[len(alpha_matrix) - 1]

vec = [vectors[0], vectors[1], vectors[2]]
second_alpha = [(cross(vec[2], vec[1]) - result_alpha * cross(vec[1], vec[1])) / (
        cross(vec[1], vec[1]) - result_alpha * cross(vec[1], vec[0]))]

while True:

    vec_size = len(vec)
    vec.append(matrix @ vec[vec_size - 1])
    second_alpha.append(
        (cross(vec[vec_size], vec[vec_size - 1]) - result_alpha * cross(vec[vec_size - 1], vec[vec_size - 1])) / (
                    cross(vec[vec_size - 1], vec[vec_size - 1]) - result_alpha * cross(vec[vec_size - 1],
                                                                                       vec[vec_size - 2])))
    size = len(second_alpha)
    if abs(second_alpha[size - 1] - second_alpha[size - 2]) < 1e-5:
        break

# print(second_alpha)

print('Первое собственное значение', result_alpha, 'Второе собственное значение', second_alpha[len(second_alpha) - 1],
      'Собственный вектор', norm_vec(vectors[len(vectors) - 1]), sep='\n')
# print(matrix @ vectors[len(vectors) - 1])
# print(alpha_matrix,sep='\n')
