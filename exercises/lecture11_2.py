from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lenna = image.imread(path + "/samples/lenna.bmp")
flag = image.imread(path + "/exercises/flag.jpeg")

lenna_data = lenna.copy()
# print(flag.shape) 167, 250, 3
height, width, _ = flag.shape

for i in range(height):
    for j in range(width):
        lenna_data[i][512 - width + j] = flag[i][j]

pyplot.imshow(lenna_data)
pyplot.show()

# flag_height = flag.shape[0]
# flag_width = flag.shape[1]
# data[:flag_height, -flag_width:] = flag

