# Exercise 3: Multi asset returns
import pandas as pd
import numpy as np

business_dates = pd.bdate_range('2021-01-01', '2021-12-31')
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

market_data = pd.DataFrame(index=index, data=np.random.randn(len(index), 1), columns=['Price'])

market_data_reset = market_data.reset_index()

pivoted_data = market_data_reset.pivot_table(index='Date', columns='Ticker', values='Price')
#pct_change : return(d) = (price(d)-price(d-1))/price(d-1)
daily_returns = pivoted_data.pct_change()

print(daily_returns.head())


