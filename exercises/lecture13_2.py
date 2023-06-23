import numpy as np
import matplotlib.pyplot as plt


plt.plot([1, 2, 3], [2, 4, 1], color="b")
plt.xlim(1, 3)
plt.ylim(1, 4)
plt.xticks(np.arange(1, 3.5, 0.5))
plt.yticks(np.arange(1, 4.5, 0.5))

plt.title("Sample graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.show()