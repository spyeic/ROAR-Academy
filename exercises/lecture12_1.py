import numpy as np

v = np.array([2., 2., 4.])

e0 = v.dot(np.array([1, 0, 0]))
e1 = v.dot(np.array([0, 1, 0]))
e2 = v.dot(np.array([0, 0, 1]))
print(e0, e1, e2)