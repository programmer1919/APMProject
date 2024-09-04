from portfoliovalue import portfolio_values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load SPY data
spy = pd.read_csv('CSVFiles/SPY.csv', parse_dates=['Date'], index_col='Date')
spy = spy['Close'].resample('D').last().dropna()  # Resample and align with portfolio data

# Ensure the data aligns by finding the intersection of dates
aligned_data = pd.concat([portfolio_values, spy], axis=1).dropna()
aligned_data.columns = ['Portfolio', 'SPY']

# Calculate daily returns for both portfolio and SPY
returns = aligned_data.pct_change().dropna()

# Calculate the rolling 1-month (21 trading days) beta
rolling_window = 21
rolling_covariance = returns['Portfolio'].rolling(window=rolling_window).cov(returns['SPY'])
rolling_variance = returns['SPY'].rolling(window=rolling_window).var()
rolling_beta = rolling_covariance / rolling_variance

# Plot the rolling beta
plt.figure(figsize=(12, 6))
plt.plot(rolling_beta, label="Rolling 1-Month Beta with SPY", color="green")
plt.title("Rolling 1-Month Beta of Portfolio with SPY")
plt.xlabel("Date")
plt.ylabel("Beta")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
