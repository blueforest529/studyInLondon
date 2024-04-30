#Exercise 2: Financial data

import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# Apple 주식 데이터 다운로드
apple_stock = yf.download('AAPL', start='2023-01-01', end='2023-12-31')

print(apple_stock.head(10))

# 캔들스틱 차트 생성
fig = go.Figure(data=[go.Candlestick(x=apple_stock.index,
                open=apple_stock['Open'],
                high=apple_stock['High'],
                low=apple_stock['Low'],
                close=apple_stock['Close'])])

# 차트 제목 및 축 라벨 설정
fig.update_layout(title='Apple Stock Candlestick Chart 2021',
                  xaxis_title='Date',
                  yaxis_title='Price (USD)',
                  xaxis_rangeslider_visible=False)  # 범위 슬라이더 비활성화

# 차트 보여주기
fig.show()

aggregated = apple_stock.resample('BM').agg({'Open': 'first', 
                                              'High': 'max', 
                                              'Low': 'min', 
                                              'Close': 'last'})

print(aggregated)

num_months = len(aggregated)
print(num_months)


# open 가격을 기반으로 한 일일 수익률 계산
prices = apple_stock['Open']
daily_returns_vectorized = (prices - prices.shift(1)) / prices.shift(1)

print(daily_returns_vectorized.head())