import numpy as np

a = np.array([[3, 2, -1], [2, -2, 4], [-1, 1/2, -1]])
b = np.array([1, -2, 0])

x = np.linalg.solve(a,b)
print(x)