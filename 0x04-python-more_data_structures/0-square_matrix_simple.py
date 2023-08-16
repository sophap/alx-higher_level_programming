#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[0 for _ in range(len(row))] for row in matrix]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            result[x][y] = matrix[x][y] ** 2
    return result
