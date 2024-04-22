#!/usr/bin/python3
""" Rotation of 2D Matrix in Python
"""


def rotate_2d_matrix(matrix):
    """ Rotates an n x n 2D matrix
        90 degree clockwise
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)
