#Exercise 4: Random
import numpy as np

np.random.seed(888)
array_normal = np.random.normal(size=100)
array_random_integers_2d = np.random.randint(1, 11, (8,8))
array_random_integers_3d = np.random.randint(1, 18, (4,2,5))

print(array_normal)
print(array_random_integers_2d)
print(array_random_integers_3d)