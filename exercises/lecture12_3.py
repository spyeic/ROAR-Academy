import numpy as np

def swap_rows(M, a, b):
    M[a], M[b] = M[b],M[a].copy()

def swap_cols(M, a, b):
    for i in range(len(M)):
        M[i][a], M[i][b] = M[i][b], M[i][a]


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
swap_rows(matrix, 0, 1)
print(matrix)
swap_cols(matrix, 0, 1)
print(matrix)
