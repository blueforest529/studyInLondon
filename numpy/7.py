#Exercise 7: NaN
import numpy as np

generator = np.random.default_rng(123)
grades = np.round(generator.uniform(low = 0.0, high = 10.0, size = (10, 2)))
grades[[1,2,5,7], [0,0,0,0]] = np.nan


new_arr = np.where(~np.isnan(grades[:, 0]), grades[:,0], grades[:,1])
print(np.hstack((grades, new_arr.reshape(-1,1))))
