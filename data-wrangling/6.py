#Exercise 6: Unstack

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


business_dates = pd.bdate_range('2021-01-01', '2021-12-31')
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])
market_data = pd.DataFrame(index=index, data=np.random.randn(len(index), 1), columns=['Prediction'])


market_data_unstacked = market_data.unstack(level='Ticker')

print(market_data_unstacked.head(3))

market_data_unstacked.plot(figsize=(15, 7))
plt.xlabel("Date")
plt.ylabel("Prediction")
plt.legend([ticker for ticker in tickers], loc="upper left")
plt.show()
