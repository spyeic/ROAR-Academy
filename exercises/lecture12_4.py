import numpy as np

def set_array(L, rows, cols):
    result = np.zeros((rows, cols))
    for row in range(rows):
        for col in range(cols):
            result[row][col] = L[row * cols + col]
            
    return result


arr = [1, 3, 5, 7, 9, 11]
set_array(arr, 3, 2)