#Exercise 3: Slicing
import numpy as np

array_1_to_100 = np.arange(1, 101)

array_odd = array_1_to_100[array_1_to_100 % 2 != 0]

array_even_reversed = array_1_to_100[array_1_to_100 % 2 == 0][::-1]

array_modified = array_1_to_100.copy()
array_modified[1::3] = 0

print("Q1:", array_1_to_100)
print("Q2:", array_odd)
print("Q3:", array_even_reversed)
print("Q4:", array_modified)
