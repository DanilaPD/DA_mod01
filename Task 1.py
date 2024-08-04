import numpy as np

array1 = np.array([[1, 39, 41, 33], [2, 38, 32, 18], [3, 27, 14, 17], [4, 22, 21, 22], [5, 20, 28, 23]])

print(array1)
print()

array2 = array1[:, [1, 2, 3]]
print(array2)
print()

array3 = array2.sum(axis=1)
print(array3)
