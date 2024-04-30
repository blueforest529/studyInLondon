#Exercise 1: Series

import pandas as pd

dates = pd.date_range(start='2010-01-01', end='2020-12-31')
days_since_start = (dates - pd.Timestamp('2010-01-01')).days
integer_series = pd.Series(data=days_since_start, index=dates)
print(integer_series.head())

moving_average_7d = integer_series.rolling(window=7).mean()
print(moving_average_7d.head(10))
