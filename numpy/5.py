#Exercise 5: Split, concatenate, reshape arrays
import numpy as np

first = np.arange(1, 51)
second = np.arange(51, 101)
merge = np.concatenate((first, second), axis=None)
merge = merge.reshape(10,10)

print(first)
print(second)
print(merge)