import numpy as np

arr = np.zeros((6, 6))
for row in range(6):
    for col in range(6):
        arr[row][col] = row * 10 + col


pink = arr[1:2, 2:4]
green = arr[2:4, 4:]
blue = arr[:,1:2]
orange = arr[2::2, ::2]
print(pink)
print(green)
print(blue)
print(orange)