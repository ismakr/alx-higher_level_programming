#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    def sq(n):
        n = n * n
        return n
    i = 0
    while i < len(matrix):
        new_matrix[i] = list(map(sq, new_matrix[i]))
        i += 1
    return new_matrix
