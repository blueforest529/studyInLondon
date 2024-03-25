#Exercise 6: Plotly 1
import pandas as pd
import numpy as np
import plotly.express as px

returns = np.random.randn(50)
price = 100 + np.cumsum(returns)

dates = pd.date_range(start='2020-09-01', periods=50, freq='B')
df = pd.DataFrame(zip(dates, price), 
                  columns=['Date', 'Company_A'])

fig = px.line(df, x='Date', y='Company_A', title='Company_1 stock price')
fig.update_layout(xaxis_title='Date', yaxis_title='Company_A')
fig.show()
