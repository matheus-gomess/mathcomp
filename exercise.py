import numpy as np
import matplotlib.pyplot as plt 

#

A = np.array([[2, 1], [1, -1]])
B = np.array([5, 1])

X = np.linalg.solve(A, B)
x_intersec, y_intersec = X
print(f"Interseção: x = {x_intersec:.2f}, y = {y_intersec:.2f}")
