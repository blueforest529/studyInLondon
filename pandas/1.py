#Exercise 1: Your first DataFrame

import pandas as pd 
import numpy as np

data = [('Blue', [1,2], 1.1),
        ('Red', [3,4], 2.2),
        ('Pink', [5,6], 3.3),
        ('Grey', [7,8], 4.4),
        ('Black', [9,10], 5.5)]

#데이터 구조 정의
dtype = [('color', str), ('list', list), ('number', float)]

data_np = np.array(data, dtype=dtype)

pd_data = pd.DataFrame(data_np, 
                   index=[i for i in range(1, len(data) * 2, 2)], 
                   columns=['color', 'list', 'number'])

print(pd_data)

print(type(pd_data.iloc[0, :]))
print(type(pd_data.iloc[1, :]))
print(type(pd_data.iloc[2, :]))

