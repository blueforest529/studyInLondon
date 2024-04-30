#Exercise 6: Broadcasting and Slicing
import numpy as np

array = np.ones((9, 9), dtype=np.int8)
idx = [1,2,3,4]

for idx, i in enumerate(idx):
    array[i:-i, i:-i] = idx % 2

print(array)

array_1 = np.array([1,2,3,4,5], dtype=np.int8)  
array_2 = np.array([1,2,3], dtype=np.int8) 
mat = np.reshape(array_1, (5, 1))

print(mat * array_2)