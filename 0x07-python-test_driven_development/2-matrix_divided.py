#!/usr/bin/python3
"""
module: function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix."""

    new_matrix = matrix.copy()
    i = 0
    while i < len(new_matrix):
        j = 0
        while j < len(new_matrix[i]):
            if not isinstance(new_matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            j += 1
        i += 1
    i = 1
    while i < len(matrix):
        if len(new_matrix[i]) != len(new_matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    def f_div(num):
        num = num / div
        return round(num, 2)
    i = 0
    while i < len(matrix):
        new_matrix[i] = list(map(f_div, new_matrix[i]))
        i += 1
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
