import numpy as np

def set_array(L, rows, cols):
    result = np.zeros((rows, cols))
    for col in range(cols):
        for row in range(rows):
            result[row][col] = L[col * rows + row]
            
    return result


arr = [1, 3, 5, 7, 9, 11]
result = set_array(arr, 3, 2)
print(result)