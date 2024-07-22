import numpy as np


def compute_vector_len(vector):
    len_of_vector = np.linalg.norm(vector)

    return len_of_vector


def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)

    return dot_product


def matrix_multi_vector(matrix, vector):
    return matrix @ vector


def matrix_multi_matrix(matrix1, matrix2):
    return matrix1 @ matrix2


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)
