import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 로드 및 전처리
data = pd.read_csv('../data/AAPL.txt', parse_dates=['Date'], index_col='Date')
data.dropna(inplace=True)

# 일일 미래 수익률 계산
data['Future Return'] = data['Adj Close'].pct_change().shift(-1)
print(data['Future Return'])

np.random.seed(0)
data['Signal'] = np.random.choice([0, 1], size=len(data), p=[0.5, 0.5])
print(data['Signal'])

# 백테스트 수행: 일일 PnL 계산
data['Daily PnL'] = data['Signal'] * data['Future Return']
print(data['Daily PnL'])

# 투자된 총 금액과 총 수익 계산
total_invested = 1 * data['Signal'].sum()  # 1달러씩 투자했다고 가정
total_earned = data['Daily PnL'].sum()
print(total_earned)

# 전략의 수익률 계산
strategy_return = total_earned / total_invested
print(strategy_return)

# 'Always Buy' 신호에 대한 일일 PnL 계산
data['Always Buy Signal'] = 1  # 항상 매수 신호
data['Always Buy Daily PnL'] = data['Always Buy Signal'] * data['Future Return']

# 전략에 따른 일일 PnL 계산
data['Strategy Daily PnL'] = data['Signal'] * data['Future Return']

# 전략에 따른 총 PnL 계산
total_strategy_pnl = data['Strategy Daily PnL'].sum()
print(total_strategy_pnl)

# 항상 매수 전략에 따른 총 PnL 계산
total_always_buy_pnl = data['Always Buy Daily PnL'].sum()
print(total_always_buy_pnl)

# 전략 수익률 계산
strategy_return = total_strategy_pnl / data['Signal'].sum()
print(strategy_return)

# 항상 매수 전략 수익률 계산
always_buy_return = total_always_buy_pnl / data['Always Buy Signal'].sum()
print(always_buy_return)

# 일일 PnL 시각화
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Strategy Daily PnL'], label='Strategy Daily PnL')
plt.plot(data.index, data['Always Buy Daily PnL'], label='Always Buy Daily PnL', alpha=0.7)
plt.legend()
plt.title("Daily PnL Comparison")
plt.xlabel("Date")
plt.ylabel("Daily PnL")
plt.show()
