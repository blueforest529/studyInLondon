#Exercise 1: Your first NumPy array

import numpy as np

integer = 10
float_num = 3.14
string = "hello"
dictionary = {'a': 1, 'b': 2}
list_ = [1, 2, 3]
tuple_ = (4, 5, 6)
set_ = {7, 8, 9}
boolean = True

np_array = np.array([integer, float_num, string, dictionary, list_, tuple_, set_, boolean], dtype=object)

for i in np_array:
    print(type(i))