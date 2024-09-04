from project import df
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

# Normalize both portfolio and SPY to start at 100 for better comparison
aligned_data['Portfolio'] = (aligned_data['Portfolio'] / aligned_data['Portfolio'].iloc[0]) * 100
aligned_data['SPY'] = (aligned_data['SPY'] / aligned_data['SPY'].iloc[0]) * 100

# Plot portfolio performance against SPY
plt.figure(figsize=(12, 6))
plt.plot(aligned_data.index, aligned_data['Portfolio'], label="Portfolio", color="blue")
plt.plot(aligned_data.index, aligned_data['SPY'], label="S&P 500 (SPY)", color="orange")
plt.title("Portfolio Performance vs. S&P 500 (SPY)")
plt.xlabel("Date")
plt.ylabel("Normalized Value (Starting at 100)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()