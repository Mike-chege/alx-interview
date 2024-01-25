#!/usr/bin/env python3
"""
This script, rotates a n x n 2D matrix
90 degrees clockwise
"""

def rotate_2d_matrix(m):
    """
    Rotating the matrix
    """
    n = len(m)
    temp1, temp2 = 0, 0

    for j in range(0, len(m) // 2 + 1):
        for i in range(j, n - 1):
            temp1 = m[i][n - 1]
            m[i][n - 1] = m[j][i]
            temp2 = m[n - 1][n - 1 - i + j]
            m[n - 1][n - 1 - i + j] = temp1
            temp1 = m[n - 1 - i + j][j]
            m[n - 1 - i + j][j] = temp2
            m[j][i] = temp1
        n -= 1
