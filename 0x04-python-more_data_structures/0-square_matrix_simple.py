#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = [[i ** 2 for i in row] for row in matrix]
    return newm
